#Importamos primeramente la libreria de googlesearch 
import googlesearch

def rea_busqueda(objetivo):
    resultados = []

    # mediante esta linea de codigo podremos realizar bsuquedas en google
    resultados = googlesearch.search(objetivo, num_results = 5)
    return resultados

def guar_resultado_archivo(rersultados, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for resultado in resultados:
            archivo.write(resultado + '\n')

if __name__ == '__main__':
    objetivo = input("Hola, introduzca el nombre del objetivo de busqueda: ")

    resultados = rea_busqueda(objetivo)

    nombre_archivo = 'resultdo.txt'

    guar_resultado_archivo(resultados, nombre_archivo)
    
    #Esta linea de codigo nos mostrara un mensaje donde el archivo ya ha sidfo guardado
    print("Los resultados de la investigtacion reralizada se almaceno correctamente en {nombre_archivo}")