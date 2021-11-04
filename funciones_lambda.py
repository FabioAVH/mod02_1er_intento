from funciones_primer_nivel import SumaTodos

doble = lambda x: x*2 #lambda se usa para funciones anonimas. Variable : codigo

triple = lambda x: x*3

print(SumaTodos(3, doble))

print(SumaTodos(100, triple))

'''
Lo ideal seria:
print(SumaTodos(3, lambda x: x*2))
print(SumaTodos(100, lambda x: x*3))