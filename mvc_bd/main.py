from controlador.personaControl import personaControl

lista=["Valeria","flores","62456795","m","12584","43"]
enlace=personaControl()
enlace.crearRegistro(lista)

listaDeRegistro = enlace.leerRegistro()

for i in range(len(listaDeRegistro)):
    print("Codigo: ",listaDeRegistro[i][0])
    print("Nombre: ",listaDeRegistro[i][1])
    print("Apellidos: ",listaDeRegistro[i][2])
    print("Dni: ",listaDeRegistro[i][3])
    print("Sexo: ",listaDeRegistro[i][4])
    print("Ciclo: ",listaDeRegistro[i][5])
    print("###############################")