student1 = ["Sofia Pelaez", 22, 43275760, 4.7]
student2 = ["Camilo Sanchez", 24, 72428092, 3.2]
student3 = ["Camila Castrillon", 22, 54132128, 4.0]
student4 = ["Daniel Labrador", 30, 1001418072, 5.0]
student5 = ["Juan Esteban Grisales", 28, 244718042, 3.9]

olddatabase = student1, student2, student3, student4, student5
newdatabase = []

continuar = True

print("=======> Bienvenido, Director. Que deseas hacer hoy? <=======")

while continuar:
        menu = int(input("=======> MENU PRINCIPAL <======= \n1. Agregar Estudiantes \n2. Buscar Estudiante \n3. Actualizar Informacion Estudiante \n4. Eliminar Estudiante \n5. Calcular Promedios \n6. Listar Estudiantes  "))
        break
# /////////////////  ADD A NEW STUDENT //////////// #

def add_new_student():
    continuar = True

    while continuar:
            while True:
                if menu == 1:
                    print("=======> AGREGAR ESTUDIANTE <=======")
                    name = str(input("Ingrese el nombre completo: "))
                    age = int(input("Ingrese la edad: "))
                    id = int(input("Ingrese el ID: "))
                    score = float(input("Ingrese la calificacion: "))
                    continuar = False
                    break
    
            while True:
                validate = input("Desea agregar mas estudiantes? SI(Y) / NO(N) ")
                if validate == "No" or validate == "no" :
                    continuar = False
                    break
                elif validate == "Si" or validate == "si":
                    continuar = True
                    break
                else:
                    print("Por favor responda Si o No")

            newdatabase.append([name, age, id, score])

    print("=======> ESTOS SON LOS ESTUDIANTES EN EL REGISTRO <=======")
    for idx, p in enumerate(olddatabase, 1):
        print(f"{idx}. {p}")
    for idx, p in enumerate(newdatabase, 6):
        print(f"{idx}. {p}")

        retornar = int(input("Que deseas hacer? \n1. Menu principal \n2. Salir \n"))
        if retornar == 2:
            continuar = False
            break
        elif retornar == 1:
            print(menu)
            break
        else:
            print("Solo se permite opcion 1 o 2 \n")

add_new_student()

# /////////////////  SEARCH A STUDENT //////////// #

# def search_student():
#      continuar = True

#      while continuar:
#             while True:
#                 if menu == 2:
#                     print("=======> INGRESE EL ID DEL ESTUDIANTE <=======")
#                     int(input(""))
#                     break

# search_student()