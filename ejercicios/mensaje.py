# -*- coding: utf-8 -*-

#Ejecutar este programa desde spyder, o desde una consola
#
#Ejercicio:
#Escribe un programa tal que: El programa pregunta nombre, y mensaje. 
#
#El programa imprime en la terminal:
#
#    "El mensaje de <nombre> tiene <n> caracteres", 
#
#    donde <nombre> se refiere al nombre que se escribe y <n> es el número de caracteres que tiene el mensaje.

nombre = raw_input('Nombre: ')
mensaje = raw_input('Mensaje: ')
n = len(mensaje)

#Hay dos formas de escribir el programa. La primera manera aparece a
#continuacion comentada:

#print 'El mensaje de ' + nombre + ' tiene ' + str(n) + ' caracteres.'

#Observa que en la linea anterior, es necesario escribir `str(n)`, pues n es 
#una variable de tipo entero, y no se *concatenara* sin convertirla en texto
#con el comando `str`.
#La segunda manera de imprimir, mas elegante, es utilizando una plantilla:

print 'El mensaje de {0} tiene {1} caracteres.'.format(nombre, n)


#Puedes leer mas acerca de las plantillas aqui: 
#https://docs.python.org/2/library/string.html#format-examples
