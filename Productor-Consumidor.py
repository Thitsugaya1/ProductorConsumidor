# -*- coding: utf-8 -*-
"""
@author: Thitsugaya1
"""
import sys, queue, random, time
from threading import Thread

#se definen las variables que son ingresadas por consola
global queueProductos, consumidores, productores, bufferSize

#Validamos que existan los argumentos
if len(sys.argv) != 4:
    print ("Error al leer el los datos, debe existir un numero de Consumidores, productores y buffer")
    sys.exit()
elif len(sys.argv) == 4:
    consumidores = int(sys.argv[1])
    productores = int(sys.argv[2])
    bufferSize =int(sys.argv[3])
#Se crea la Queue a utilizar
queueProductos = queue.Queue(maxsize = bufferSize) 

#Clase del productor
class productor(Thread):
    #Constructor
    def __init__(self, id):
        Thread.__init__(self)
        self.__id__ = id
        return
    
    #Metodo para ejecutar el productor    
    def run(self):
        while True:
            if not queueProductos.full():
                item = random.randint(100, 110)
                queueProductos.put(item)
    
                print("Se agrego un item con codigo:", item,", por parte del productor:", self.__id__)
    
                time_to_sleep = random.randint(1, 3)
                time.sleep(time_to_sleep)

#Clase del consumior
class consumidor(Thread):
    #Constructor    
    def __init__(self, id):
        Thread.__init__(self)
        self.__id__ = id
        return
    
    #Metodo para ejecutar el consumidor
    def run(self):
        while True:
            if not queueProductos.empty():
                item = queueProductos.get()
                queueProductos.task_done()
        
                print("Se consumio el item de codigo:", item,", por parte del consumidor:", self.__id__)
        
                time_to_sleep = random.randint(1, 3)
                time.sleep(time_to_sleep)

def main ():   
    
    #se considera que como existe un numero X de consumidores 
    #y otro Y de productores, la creacion de 2 listas que guardaran
    #cada una de las instancias de los hilos/threads
    consumer = []
    producter = []
   
    for i in range (0, productores):
        producter += [productor(i)]
    for i in range (0, consumidores):
        consumer += [consumidor(i)]

    for product in producter:
        product.start()
    for consum in consumer:
        consum.start()
    
    for product in producter:
        product.join()
    for consum in consumer:
        consum.join()

if __name__ == '__main__':
    main()