from functools import reduce
from AST import *
from Visitor import *
from StaticError import *
class Stype(ABC):
    pass
class VariableType(Stype):
    def __init__(self, returnType: str(Type), is_const: bool) -> None:
        self.returnType = returnType
        self.is_const = is_const
class ParamType(Stype):
    def __init__(self, returnType: str(Type)) -> None:
        self.returnType = returnType
        self.is_const = False
class AttrType(Stype):
    def __init__(self, returnType: str(Type), kind: str, is_const: bool) -> None:
        self.returnType = returnType
        self.kind = kind
        self.is_const = is_const
class MethodType(Stype):
    def __init__(self, kind: str, paramType, returnType: str(Type)) -> None:
        self.kind = kind
        self.paramType = paramType
        self.returnType = returnType
        self.is_const = False
class Symbol:
    def __init__(self, name: str, kind: str(Kind), stype=None, value=None, parentname=None) -> None:
        self.name = name
        self.kind = kind
        self.stype = stype
        self.value = value
        self.parentname = parentname
class SymbolTable:
    def __init__(self, symbols = [], next=None, prev=None, currentmethod=None, in_for_loop=None, currentclass=None) -> None:
        self.symbols = symbols
        self.next = next
        self.prev = prev
        self.currentmethod = currentmethod
        self.in_for_loop = in_for_loop
        self.currentclass = currentclass
class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visit(self.ast, {})
    def visitProgram(self, ast: Program, classes={}):
        self.classes = GlobalEnvironment().visit(ast, None)
        for clss in ast.decl:
            class_name = clss.classname.name
            class_table = self.classes.get(class_name).get('table')
            self.visit(clss, class_table)
        return []
    def visitClassDecl(self, ast: ClassDecl, table: SymbolTable):
        table.currentclass = ast.classname.name
        return [self.visit(mem, table) for mem in ast.memlist]
    def visitAttributeDecl(self, ast: AttributeDecl, table: SymbolTable):
        self.visit(ast.decl, table)
    def visitMethodDecl(self, ast: MethodDecl, table: SymbolTable):
        name = ast.name.name
        new_table = SymbolTable([], next=table, currentmethod=name)
        table.prev = new_table
        for var in ast.param:
            var_name = var.variable.name
            var_type = str(var.varType)
            if var_name in map(lambda x: x.name, new_table.symbols):
                raise Redeclared(Parameter(), var_name)
            if var.varInit is not None and False == self.compareType(var_type, self.visit(var.varInit, table)[0]):
                pass
            new_table.symbols.append(
                Symbol(var_name, str(Variable()), ParamType(var_type)))
        for decl in ast.body.decl:
            kind = Variable() if isinstance(decl, VarDecl) else Constant()
            name, type, is_const = self.visit(decl, new_table)
            decl_symbol = Symbol(name, str(kind), VariableType(type, is_const))
            new_table.symbols.append(decl_symbol)
        for stmt in ast.body.stmt:
            self.visit(stmt, new_table)
    def visitBlock(self, ast: Block, table: SymbolTable):
        new_table = SymbolTable([], next=table)
        table.prev = new_table
        for decl in ast.decl:
            kind = Variable() if isinstance(decl, VarDecl) else Constant()
            name, type, is_const = self.visit(decl, new_table)
            decl_symbol = Symbol(name, str(kind), VariableType(type, is_const))
            new_table.symbols.append(decl_symbol)
        for stmt in ast.stmt:
            self.visit(stmt, new_table)
    def visitVarDecl(self, ast: VarDecl, table: SymbolTable):
        name = ast.variable.name
        if self.is_valid_class_type(ast.varType) == False:
            raise Undeclared(Class(), ast.varType.classname.name)
        type = str(ast.varType)
        is_const = False
        if table.next is None:
            if isinstance(ast.varInit, Id):
                raise Undeclared(Identifier(), name)
        if name in map(lambda x: x.name, table.symbols) and table.next is not None:
            raise Redeclared(Variable(), name)
        if ast.varInit is not None and False == self.compareType(type, self.visit(ast.varInit, table)[0]):
            raise TypeMismatchInStatement(ast)
        return name, type, is_const
    def visitConstDecl(self, ast: ConstDecl, table: SymbolTable):
        name = ast.constant.name
        if self.is_valid_class_type(ast.constType) == False:
            raise Undeclared(Class(), ast.constType.classname.name)
        type = str(ast.constType)
        is_const = True
        if table.next is None:
            if isinstance(ast.value, Id):
                raise Undeclared(Identifier(), name)
        if name in map(lambda x: x.name, table.symbols) and table.next is not None:
            raise Redeclared(Constant(), name)
        if ast.value is None:
            raise IllegalConstantExpression(None)
        type_value, is_value_const = self.visit(ast.value, table)
        if is_value_const != True:
            raise IllegalConstantExpression(ast.value)
        if self.compareType(type, type_value) == False:
            raise TypeMismatchInConstant(ast)
        return name, type, is_const
    def visitAssign(self, ast: Assign, table: SymbolTable):
        type_lhs, _ = self.visit(ast.lhs, table)
        type_exp, _ = self.visit(ast.exp, table)
        if StaticChecker.checkIsConstant(ast.lhs, table):
            raise CannotAssignToConstant(ast)
        if self.compareType(type_lhs, type_exp) == False or type_lhs == str(VoidType()):
            raise TypeMismatchInStatement(ast)
    def visitIf(self, ast: If, table: SymbolTable):
        type_expr = self.visit(ast.expr, table)[0]
        if type_expr != str(BoolType()):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, table)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, table)
    def visitFor(self, ast: For, table: SymbolTable):
        type_id, is_id_const = self.visit(ast.id, table)
        type_expr1 = self.visit(ast.expr1, table)[0]
        type_expr2 = self.visit(ast.expr2, table)[0]
        table.in_for_loop = True
        if is_id_const:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        if type_id != str(IntType()) or type_expr1 != str(IntType()) or type_expr2 != str(IntType()):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, table)
    def visitBreak(self, ast: Break, table: SymbolTable):
        table = table.next
        while table.next is not None:
            if table.in_for_loop == True:
                return
            table = table.next
        raise MustInLoop(ast)
    def visitContinue(self, ast: Continue, table: SymbolTable):
        table = table.next
        while table.next is not None:
            if table.in_for_loop == True:
                return
            table = table.next
        raise MustInLoop(ast)
    def visitReturn(self, ast: Return, table: SymbolTable):
        type_expr = self.visit(ast.expr, table)[0]
        while table.currentmethod is None:
            table = table.next
        method_name = table.currentmethod
        table = table.next
        for method in table.symbols:
            if method.name == method_name and not self.compareType(method.stype.returnType, type_expr):
                raise TypeMismatchInStatement(ast)
    def visitCallStmt(self, ast: CallStmt, table: SymbolTable):
        type_obj = None
        kind = str(Instance())
        if isinstance(ast.obj, Id):
            try:
                type_obj = self.visit(ast.obj, table)[0]
                kind = str(Instance())
            except Undeclared:
                if ast.obj.name not in self.classes:
                    raise Undeclared(Identifier(), ast.obj.name)
                type_obj = str(ClassType(Id(ast.obj.name)))
                kind = str(Static())
        else:
            type_obj = self.visit(ast.obj, table)[0]
        class_name = StaticChecker.getNameFromClassTypeName(type_obj)
        if class_name is None:
            raise TypeMismatchInStatement(ast)
        method_name = ast.method.name
        type_param = list(map(lambda x: self.visit(x, table)[0], ast.param))
        method_symbol = None
        while method_symbol is None and class_name is not None:
            class_table: SymbolTable = self.classes.get(
                class_name).get('table')
            for sym in class_table.symbols:
                if sym.name == method_name and sym.kind == str(Method()):
                    method_symbol = sym
            class_name = self.classes.get(class_name).get('parentname')
        if method_symbol is None:
            raise Undeclared(Method(), method_name)
        method_param = method_symbol.stype.paramType
        if len(type_param) != len(method_param):
            raise TypeMismatchInStatement(ast)
        for i in range(len(type_param)):
            if False == self.compareType(method_param[i], type_param[i]):
                raise TypeMismatchInStatement(ast)
        if method_symbol.stype.returnType != str(VoidType()):
            raise TypeMismatchInStatement(ast)
        if method_symbol.stype.kind != kind:
            raise IllegalMemberAccess(CallExpr(ast.obj, ast.method, ast.param))
    def visitId(self, ast: Id, table: SymbolTable):
        if table.next is None:
            for x in table.symbols:
                if x.name == ast.name:
                    return x.stype.returnType, x.stype.is_const
        while table.next is not None:
            for x in table.symbols:
                if x.name == ast.name:
                    return x.stype.returnType, x.stype.is_const
            table = table.next
        raise Undeclared(Identifier(), ast.name)
    def visitArrayCell(self, ast: ArrayCell, table: SymbolTable):
        arr_type, is_array_const = self.visit(ast.arr, table)
        idx_type, _ = self.visit(ast.idx, table)
        if arr_type[:9] != "ArrayType" or idx_type != str(IntType()):
            raise TypeMismatchInExpression(ast)
        return arr_type.split(',')[1][:-1], is_array_const
    def visitFieldAccess(self, ast: FieldAccess, table: SymbolTable):
        type_obj = None
        kind = str(Instance())
        if isinstance(ast.obj, Id):
            try:
                type_obj = self.visit(ast.obj, table)[0]
            except Undeclared:
                if ast.obj.name not in self.classes:
                    raise Undeclared(Identifier(), ast.obj.name)
                type_obj = str(ClassType(Id(ast.obj.name)))
                kind = str(Static())
        else:
            type_obj = self.visit(ast.obj, table)[0]
        class_name = StaticChecker.getNameFromClassTypeName(type_obj)
        if class_name is None:
            raise TypeMismatchInExpression(ast)
        fieldname = ast.fieldname.name
        field_symbol = None
        while field_symbol is None and class_name is not None:
            class_table: SymbolTable = self.classes.get(class_name).get('table')
            for sym in class_table.symbols:
                if sym.name == fieldname and sym.kind == str(Attribute()):
                    field_symbol = sym
                    if sym.kind != str(Attribute()):
                        TypeMismatchInExpression(ast)
            class_name = self.classes.get(class_name).get('parentname')
        if field_symbol is None:
            raise Undeclared(Attribute(), fieldname)
        if field_symbol.stype.returnType == str(VoidType()):
            raise TypeMismatchInExpression(ast)
        if field_symbol.stype.kind != kind:
            raise IllegalMemberAccess(ast)
        return field_symbol.stype.returnType, field_symbol.stype.is_const
    def visitBinaryOp(self, ast: BinaryOp, table: SymbolTable):
        op = ast.op
        type_left, is_left_const = self.visit(ast.left, table)
        type_right, is_right_const = self.visit(ast.right, table)
        if op in ['%', '\\']:
            if type_left == type_right == str(IntType()):
                return type_left, is_left_const and is_right_const
        elif op in ['/']:
            if type_left in [str(IntType()), str(FloatType())] and type_right in [str(IntType()), str(FloatType())]:
                return str(FloatType()), is_left_const and is_right_const
        elif op in ['+', '-', '*']:
            if type_left == type_right == str(IntType()):
                return type_left, is_left_const and is_right_const
            elif type_left in [str(IntType()), str(FloatType())] and type_right in [str(IntType()), str(FloatType())]:
                return str(FloatType()), is_left_const and is_right_const
        elif op in ['&&', '||']:
            if type_left == type_right == str(BoolType()):
                return type_left, is_left_const and is_right_const
        elif op in ['==', '!=']:
            if type_left == type_right == str(IntType()) or type_left == type_right == str(BoolType()):
                return str(BoolType()), is_left_const and is_right_const
        elif op in ['>', '<', '<=', '>=']:
            if type_left in [str(IntType()),str(FloatType())] and type_right in [str(IntType()),str(FloatType())]:
                return str(BoolType()) , is_left_const and is_right_const
        elif op in ['^']:
            if type_left == type_right == str(StringType()):
                return str(StringType()), is_left_const and is_right_const
        raise TypeMismatchInExpression(ast)
    def visitUnaryOp(self, ast: UnaryOp, table: SymbolTable):
        op = ast.op
        type_body, is_body_const = self.visit(ast.body, table)
        if op in ['+', '-']:
            if type_body not in [str(IntType()), str(FloatType())]:
                raise TypeMismatchInExpression(ast)
        elif op in ['!']:
            if type_body != str(BoolType()):
                raise TypeMismatchInExpression(ast)
        return type_body,is_body_const
    def visitCallExpr(self, ast: CallExpr, table: SymbolTable):
        type_obj = None
        kind = str(Instance())
        if isinstance(ast.obj, Id):
            try:
                type_obj = self.visit(ast.obj, table)[0]
                kind = str(Instance())
            except Undeclared:
                if ast.obj.name not in self.classes:
                    raise Undeclared(Identifier(), ast.obj.name)
                type_obj = str(ClassType(Id(ast.obj.name)))
                kind = str(Static())
        else:
            type_obj = self.visit(ast.obj, table)[0]
        class_name = StaticChecker.getNameFromClassTypeName(type_obj)
        if class_name is None:
            raise TypeMismatchInExpression(ast)
        method_name = ast.method.name
        type_param = list(map(lambda x: self.visit(x, table)[0], ast.param))
        method_symbol = None
        while method_symbol is None and class_name is not None:
            class_table: SymbolTable = self.classes.get(
                class_name).get('table')
            for sym in class_table.symbols:
                if sym.name == method_name:
                    method_symbol = sym
                    if sym.kind != str(Method()):
                        raise TypeMismatchInExpression(ast)
            class_name = self.classes.get(class_name).get('parentname')
        if method_symbol is None:
            raise Undeclared(Method(), method_name)
        method_param = method_symbol.stype.paramType
        if len(type_param) != len(method_param):
            raise TypeMismatchInExpression(ast)
        for i in range(len(type_param)):
            if False == self.compareType(method_param[i], type_param[i]):
                raise TypeMismatchInExpression(ast)
        if method_symbol.stype.returnType == str(VoidType()):
            raise TypeMismatchInExpression(ast)
        if method_symbol.stype.kind != kind:
            raise IllegalMemberAccess(ast)
        return method_symbol.stype.returnType,False
    def visitNewExpr(self, ast: NewExpr, table: SymbolTable):
        classname = ast.classname.name
        if classname not in self.classes:
            raise Undeclared(Class(), classname)
        table = self.classes.get(classname).get('table')
        type_param = list(map(lambda x: self.visit(x, table), ast.param))
        for sym in table.symbols:
            if sym.name == "<init>":
                method_symbol = sym
        params = method_symbol.stype.paramType
        if type_param != params:
            raise TypeMismatchInExpression(ast)
        return str(ClassType(ast.classname)),False
    def visitIntLiteral(self, ast: IntLiteral, table: SymbolTable):
        return str(IntType()),True
    def visitFloatLiteral(self, ast: FloatLiteral, table: SymbolTable):
        return str(FloatType()),True
    def visitStringLiteral(self, ast: StringLiteral, table: SymbolTable):
        return str(StringType()),True
    def visitBooleanLiteral(self, ast: BooleanLiteral, table: SymbolTable):
        return str(BoolType()),True
    def visitNullLiteral(self, ast: NullLiteral, table: SymbolTable):
        return str(NullLiteral()),True
    def visitSelfLiteral(self, ast: SelfLiteral, table: SymbolTable):
        while table.next is not None:
            table = table.next
        return str(ClassType(Id(table.currentclass))),False
    def visitArrayLiteral(self, ast: ArrayLiteral, table: SymbolTable):
        list_array_type = list(map(lambda x: self.visit(x, table), ast.value))
        if len(list_array_type) > 1:
            for i in range(1, len(list_array_type)):
                if list_array_type[i-1][0] != list_array_type[i][0]:
                    raise IllegalArrayLiteral(ast)
        return str(ArrayType(len(list_array_type), list_array_type[0][0] if len(list_array_type) > 0 else None)),reduce(lambda acc,ele: ele[1] and acc, list_array_type, True)
    def compareType(self, lhs, rhs):
        if lhs == rhs:
            return True
        if lhs == str(IntType()):
            return rhs == str(IntType())
        if lhs == str(FloatType()):
            return rhs == str(FloatType()) or rhs == str(IntType())
        if lhs == str(BoolType()):
            return rhs == str(BoolType())
        if lhs[:9] == "ArrayType" and lhs[10] == rhs[10]:
            lhs_ele_type = lhs[10:-1].split(',')[1]
            rhs_ele_type = rhs[10:-1].split(',')[1]
            return self.compareType(lhs_ele_type, rhs_ele_type)
        lhs_class = StaticChecker.getNameFromClassTypeName(lhs)
        rhs_class = StaticChecker.getNameFromClassTypeName(rhs)
        if lhs_class is None or rhs_class is None:
            return False
        else:
            rhs_parentclass = self.classes.get(rhs_class).get('parentname')
            while rhs_parentclass is not None:
                if rhs_parentclass == lhs_class:
                    return True
                rhs_parentclass = self.classes.get(rhs_parentclass).get('parentname')
        return False
    def is_valid_class_type(self, type):
        if isinstance(type, ClassType):
            return type.classname.name in self.classes
        return True
    @staticmethod
    def checkIsConstant(lhs, table: SymbolTable):
        if isinstance(lhs, Id):
            while table.next is not None:
                for sym in table.symbols:
                    if sym.name == lhs.name:
                        return sym.stype.is_const
                table = table.next
        if isinstance(lhs, FieldAccess):
            while table.next is not None:
                table = table.next
            for sym in table.symbols:
                if sym.name == lhs.fieldname.name:
                    return sym.stype.is_const
        if isinstance(lhs, ArrayCell):
            pass
        return False
    @staticmethod
    def getNameFromClassTypeName(classtypename):
        if "ClassType" != classtypename[:9]:
            return None
        else:
            return classtypename[13:-2]

class GlobalEnvironment(BaseVisitor):
    def visitProgram(self, ast: Program, o):
        self.classes = { }
        for decl in ast.decl:
            class_name = decl.classname.name
            if class_name in self.classes:
                raise Redeclared(Class(), class_name)
            self.classes[class_name] = { }
        for decl in ast.decl:
            class_name = decl.classname.name
            parent_name = decl.parentname.name if decl.parentname is not None else None
            if parent_name not in self.classes and parent_name is not None:
                raise Undeclared(Class(), parent_name)
            self.classes[class_name]['parentname'] = parent_name
        [self.visit(x, self.classes) for x in ast.decl]
        return self.classes
    def visitClassDecl(self, ast: ClassDecl, o):
        new_table = SymbolTable([])
        o[ast.classname.name]['table'] = new_table
        lst_name = [self.visit(x, new_table) for x in ast.memlist]
        if "<init>" not in map(lambda x: x, lst_name):
            init_method = Symbol("<init>",str(Method()),MethodType(str(Instance()),[],VoidType()))
            new_table.symbols.append(init_method)
    def visitMethodDecl(self, ast: MethodDecl, table: SymbolTable):
        kind = str(ast.kind)
        name = ast.name.name
        param_type = list(map(lambda x: str(x.varType), ast.param))
        return_type = str(ast.returnType)
        if name in map(lambda x: x.name, table.symbols):
            raise Redeclared(Method(), name)
        method_symbol = Symbol(name, str(Method()), MethodType(
            kind, param_type, return_type))
        table.symbols.append(method_symbol)
        return name
    def visitAttributeDecl(self, ast: AttributeDecl, table: SymbolTable):
        kind = str(ast.kind)
        name, type, is_const = self.visit(ast.decl, table)
        if name == "<init>":
            raise Redeclared(Attribute(), name)
        table.symbols.append(
            Symbol(name, str(Attribute()), AttrType(type, kind, is_const)))
        return name
    def visitVarDecl(self, ast: VarDecl, table: SymbolTable):
        name = ast.variable.name
        type = str(ast.varType)
        is_const = False
        if name in map(lambda x: x.name, table.symbols):
            raise Redeclared(Attribute(), name)
        return name, type, is_const
    def visitConstDecl(self, ast: ConstDecl, table: SymbolTable):
        name = ast.constant.name
        type = str(ast.constType)
        is_const = True
        if name in map(lambda x: x.name, table.symbols):
            raise Redeclared(Attribute(), name)
        return name, type, is_const

"""
    global_env = {
        'io': {
            'methods': {
                'readInt': {
                    'kind': 'Static',
                    'returnType': 'IntType'
                },
                'writeInt': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'IntType'
                        }
                    }
                },
                'writeIntLn': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'IntType'
                        }
                    }
                },
                'readFloat': {
                    'kind': 'Static',
                    'returnType': 'FloatType'
                },
                'writeFloat': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'FloatType'
                        }
                    }
                },
                'writeFloatLn': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'FloatType'
                        }
                    }
                },
                'readBool': {
                    'kind': 'Static',
                    'returnType': 'BoolType'
                },
                'writeBool': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'BoolType'
                        }
                    }
                },
                'writeBoolLn': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'BoolType'
                        }
                    }
                },
                'readStr': {
                    'kind': 'Static',
                    'returnType': 'StringType'
                },
                'writeStr': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'StringType'
                        }
                    }
                },
                'writeStrLn': {
                    'kind': 'Static',
                    'returnType': 'Void',
                    'params': {
                        'anArg': {
                            'type': 'StringType'
                        }
                    }
                },
            }
        }
    }
"""