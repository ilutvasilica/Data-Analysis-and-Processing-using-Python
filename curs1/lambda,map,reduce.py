culori =('alb','rosu','negru','verde')

def lungime_5(cuvant):
    return len(cuvant)== 5 


print(list(filter (lungime_5,culori)))

print(list(filter(lambda cuvant: len(cuvant)== 5 ,culori)))
 
#map -transformare,am facu x+x si am aplicat inca o valoare 

print(list(map(lambda x: x+ ' '+ x,culori)))

#reduce 

from functools import reduce 

culori =('alb','rosu','negru','verde')

print(reduce(lambda x, y: x if len(x) < len(y) else y,culori))


lista = [10, 2, 30, 50, 300, 10]

#lista care are valori mai mari decat 5

print(list(filter(lambda x :  x  > 5,lista)))

print(list(element for element in lista if element > 5))

vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"
y =''

print(''.join(filter(lambda x : x if x not in vocale else y,input_string)))

#daca pui join in fata si cu un caracter in fatala join se printeaza cu caracterul intrele ele.

#my_list = ["1", "2", "3", "4"]

#my_list = list(range(1,5))
#print(my_list)

my_list = list(map(str,range(1,50)))
print(my_list)

my_list = list(map(lambda x :x,range(1,5)))
print(my_list)


lista = [10, 2, 30, 50, 300, 10]
#trebuie sa returnam media acestora sum(lista)/len(lista)
#asta este suma sum(lista )
#cel ,mai usor 
print(sum(lista)/len(lista))

my_lista = reduce(lambda x ,y : x+y,lista)/len(lista)
print(my_lista)