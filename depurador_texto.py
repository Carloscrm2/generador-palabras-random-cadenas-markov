# Este script depura un texto en portugues para quitar todo los caracteres especiales, ademas
# de quitar saltos de linea, esto con el fin de poder hacer el analisis correspondiente
# y poder realizar el generador de palabras, este script se puede adaptar al idioma que se desee

# El texto que se depura es el archivo "texto-en-portugues.txt" que contiene un fragmento del libro
# ensayo sobre la ceguera de jose saramago.  

def leer_archivo(nombre_archivo):
    aux = ""
    ruta = nombre_archivo
    with open(ruta, 'r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            aux = aux + line
    print(aux)
    print(len(aux))
    f.close()
    archivo_depurado(aux)
    
def archivo_depurado(cadena):
    ruta = "texto_depurado.txt"
    f = open(ruta, "w", encoding="utf-8")
    # Quitamos los caracteres especiales y pasamos toda a minisculas
    cadena = cadena.replace("(", "")
    cadena = cadena.replace(")", "")
    cadena = cadena.replace(";", "")
    cadena = cadena.replace("0", "")
    cadena = cadena.replace("1", "")
    cadena = cadena.replace("2", "")
    cadena = cadena.replace("3", "")
    cadena = cadena.replace("4", "")
    cadena = cadena.replace("5", "")
    cadena = cadena.replace("6", "")
    cadena = cadena.replace("7", "")
    cadena = cadena.replace("8", "")
    cadena = cadena.replace("9", "")
    cadena = cadena.replace("1", "")
    cadena = cadena.replace("\n", "")
    cadena = cadena.replace(",", "")
    cadena = cadena.replace("-", "")
    cadena = cadena.replace(".", "")
    cadena = cadena.replace(":", "")
    cadena = cadena.replace("—", "")
    cadena = cadena.lower()
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    cadena = cadena.replace("â", "a")
    cadena = cadena.replace("ê", "e")
    cadena = cadena.replace("î", "i")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ô", "o")
    cadena = cadena.replace("õ", "o")
    cadena = cadena.replace("û","u")
    cadena = cadena.replace("ü", "u")
    cadena = cadena.replace("ã","a")
    cadena = cadena.replace("à", "a")
    cadena = cadena.replace("?", "")
    cadena = cadena.replace("¿", "")
    cadena = cadena.replace("~", "")
    # cadena = cadena.replace("ç", "c")
    cadena = cadena.replace(" ", "&")
    #cadena = cadena.replace(" ", "")
    print(len(cadena))
    f.write(cadena)
    f.close()

leer_archivo("texto-en-portugues.txt")