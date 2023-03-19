amperios = int(input("¿Cuántos Amperios consumen sus electrodomésticos? "))
voltaje = int(input("¿Qué voltaje nominal tiene en su domicilio? "))
watios =  (voltaje * amperios)
print ("La potencia que debe contratar con su empresa suministradora es {} watios".format (watios))
