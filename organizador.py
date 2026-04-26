from pathlib import Path 
import shutil 

textoPath = input("Dirección de la carpeta a ordenar (ejemplo: documentos/carpeta1/carpeta2/...)   ")
pathCarpeta= Path(textoPath)


while not pathCarpeta.exists():
    print("\n La carpeta ingresada no se encuentra...\n")
    textoPath = input("Dirección de la carpeta a ordenar (ejemplo: documentos/carpeta1/carpeta2/...)   ")
    
    pathCarpeta = Path(textoPath)

nombreCarpeta= pathCarpeta.stem #guardo el nombre de la carpeta para crear sus subcarpetas

textoSCPractica = "Práctica" + "_" + nombreCarpeta
textoSCTeoria = "Teoría" + "_" + nombreCarpeta
textoSCIndef = "Indefinido" + "_" + nombreCarpeta

pathSCPractica = pathCarpeta / textoSCPractica
pathSCTeoria = pathCarpeta / textoSCTeoria
pathSCIndef = pathCarpeta / textoSCIndef

pathSCPractica.mkdir(exist_ok=True)
pathSCTeoria.mkdir(exist_ok=True)
pathSCIndef.mkdir(exist_ok=True)

palabrasPractica = ["práctica", "practica", "ejercicios", "guía", "guia", "guias", "guías","ejs"]
palabrasTeoria = ["teoría", "teoria", "teórica", "teorica", "apunte", "apuntes", "libro", "diapositivas","diapositiva", "diapos", "clase"]

for elemento in pathCarpeta.iterdir():

    if elemento in [pathSCTeoria, pathSCPractica, pathSCIndef]:
        continue


    if elemento.is_dir():
        shutil.move(elemento, pathSCIndef / elemento.name )#todas las carpetas van aca


    elif elemento.is_file():
        nombreFile= elemento.stem.lower()
        
        if any(palabra in nombreFile for palabra in palabrasPractica):
            shutil.move(elemento, pathSCPractica) #guardo en carpeta práctica
        
        elif any(palabra in nombreFile for palabra in palabrasTeoria):
            shutil.move(elemento, pathSCTeoria)
        
        else:
            shutil.move(elemento, pathSCIndef)

print("Carpeta de estudio ordenada!")



