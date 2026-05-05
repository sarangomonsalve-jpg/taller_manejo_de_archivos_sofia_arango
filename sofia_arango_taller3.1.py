# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:04:40 2026

@author: sarango
"""
import os

dir_patients = "patients"
dir_his = "his"

if not os.path.exists(dir_patients):
    os.makedirs(dir_patients)

if not os.path.exists(dir_his):
    os.makedirs(dir_his)

def generar_hce():
    archivo_salida = os.path.join(dir_his, "hce.txt")
    try:
        hce = open(archivo_salida, "w")
        hce.write("Id| Nombre Apellido | Edad | Género| FechaNacimiento| EPS\n")
        
        archivos = os.listdir(dir_patients)
        
        for nombre_archivo in archivos:
            if nombre_archivo.endswith(".txt"):
                ruta_archivo = os.path.join(dir_patients, nombre_archivo)
                
                archivo = open(ruta_archivo, "r")
                lineas = archivo.readlines()
                archivo.close()
                
                id_val = ""
                nombre = ""
                apellido = ""
                edad = ""
                genero = ""
                fecha = ""
                eps = ""
                
                for linea in lineas:
                    linea = linea.strip()
                    if ":" in linea:
                        clave, valor = linea.split(":", 1)
                        clave = clave.strip()
                        valor = valor.strip()
                        
                        if clave == "Id":
                            id_val = valor
                        elif clave == "Nombre":
                            nombre = valor
                        elif clave == "Apellido":
                            apellido = valor
                        elif clave == "Edad":
                            edad = valor
                        elif clave in ["Genero", "Género"]:
                            genero = valor
                        elif clave in ["FechaNacimiento", "Fecha de Nacimiento"]:
                            fecha = valor
                        elif clave == "EPS":
                            eps = valor
                            
                hce.write(f"{id_val}| {nombre} {apellido} | {edad} | {genero}| {fecha}| {eps}\n")
                
        hce.close()
    except Exception as e:
        print(f"Error al generar el archivo HCE: {e}")


menu = 0

while menu != 3:
    print("\nMENÚ PRINCIPAL")
    print("1. Ingresar información de paciente")
    print("2. Ver carpeta")
    print("3. Salir")
    
    try:
        menu = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if menu == 1:
        print("\n--- REGISTRO DE PACIENTE ---")
        id_val = input("Id: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        genero = input("Género: ")
        fecha = input("Fecha de Nacimiento (ej. DD-MM-AAAA): ")
        eps = input("EPS: ")

        nombre_archivo = f"paciente_{id_val}.txt"
        ruta_archivo = os.path.join(dir_patients, nombre_archivo)

        with open(ruta_archivo, "w") as archivo:
            archivo.write(f"Id: {id_val}\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Apellido: {apellido}\n")
            archivo.write(f"Edad: {edad}\n")
            archivo.write(f"Genero: {genero}\n")
            archivo.write(f"FechaNacimiento: {fecha}\n")
            archivo.write(f"EPS: {eps}\n")

        print(f"Paciente registrado correctamente en '{ruta_archivo}'.")

        generar_hce()
        print("Archivo hce.txt actualizado automáticamente en la carpeta 'his'.")

    elif menu == 2:
        print("\nCONTENIDO DE LAS CARPETAS ")

        print("-> Archivos en la carpeta 'patients':")
        if os.path.exists(dir_patients):
            archivos_patients = os.listdir(dir_patients)
            if len(archivos_patients) > 0:
                for arch in archivos_patients:
                    print(f"   - {arch}")
            else:
                print("   (La carpeta 'patients' está vacía)")

        print("\n Archivos en la carpeta 'his':")
        archivo_salida = os.path.join(dir_his, "hce.txt")
        if os.path.exists(archivo_salida):
            archivos_his = os.listdir(dir_his)
            for arch in archivos_his:
                print(f"   - {arch}")
            
            print("\n  Contenido de hce.txt")
            archivo = open(archivo_salida, "r")
            contenido = archivo.read()
            archivo.close()
            print(contenido)
        else:
            print("   (La carpeta 'his' no tiene un archivo hce.txt aún)")

    elif menu == 3:
        print("Saliendo del programa. ¡Hasta luego!")
