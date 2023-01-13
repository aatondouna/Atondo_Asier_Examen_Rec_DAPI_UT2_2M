countries_dict = {'Grecia':'30'}, {'Francia':'33'}, {'España':'34'}, {'Portugal':'351'},\
                 {'Ucrania':'380'}, {'Italia':'39'}, {'Suiza':'41'}, {'Reino Unido':'44'},\
                 {'Alemania':'49'}, {'Rusia':'7'}

nif_dict = {0:'T'}, {1:'R'}, {2:'W'}, {3:'A'}, {4:'G'}, {5:'M'}, {6:'Y'}, {7:'F'}, \
           {8:'P'}, {9:'D'}, {10:'X'}, {11:'B'}, {12:'N'}, {13:'J'}, {14:'Z'}, {15:'S'}, \
           {16:'Q'}, {17:'V'}, {18:'H'}, {19:'L'}, {20:'C'}, {21:'K'}, {22:'E'}

def check_DGT():
    """Funcion que lee y escribe un fichero
         Parametros:
            -
         Salida:
           -
"""
    import csv

    with open("DGT.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, ",", dialect=csv.excel)

    for persona in reader:
        print(persona)
        check_username(user_name, user_surname)
        check_phone()
        calculate_bill(bill)

help(check_DGT)

def check_username(user_name, user_surname):
    """Funcion que corrige errores gramaticales
            Parametros:
                - user_name: Es el nombre del usuario
                - user_surname: es el apellido del usuario
            Salidas:
                - La correccion de los nombres

    """
    return user_name.tittle,  user_surname.tittle

help(check_username)


def check_nif(user_nif):
 """Funcion que corrige el DNi
         Parametros:
              - user_nif: Es el nif de la persona
         Salidas:
            - La correccion del DNI
"""
    numero = str(user_nif[0:8])
    letra = nif_dict[str(int(user_nif[0:8]) % 23)]

    return numero + letra

help(check_nif)


def check_phone():
    """Funcion que comprueba el numero de telefono
         Parametros:
           -
         Salida:
           - El numero de telefono con el prefijo correspondiente
"""
help(check_phone)


def calculate_bill(bill):
 """" Funcion que calcula las multas a pagar
         Paramteros:
              - multas_radar: son las multas por radar
              - multas_ITV: son las multas por la ITV
              - multas_estupefacientes: son las multas por estupefacientes
         Salida:
             - El total de multas a pagar
"""
    bill = int(multas_radar) + int(multas_ITV) + int(multas_estupefacientes)
    return bill

help(calculate_bill)


