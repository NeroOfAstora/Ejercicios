# JALORA

name = 'Hola_buenas_tardes'
f = open("/home/usuario/p.txt")
linea = f.readlines()
f.close()

for i in linea:
    #print(i)
    var2=i.replace(' ', '->')
    print(var2)