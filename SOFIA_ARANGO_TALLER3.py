# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
menu = 1
contador = 1

while menu != 3:
    print("\n1. Ingresar información de paciente")
    print("2. Ver información en archivo")
    print("3. Salir")
    menu = int(input("Seleccione una opción: "))

    if menu == 1:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        archivo = open("salida.txt", "a")
        archivo.write(str(contador) + "|" + nombre + "|" + apellido + "|" + edad + "|\n")
        archivo.close()
        contador = contador + 1
        print("Paciente guardado.")

    elif menu == 2:
        archivo = open("salida.txt", "r")
        contenido = archivo.read()
        archivo.close()
        print(contenido)

    elif menu == 3:
        print("Salio de la aplicación")

    else:
        print("Opción no válida.")
