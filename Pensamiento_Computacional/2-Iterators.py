
frutas = ['manzana', 'pera', 'mango']

iterador = iter(frutas)
print(iterador)

print(next(iterador))
print(next(iterador))
print(next(iterador))
# Llama un error de tipo StopIteration
# por que ya no existen
print(next(iterador)) 