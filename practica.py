from cliente import Cliente

print('Práctica de Collections')
#crear una lista de frutas
frutas=['melón','manzana','plátano','mandarina','granada','kiwi','pera','manzana','fresas','cerezas','piña']
#muestra las frutas ordenadas por orden alfabético
frutas.sort()
for fruta in frutas:
    print(fruta)
#añade a las frutas, macedonia
frutas.append('macedonia')

#tengo un error. Porque hay que poner precios a las frutas. Con decimales.
#Crea un dict nuevo con las frutas y los precios

frutas_dict={'melón':9.95,'manzana':5,'plátano':4.55,'mandarina':3.99,'granada':12,'kiwi':4.33,'pera':2.45,'manzana':2.35,'fresas':3.60,'cerezas':4.65,'piña':5}
#mostrar el precio medio

total=0 #totalizador
for precio in frutas_dict.values():
    #total=total+precio
    total+=precio
    print(precio)
print(f'el total es {total}')
print(f'el total es {total/len(frutas_dict)}')

#guardar 4 países del mundo. No ses necesario añadir más países. Pero los quiero ordenar alfabéticamente
#lista : elegido. Es mutable y puede añadir. Pues vale. Necesito sort
#tupla
#set : no sirve, porque no permite ordenar
#dict : descartado porque no pedimos key value

paises=['Alemania','España','Brasil','Argentina']
for pais in paises:
    print(pais.lower())

#3 alumnos con sus notas: con decimales
#muestra únicamente los alumnos cuya nota es superior o igual a 5

alumnos={'Julián':4.35,'Rosa':7.85,'Marcos':6.50}
for alumno in alumnos.items():
    if alumno[1]>=5:
        print(alumno[0])

#listado de clientes. 3 clientes : nombre, ciudad, facturacion
#POO
#string, int, float, boolean...
#usamos objetos: cliente es un objeto definido por nosotros
#crear clase Cliente (POO)

cliente1=Cliente('Julián','Madrid',1500) #instanciar un objeto
cliente2=Cliente('Rosa','Sevilla',2000)
cliente3=Cliente('Marcos','Caceres',3000)

clientes=[cliente1,cliente2,cliente3]
for cliente in clientes:
    print(cliente.nombre)


