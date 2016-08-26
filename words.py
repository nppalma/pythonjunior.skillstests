import sys
import os.path


def words(arg):
    file_arg = arg
    if os.path.exists(file_arg):  # Veo si existe la ruta al archivo pasado como parametro
        file = open(file_arg, "r")  #  Abro el archivo en modo lectura

        text = file.read()  # Obtengo el texto
        words = text.split()  # Separo las palabras del archivo por espacios
        lista = []

        for w in words:  # Recorro la lista de palabras
            count_consonants = 0  # Contador utilizado para ver si la palabra tiene >= 3 consonantes
            for c in w:  # Analizo caracter por caracter
                if c not in ('a', 'e', 'i', 'o', 'u'):  # Si no es una vocal, incremento el contador
                    count_consonants += 1
            if(count_consonants >= 3):  # Si tiene al menos 3 consonantes agrego la palabra a la lista
                lista.append(w)

        print lista  # Imprimo la lista
        return lista

    else:  # Si no existe la ruta pasada como argumento
        print "La ruta del archivo no existe!"

words(sys.argv[1])
