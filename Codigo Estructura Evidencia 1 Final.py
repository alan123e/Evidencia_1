import random
import datetime

("*"*30)
print("*"*9 + " BIENVENIDO " + "*"*9)

while True:
    print("1. Registrar una reserva")
    print("2. Editar un evento ya existente")
    print("3. Consulta tus reservas")
    print("4. Registrate como nuevo cliente")
    print("5. Registra una sala")
    print("6. Salir")
    opcion = int(input("Seleccione el numero de la accion que quiere realizar \n:"))

    if opcion == 1:
        print('******** REGISTRO PARA RESERVACION DE UNA SALA ********')
        nombre_evento = input('Ingrese el nombre de su evento: ')
        fecha_reservada = input("Ingrese la fecha de su evento (dd/mm/aaaa): ")
        fecha_reservada = datetime.datetime.strptime(fecha_reservada,"%d/%m/%Y").date()

        dia_reservado = fecha_reservada.day
        mes_reservado = fecha_reservada.month
        año_reservado = fecha_reservada.year

        fecha_actual = datetime.date.today()
        dia_actual = fecha_actual.day
        mes_actual = fecha_actual.month
        año_actual = fecha_actual.year

        dia_valido = dia_reservado - dia_actual

        tupla_reservacion = (mes_reservado, dia_reservado, año_reservado)
        tupla_actual = (mes_actual, dia_actual, año_actual)

        if dia_valido <= 1:
            print("Para reservar una fecha debe hacerlo con 2 dias de anticipación")
        else:
            if tupla_reservacion > tupla_actual:
                print("Su reservación a sido éxitosa")
            else:
                print("Para reservar una fecha debe hacerlo con 2 dias de anticipación")

    elif opcion == 2:
        print("2")
        Evento = {"SEGA":"Gamescom 2022", "Nintendo":"Nintendo Direct Mini","XBOX":"Xbox game fest"}
        Evento = { **Evento, 'Nintendo': "Smash Direct"}
        print(Evento)

    elif opcion == 3:
        print("3")
        print("********Consulta de reservaciones********")
        diccionario_citas = {"Alan Javier Gutierrez Garay":"12/05/2022","George Kusunoki Miller":"13/06/2023","Gustavo Adrián Cerati":"17/10/2024"}

        print(list(diccionario_citas.items()))

    elif opcion == 4:
        print("4")
        print("******** Registro de un nuevo cliente ********")
        Clave_cliente= print(f"Primero tenemos que crear su clave la cual sera:) {random.randint(1000,9999)}")
        nombre_cliente= input('Ingresa su nombre: ')
        Registro_Cliente = (Clave_cliente, nombre_cliente)
        print("Este esta es su clave y su nombre registrados")

    elif opcion == 5:
        print("5")
        print("'********Registro de una sala ********'")
        Clave_Sala = print(f"Primero tenemos que crear su clave de la sala la cual sera: {random.randint(1000,9999)}")
        nombre_cliente = input ('Ingrese el nombre del cliente: ')
        Cupo_Sala = input('Ingrese el nombre de la sala:')
        Registro_Sala = (Clave_Sala, Cupo_Sala)
        print(Registro_Sala)
        print("Estos son los datos del registro para la sala")


        print(6)
    elif opcion == 6:
        print("Fin")
        break

    #else:
    #   print("Ingresa un numero valido")