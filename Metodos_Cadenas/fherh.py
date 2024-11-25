from datetime import datetime

class Escritorio:
    # Atributo de clase para contar los objetos creados
    contador_objetos = 0

    def __init__(self):
        self.__marca = None
        self.__color = None
        self.__precio = None
        self.__forma = None
        self.__medidas = None
        # Incrementa el contador cada vez que se crea un objeto
        Escritorio.contador_objetos += 1

    # Métodos SET
    def set_marca(self, marca):
        if isinstance(marca, str) and marca.strip():
            self.__marca = marca

    def set_color(self, color):
        if color in ['amarillo', 'madera', 'negro', 'gris']:
            self.__color = color

    def set_precio(self, precio):
        if isinstance(precio, (int, float)) and 0 < precio <= 1000000:
            self.__precio = precio

    def set_forma(self, forma):
        if forma in ['circular', 'cuadrada']:
            self.__forma = forma

    def set_medidas(self, medidas):
        if isinstance(medidas, int) and 20 <= medidas <= 180:
            self.__medidas = medidas

    # Métodos GET
    def get_marca(self):
        return self.__marca

    def get_color(self):
        return self.__color

    def get_precio(self):
        return self.__precio

    def get_forma(self):
        return self.__forma

    def get_medidas(self):
        return self.__medidas

    # Método para mostrar la información del escritorio
    def mostrar_informacion(self):
        print(f"Marca: {self.__marca}")
        print(f"Color: {self.__color}")
        print(f"Precio: {self.__precio}")
        print(f"Forma: {self.__forma}")
        print(f"Medidas: {self.__medidas}")

    # Método de clase para informar cuántos escritorios están disponibles
    @classmethod
    def vender(cls):
        print(f"Escritorios disponibles para vender: {cls.contador_objetos}")

    # Método estático para emitir un saludo con la fecha actual
    @staticmethod
    def saludar():
        hoy = datetime.now().strftime('%Y-%m-%d')
        print(f"Bienvenidos, hoy es el día: {hoy}")


# Crear objetos y usar los métodos SET para asignar valores
escritorio1 = Escritorio()
escritorio1.set_marca("Escritorio Moderno")
escritorio1.set_color("gris")
escritorio1.set_precio(950000)
escritorio1.set_forma("cuadrada")
escritorio1.set_medidas(120)

escritorio2 = Escritorio()
escritorio2.set_marca("Escritorio Compacto")
escritorio2.set_color("madera")
escritorio2.set_precio(850000)
escritorio2.set_forma("circular")
escritorio2.set_medidas(100)

escritorio3 = Escritorio()
escritorio3.set_marca("Escritorio Minimalista")
escritorio3.set_color("negro")
escritorio3.set_precio(780000)
escritorio3.set_forma("cuadrada")
escritorio3.set_medidas(110)

escritorio4 = Escritorio()
escritorio4.set_marca("Escritorio Elegante")
escritorio4.set_color("amarillo")
escritorio4.set_precio(720000)
escritorio4.set_forma("circular")
escritorio4.set_medidas(90)

escritorio5 = Escritorio()
escritorio5.set_marca("Escritorio Clásico")
escritorio5.set_color("madera")
escritorio5.set_precio(890000)
escritorio5.set_forma("cuadrada")
escritorio5.set_medidas(130)

# Usar los métodos GET para imprimir datos de dos objetos
print("Información del escritorio 1:")
print(f"Marca: {escritorio1.get_marca()}")
print(f"Color: {escritorio1.get_color()}")
print(f"Precio: {escritorio1.get_precio()}")
print(f"Forma: {escritorio1.get_forma()}")
print(f"Medidas: {escritorio1.get_medidas()} cm\n")

print("Información del escritorio 2:")
print(f"Marca: {escritorio2.get_marca()}")
print(f"Color: {escritorio2.get_color()}")
print(f"Precio: {escritorio2.get_precio()}")
print(f"Forma: {escritorio2.get_forma()}")
print(f"Medidas: {escritorio2.get_medidas()} cm\n")

# Imprimir el valor de la variable de clase contador_objetos
print(f"Total de objetos creados: {Escritorio.contador_objetos}\n")

# Usar el método estático saludar()
Escritorio.saludar()

# Usar el método de clase vender()
Escritorio.vender()