from .models import *

#VALIDACIÓN DE TEXTOS
def alphabet_surname(only_alphabet):
    
    if(only_alphabet == ""):
        flag_alphabet = False
    else:
        for cadena in only_alphabet:
            if (cadena == "Á") or (cadena == "É") or (cadena == "Í") or (cadena == "Ó") or (cadena == "Ú") or (cadena == "Ü") or (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == "'") or (cadena == "´"):
                flag_alphabet = True
            else:
                flag_alphabet = False
                break
            
    return flag_alphabet


def alphabet_name(only_alphabet):
    
    for cadena in only_alphabet:
        if (cadena == "Á") or (cadena == "É") or (cadena == "Í") or (cadena == "Ó") or (cadena == "Ú") or (cadena == "Ü") or (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == "'") or (cadena == "´"):
            flag_alphabet = True
        else:
            flag_alphabet = False
            break
            
    return flag_alphabet


def alphabet_department(only_alphabet):
    
    for cadena in only_alphabet:
        if (cadena == "Á") or (cadena == "É") or (cadena == "Í") or (cadena == "Ó") or (cadena == "Ú") or (cadena == "Ü") or (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == ""):
            flag_alphabet = True
        else:
            flag_alphabet = False
            break
            
    return flag_alphabet


def alphabet_province(only_alphabet):

    for cadena in only_alphabet:
        if (cadena == "Á") or (cadena == "É") or (cadena == "Í") or (cadena == "Ó") or (cadena == "Ú") or (cadena == "Ü") or (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == ""):
            flag_alphabet = True
        else:
            flag_alphabet = False
            break
            
    return flag_alphabet


def cod_postal(only_number):
    
    if (only_number == ""):
        flag_number = True
    else:
        if(only_number != ""):

            for i in only_number:
                if (i == "0") or (i == "1") or (i == "2") or (i == "3") or (i == "4") or (i == "5") or (i == "6") or (i == "7") or (i == "8") or (i == "9"):
                    flag_number = True
                else:
                    flag_number = False
                    break
            
    return flag_number
 

# VALIDACIÓN TIPO PRENDA / CATEGORÍA
def alphabet_category_name(only_alphabet):
    
    if(only_alphabet == ""):
        flag_alphabet = False
    else:
        for cadena in only_alphabet:
            if (cadena == "Á") or (cadena == "É") or (cadena == "Í") or (cadena == "Ó") or (cadena == "Ú") or (cadena == "Ü") or (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == "'") or (cadena == "´"):
                flag_alphabet = True
            else:
                flag_alphabet = False
                break
    
    return flag_alphabet


# VALIDACIÓN DESCRIPCIÓN PRODUCTO
def alphabet_name2(only_alphabet):
    
    if(only_alphabet == ""):
        flag_alphabet = False
    else:
        for cadena in only_alphabet:
            if (cadena == "Á") or (cadena == "É") or (cadena == "Í") or (cadena == "Ó") or (cadena == "Ú") or (cadena == "Ü") or (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == "0") or (cadena == "1") or (cadena == "2") or (cadena == "3") or (cadena == "4") or (cadena == "5") or (cadena == "6") or (cadena == "7") or (cadena == "8") or (cadena == "9") or (cadena == "-") or (cadena == "+") or (cadena == "(") or (cadena == ")") or (cadena == "'") or (cadena == "´"):
                flag_alphabet = True
            elif (cadena == ""):
                flag_alphabet = False
                break
            else:
                flag_alphabet = False
                break
            
    return flag_alphabet


def alphabet_number_size(only_alphabet):
    
    if(only_alphabet == ""):
        flag_alphabet = False
    else:
        for cadena in only_alphabet:
            if (cadena == "A") or (cadena == "B") or (cadena == "C") or (cadena == "D") or (cadena == "E") or (cadena == "F") or (cadena == "G") or (cadena == "H") or (cadena == "I") or (cadena == "J") or (cadena == "K") or (cadena == "L") or (cadena == "M") or (cadena == "N") or (cadena == "Ñ") or (cadena == "O") or (cadena == "P") or (cadena == "Q") or (cadena == "R") or (cadena == "S") or (cadena == "T") or (cadena == "U") or (cadena == "V") or (cadena == "W") or (cadena == "X") or (cadena == "Y") or (cadena == "Z") or (cadena == " ") or (cadena == "0") or (cadena == "1") or (cadena == "2") or (cadena == "3") or (cadena == "4") or (cadena == "5") or (cadena == "6") or (cadena == "7") or (cadena == "8") or (cadena == "9"):
                flag_alphabet = True
            else:
                flag_alphabet = False
                break
            
    return flag_alphabet
