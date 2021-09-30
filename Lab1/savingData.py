import pickle

nombre_archivo="C:/UNIVERSITY/ST0246-TopicosTelematica-CristianCeballos/Lab1/data/archivo.txt"
puntajes = [("Negro", 1, "7:06"), ("Anaconda", 32, "6:3")]

def saveData(nombre_archivo, puntajes):
    archivo = open(nombre_archivo, "wb")
    pickle.dump(puntajes, archivo)
    archivo.close()

def callData(nombre_archivo):
    archivo = open(nombre_archivo, "rb")
    puntajes = pickle.load(archivo)
    archivo.close()
    return puntajes


saveData(nombre_archivo, puntajes)
data = callData(nombre_archivo)
print(data)