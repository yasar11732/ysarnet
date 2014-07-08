# -*- coding: cp1254 -*-
import inspect
import ast

def make_print_node(s):
    return ast.Print(dest=None, values=[ast.Str(s=s)], nl=True)

def make_print_with_percent_formatting(s, *args):
    if not args:
        return make_print_node(s)

    printnode = ast.Print(dest=None, nl=True)
    binop = ast.BinOp(left=ast.Str(s=s), op=ast.Mod())
    if len(args) == 1:
        binop.right = ast.Name(id = args[0], ctx=ast.Load())
    else:
        name_list = []
        for arg in args:
            name_list.append(ast.Name(id=arg, ctx=ast.Load()))
        binop.right = ast.Tuple(elts=name_list)

    printnode.values = [binop]
    return printnode

def debugging(func):
    tree = ast.parse(inspect.getsource(func))
    func_ast = None
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == func.func_name:
            func_ast = n
            break
    if not func_ast:
        return func

    
    new_function_body = []
    # print called function's name
    new_function_body.append(make_print_node("function %s called" % func.func_name))

    # print function's locals
    mystr ="""for k, v in locals().items():
    print k,v
    """
    for_loop = ast.parse(mystr).body[0]
    new_function_body.append(for_loop)

    for node in func_ast.body:
        if isinstance(node, ast.Return):
            """
            convert:
                return expr
            to:
                __return_value__ = expr
                print "returning %s" % __return_value__
                return __return_value__
            """

            new_function_body.append(ast.Assign(targets=[ast.Name(id='__return_value__', ctx=ast.Store())], value=node.value))
            new_function_body.append(make_print_with_percent_formatting('returning %s', '__return_value__'))
            new_function_body.append(ast.Return(value=ast.Name(id='__return_value__', ctx=ast.Load())))

        elif isinstance(node, ast.Assign):
            """
            convert:
                a = expr
            to:
                a = expr
                print "assigned new value to a, %r" % a
            """
            new_function_body.append(node)
            for target in node.targets:
                new_function_body.append(node)
                new_function_body.append(make_print_with_percent_formatting('assigned new value to ' + target.id + ': %r', target.id))

        else:
            new_function_body.append(node)




    func_ast.body = new_function_body
    # if you don't do this, compile compile&exec will call this function recursively.
    func_ast.decorator_list = []
    # print ast.dump(func_ast)
    # func_ast = ast.fix_missing_locations(func_ast)
    # print "trying to compile this function:", ast.dump(func_ast)
    modul_ast = ast.fix_missing_locations(ast.Module(body=[func_ast]))
    exec compile(modul_ast,'<string>','exec')
    return locals()[func.func_name]

