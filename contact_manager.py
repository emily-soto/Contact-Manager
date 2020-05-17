### Emily Soto y Madeline Salguero
import csv
import requests
import validators
import time, string
import emoji
from os import system, name 



##Variables globales
def nombre_apellido(s):
  return len(s.split()) > 1

def orden_alfabetico(unsorted_dict):  
    sorted_keys = sorted(unsorted_dict.keys(), key=lambda x:x.lower())
    sorted_dict= {}
    for key in sorted_keys:
        sorted_dict.update({key: unsorted_dict[key]})
    return sorted_dict
###Clearscreen
def clear(): 
    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 

clear()
r = requests.get('http://demo7130536.mockable.io/final-contacts-100')
contacts=(r.json())

exit = False

def crearContacto():
    nombre_init = (input("Ingrese nombre del nuevo contacto\n"))
    nombre=nombre_init.title()
    if (nombre_apellido(nombre) == True):
        numero = (input("Ingrese el telefono:\n"))
        if (numero.isdigit()==True):
            mail = (input("Ingrese la email address:\n"))
            if validators.email(mail):
                empresa = input("Ingrese la empresa (opcional):\n")
                extra = input("Ingrese informacion  extra (opcional):\n")
                letra = nombre[:1]
                if letra in contacts:
                    contacts[letra][nombre] = {'telefono': numero, 'email': mail, 'company': empresa, 'extra': extra}
                else:
                    contacts[letra]={}
                    contacts[letra]={nombre:{'telefono': numero, 'email': mail, 'company': empresa, 'extra': extra}}

                print(emoji.emojize((f"\n¡Contacto '{nombre}' guardado con éxito! :white_check_mark:\n"), use_aliases=True))
            else:
                print("WARNING!!! Su correo debe tener solamente una '@' y un dominio valido\n")
        else:
            print(" WARNING!!! El telefono debe contener solamente numeros\n")
    else:
        print(" WARNING!!! El nombre debe contener al menos un nombre y un apellido\n")
    terminar=input("---------Presione una tecla para continuar---------\n")

def buscarContacto():
    nombre = input("Ingrese su búsqueda de contacto:\n")
    input_nombre=nombre.casefold()
    letras=list(contacts.keys())
    print("\nResultados:")
    print("*Si no se muestra una lista, no hay contactos relacionados con su busqueda\n")

    for i in letras:
        for x in range(len(contacts[i])):
            name= list(contacts[i].keys())[x]
            comparar=str(name.casefold())
            if comparar.find(input_nombre) != -1:
                print(f"    - {name}")
    print("\n")
    terminar=input("-------Si ya termino su búsqueda, presione una tecla-------\n")




def eliminarContacto():
    nombre = input("Ingrese nombre del contacto que quiere eliminar\n")
    input_nombre=nombre.title()
    letra = input_nombre[:1]
    if letra in contacts:
        if input_nombre in contacts[letra]:
            contacts[letra].pop(input_nombre)
            print(f"Contacto '{input_nombre}' está siendo eliminado...")
            time.sleep(3)
            print('¡Contacto eliminado con éxito!\n')
        else:
            print("El contacto no existe, intentelo de nuevo\n")
            time.sleep(1)
    else:
        print("El contacto no existe, intentelo de nuevo\n")
        time.sleep(1)


def listarContactos():
    ordenados = orden_alfabetico(contacts)
    letras = ordenados.keys()
    print("\nListado de contactos:")
    contador = 1
    for i in letras:
        print('\n',i + ': ','\n')
        for contacto in ordenados[i]:
            print(str(contador)+ '.', contacto)
            contador += 1
    print("------------------------- \n")

def verContactos():
    contacto_init=input("Ingrese el nombre del contacto que desea ver:\n")
    contacto=contacto_init.title()
    letra = contacto[:1]
    if  letra in contacts:
        if contacto in contacts[letra]:
            print(f'=========================================\n')
            print(f"\nVer '{contacto}':\n")
            print(emoji.emojize((f" :phone: Telefono: {contacts[letra][contacto]['telefono']}  \n"), use_aliases=True))
            print(emoji.emojize((f" :email: Email: {contacts[letra][contacto]['email']} \n"), use_aliases=True))
            print(emoji.emojize((f" :house: Company: {contacts[letra][contacto]['company']} \n"), use_aliases=True))
            print(emoji.emojize((f" :round_pushpin: Extra: {contacts[letra][contacto]['extra']}  \n"), use_aliases=True))
        else:
            print("El contacto no existe, intentelo de nuevo\n")
            time.sleep(1)
    else:
        print("     El contacto no existe, intentelo de nuevo\n")
        time.sleep(1)
    print("========================================")
    terminar=input("---------Presione una tecla para continuar---------\n")



def guardar():
    data =  orden_alfabetico(contacts) 
    ## W da permisos de escritura
    outputFile = csv.writer(open("contact_manager.csv", "w", newline=''))
    ##Crea encabezados
    outputFile.writerow(["nombre", "telefono", "email", "company", "extra"])
    ##Lenna de data
    for item in data:
        for detail in data[item]:
            outputFile.writerow([detail,
                        data[item][detail]["telefono"],
                        data[item][detail]["email"],
                        data[item][detail]["company"],
                        data[item][detail]["extra"]])

    print(emoji.emojize((f"     Sus contactos están siendo guardados :open_file_folder: ..."), use_aliases=True))
    time.sleep(3)
    print('     ¡Contactos guardados en su computadora!, encuentrelos como "contact_manager.csv"  \n')

def llamar():
    contacto_init=input("Ingrese el nombre del contacto al que desea llamar:\n")
    contacto=contacto_init.title()
    letra = contacto[:1]
    if letra in contacts:
        if contacto in contacts[letra]:
            print(emoji.emojize((f"Llamando a {contacto} al {contacts[letra][contacto]['telefono']} :phone: ...\n"), use_aliases=True))
            time.sleep(3)
            print('         ¡Llamada finalizada!\n')
            time.sleep(1)
        else:
            print("El contacto no existe, intentelo de nuevo\n")
            time.sleep(1)
    else:
        print("         El contacto no existe, intentelo de nuevo\n")
        time.sleep(1)

def mensaje():
    contacto_init=input("Ingrese el nombre del contacto al que desea enviar un mensaje:\n")
    contacto=contacto_init.title()
    letra = contacto[:1]
    if  letra in contacts:
        if contacto in contacts[letra]:
            mensaje=input(f"Escriba el mensaje que desea enviar a {contacto}:\n")
            print(emoji.emojize((f"\nPara: {contacto} al {contacts[letra][contacto]['telefono']} :calling: ...\n"), use_aliases=True))
            print(f">> {mensaje}\n")
            time.sleep(3)
            print('         ¡Mensaje enviado exitosamente!\n')
            time.sleep(1)
        else:
            print("El contacto no existe, intentelo de nuevo\n")
            time.sleep(1)
    else:
        print("         El contacto no existe, intentelo de nuevo\n")
        time.sleep(1)

def email():
    contacto_init=input("Ingrese el nombre del contacto para enviar el email:\n")
    contacto=contacto_init.title()
    letra = contacto[:1]
    if  letra in contacts:
        if contacto in contacts[letra]:
            subject=input("Escriba el asunto de su correo electronico:\n")
            mensaje=input(f"Escriba el body que desea enviar a {contacto} por mail:\n")
            print(emoji.emojize((f"\nPara: {contacto} al {contacts[letra][contacto]['email']} :email: ...\n"), use_aliases=True))
            print(f">> Asunto:{subject}\n --{mensaje}\n") 
            time.sleep(3)
            print('         ¡Email enviado exitosamente!\n')
            time.sleep(1)
        else:
            print("El contacto no existe, intentelo de nuevo\n")
            time.sleep(1)
    else:
        print("El contacto no existe, intentelo de nuevo\n")
        time.sleep(1)


while not exit:
    print("\n\n==========Menu principal===========")
    input_menu = int(input(" 1. Agregar Contacto \n 2. Buscar Contacto\n 3. Listar Contacto\n 4. Eliminar Contacto\n 5. Llamar Contactos\n 6. Enviar SMS a contacto\n 7. Enviar mail a Contacto\n 8. Guardar/Exportar contactos creados\n 9. Salir\n"))
    if input_menu == 1:
        clear()
        crearContacto()
    if input_menu == 2:
        clear()
        buscarContacto()
    if input_menu == 3:
        clear()
        listarContactos()
        verContactos()
    if input_menu == 4:
        clear()
        listarContactos()
        eliminarContacto()
    if input_menu == 5:
        clear()
        listarContactos()
        llamar()
    if input_menu == 6:
        clear()
        listarContactos()
        mensaje()
    if input_menu == 7:
        clear()
        listarContactos()
        email()
    if input_menu == 8:
        clear()
        guardar()
    elif input_menu == 9:
        clear()
        print(f">> Saliendo...\n") 
        time.sleep(0.5)
        exit = True
