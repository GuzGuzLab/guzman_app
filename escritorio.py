from datetime import date

class Escritorio:
    contador_objetos = 0

    def __init__(self):

        self.__marca = ""
        self.__color = ""
        self.__precio = 0.0
        self.__forma = ""
        self.__medidas = 0
        Escritorio.contador_objetos += 1

    def set_marca(self, marca):
        self.__marca = marca

    def set_color(self, color):
        if color in ["amarillo", "madera", "negro", "gris"]:
            self.__color = color
        else:
            raise ValueError("El color debe ser 'amarillo', 'madera', 'negro' o 'gris'.")

    def set_precio(self, precio):
        if isinstance(precio, float) and 0.0 < precio <= 1000000.0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser un número flotante positivo entre 0.0 y 1000000.0.")

    def set_forma(self, forma):
        if forma in ["circular", "cuadrada"]:
            self.__forma = forma
        else:
            raise ValueError("La forma debe ser 'circular' o 'cuadrada'.")

    def set_medidas(self, medidas):
        if isinstance(medidas, int) and 20 <= medidas <= 180:
            self.__medidas = medidas
        else:
            raise ValueError("Las medidas deben ser un entero entre 20 y 180 cm.")

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

 
    @classmethod
    def vender(cls):
        print(f"Escritorios disponibles para la venta: {cls.contador_objetos}")

    @staticmethod
    def saludar():
        print(f"Bienvenidos, hoy es el día: {date.today()}")

escritorio1 = Escritorio()
escritorio1.set_marca("Ikea")
escritorio1.set_color("madera")
escritorio1.set_precio(500000.0)
escritorio1.set_forma("cuadrada")
escritorio1.set_medidas(120)

escritorio2 = Escritorio()
escritorio2.set_marca("Home Center")
escritorio2.set_color("negro")
escritorio2.set_precio(600000.0)
escritorio2.set_forma("circular")
escritorio2.set_medidas(100)

escritorio3 = Escritorio()
escritorio3.set_marca("Oficina Plus")
escritorio3.set_color("gris")
escritorio3.set_precio(750000.0)
escritorio3.set_forma("cuadrada")
escritorio3.set_medidas(140)

escritorio4 = Escritorio()
escritorio4.set_marca("Faber")
escritorio4.set_color("amarillo")
escritorio4.set_precio(300000.0)
escritorio4.set_forma("circular")
escritorio4.set_medidas(90)

escritorio5 = Escritorio()
escritorio5.set_marca("DecoHome")
escritorio5.set_color("madera")
escritorio5.set_precio(850000.0)
escritorio5.set_forma("cuadrada")
escritorio5.set_medidas(160)

print(f"Escritorio 1: Marca: {escritorio1.get_marca()}, Color: {escritorio1.get_color()}, Precio: {escritorio1.get_precio()}, Forma: {escritorio1.get_forma()}, Medidas: {escritorio1.get_medidas()}")
print(f"Escritorio 2: Marca: {escritorio2.get_marca()}, Color: {escritorio2.get_color()}, Precio: {escritorio2.get_precio()}, Forma: {escritorio2.get_forma()}, Medidas: {escritorio2.get_medidas()}")

print(f"Total de escritorios creados: {Escritorio.contador_objetos}")

Escritorio.saludar()
Escritorio.vender()