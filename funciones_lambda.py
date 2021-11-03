from funciones_primer_nivel import SumaTodos

doble = lambda x: x*2 #lambda se usa para funciones anonimas

triple = lambda x: x*3

print(SumaTodos(3, doble))

print(SumaTodos(100, triple))