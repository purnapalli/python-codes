def outer():
	print("Outer function execution starts ")
	def inner():
		print("Inner function executing ")
	print("Outer function execution done ")
	return inner
f1=outer()
print()
f1()
print()
outer()
print(type(f1))
print(id(f1))