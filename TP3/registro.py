def convertir_titulo(i):
    lenguajes = ('Python', 'Java', 'C++', 'Javascript', 'Shell', 'HTML', 'Ruby', 'Swift', 'C#', 'VB', 'Go')
    return lenguajes[i]


class Proyecto:
    def __init__(self, numero, fecha, titulo, lenguaje, cant_lineas):
        self.numero = numero
        self.fecha = fecha
        self.titulo = titulo
        self.lenguaje = lenguaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        res = "Número: " + str(self.numero)
        res += "- Fecha: " + self.fecha
        res += "- Titulo: " + self.titulo
        res += "- Lenguaje: " + convertir_titulo(self.lenguaje)
        res += "- Cantidad de lineas: " + str(self.cant_lineas)
        return res


# proyecto = Proyecto(1, "12-06-2008", "ArtPac", 4, 120)
# print(proyecto)
