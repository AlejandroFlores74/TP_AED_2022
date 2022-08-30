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
        cadena = 'numero: {:<10} fecha: {:<20} titulo: {:<10} Lenguaje: {:<10} cantidad de lineas {:<10}'
        return cadena.format(self.numero,
                             str(self.fecha),
                             self.titulo,
                             convertir_titulo(self.lenguaje),
                             self.cant_lineas)


# proyecto = Proyecto(1, "12-06-2008", "ArtPac", 4, 120)
# print(proyecto)
