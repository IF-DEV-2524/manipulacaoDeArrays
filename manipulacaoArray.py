lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

lista_produtos[lista_produtos.index('batons')],lista_produtos[lista_produtos.index('loções')] = 'rímel','cremes hidratantes'

lista_produtos.pop()

lista_produtos.append('shampoo')

lista_produtos.append('creme facial')
print(lista_produtos)