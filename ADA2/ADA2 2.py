from queue import Queue

class SistemaColas:
    def __init__(self, num_servicios):
        self.servicios = {i: Queue() for i in range(1, num_servicios + 1)}
        self.contadores = {i: 0 for i in range(1, num_servicios + 1)}

    def agregar_cliente(self, servicio):
        self.contadores[servicio] += 1
        numero = self.contadores[servicio]
        self.servicios[servicio].put(numero)
        print(f"Cliente agregado al servicio {servicio} con número {numero}")

    def atender_cliente(self, servicio):
        if not self.servicios[servicio].empty():
            numero = self.servicios[servicio].get()
            print(f"Atendiendo al cliente número {numero} del servicio {servicio}")
        else:
            print(f"No hay clientes en la cola del servicio {servicio}")

if __name__ == "__main__":
    sistema = SistemaColas(3)

    while True:
        entrada = input("Ingrese comando (C n = cliente, A n = atender, S = salir): ").strip().upper()
        if entrada == "S":
            break
        try:
            letra, num = entrada.split()
            num = int(num)
            if letra == "C":
                sistema.agregar_cliente(num)
            elif letra == "A":
                sistema.atender_cliente(num)
            else:
                print("Comando no reconocido.")
        except ValueError:
            print("Formato inválido. Use 'C n' o 'A n'.")
