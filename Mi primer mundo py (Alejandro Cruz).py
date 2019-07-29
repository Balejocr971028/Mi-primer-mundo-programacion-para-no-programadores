'''Descripcion:El objetivo de este mapa, es demostrar como han avanzado
nuestros conocimientos en esta aplicacion demostrando distintos tipos de objetos y
modificaciones en el mundo'''
print("Hola soy reeborg´s")
print("voy a hacer una mision") 
repeat 4 :
    move()
#pause()
put("banana")
#pause()
take("apple")
#pause()
repeat 2 :
    turn_left()
#pause()
repeat 4 :
    move()
#pause()
print("Hecho por mi amo Alejandro Cruz")
    
'''Alejandro Cruz'''    
    
    
      
  

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
put()
while front_is_clear() :
    move()