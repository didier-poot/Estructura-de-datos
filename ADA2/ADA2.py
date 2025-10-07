from queue import Queue

def sumar_colas(colaA, colaB):
    cola_resultado = Queue()
    
    while not colaA.empty() and not colaB.empty():
        a = colaA.get()
        b = colaB.get()
        cola_resultado.put(a + b)
    
    return cola_resultado

colaA = Queue()
colaB = Queue()

for n in [3, 4, 8, 12]:
    colaA.put(n)

for n in [6, 2, 9, 3]:
    colaB.put(n)

colaResultado = sumar_colas(colaA, colaB)

print("Cola Resultado:")
while not colaResultado.empty():
    print(colaResultado.get())
