<!-- 
.. description: Python'da debug işlerini kolaylaştıracak bir decorator
.. date: 2013/10/26 02:37
.. title: Debugging Decorator
.. slug: debugging-decorator
-->

Kod yazarken ve bu kodun tam olarak ne yaptığını anlamazken, fonksiyonların içine ara ara
print serpiştiriyordum ki, neler döndüğünü görebileyim. Ancak malumunuz, bu printleri
teker teker yazması, sonra teker teker silmesi bir hayli zahmetli bir işe dönüşebiliyor.
Bu problemin üstesinden gelmek için, aşağıdaki decorator'u yazdım. İndirmek isteyenler [debugging.py](https://gist.github.com/yasar11732/7163528/raw/3aac84a23fd57d3c4ee28d627c7607d68c3ac24b/debugging.py) adresinden indirebilir.<!-- TEASER_END -->

	:::python
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

		# print ast.dump(func_ast)
		
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
		# if you don't do this, compile&exec will call this function recursively.
		func_ast.decorator_list = []
		# func_ast = ast.fix_missing_locations(func_ast)
		# print "trying to compile this function:", ast.dump(func_ast)
		modul_ast = ast.fix_missing_locations(ast.Module(body=[func_ast]))
		exec compile(modul_ast,'<string>','exec')
		return locals()[func.func_name]
		
Kullanımı çok basit. Örneğin şu kodu inceleyelim:

	:::python
	@debugging
	def osman(ali, veli, mehmet, zeynep = 48):
		ali = 129
		return ali + veli

	print osman(12,24,32)
	
Bu kod şöyle bir çıktı veriyor:
<pre>
function osman called
mehmet 32
zeynep 48
veli 24
ali 12
assigned new value to ali: 129
returning 153
153
</pre>

Gördüğünüz üzere, önce çalışan fonksiyonun ismini yazıyor. Daha sonra local değişkenleri gösteriyor. Her atama yapıldığında, bunu da belirtiyor. Son olarak, return olacağı zaman, neyin return olduğunu
da gösteriyor. Fonksiyonu debug ettikten sonra da, `@debugging` decorator'unu kaldırarak bu çıktıyı durdurabilirsiniz.

## Nasıl çalışıyor peki bu?

Eğer decorator'lerle ilgili temel bilgileriniz yoksa, [Decorator nedir](/python/decorator.html) yazısını okuyarak başlayabilirsiniz.

Bu decorator'de, hedef fonksiyonun `ast` modülündeki fonksiyonları kullanarak syntax tree'sini oluşturdum. Syntax tree
üzerinde gezinip, gerekli gördüğüm yerlere print ifadeleri ekleyip, tekrar derledim.

Sizce bu decorator iş görür mü? Daha nasıl geliştirebilirim?