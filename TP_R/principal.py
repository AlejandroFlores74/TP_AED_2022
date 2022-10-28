def mostrar_menu():
    equals = '='
    print('\n' + equals * 25 + ' !SERIES DE TELEVISION! ' + equals * 25 + '\n'
          '1) Procesar el archivo de texto generos.txt\n'
          '2) Procesar el archivo de texto series.csv\n'
          '3) de la opcion 2, mostrar series que tengan una duración en minutos entre a y b al final mostrar duracion '
          'promedio y almacenar el listado en un archivo de texto con el formato original, sin los campos omitidos.\n'
          '4) Generar un vector de conteo se determinar la cantidad de series por cada uno de los géneros posibles\n'
          '5) Buscar proyecto para actualizar fecha y url.\n'
          '6) Mostrar el archivo generado en el punto 5.\n'
          '7) Buscar si en el vector de series se encuentra una serie con el campo Series_Title igual a tit, '
          'Si se encuentra incrementar su número de votos en uno. Si no se encuentra mostrar un mensaje\n'
          '0) Salir del Programa\n')


def grabar_nombres(generos, path_name='generos.txt'):
    m = open(path_name, 'r')
    nro_linea = 0
    for linea in m:
        nro_linea += 1
        if nro_linea == 1:
            continue

        if linea[-1] == '\n':
            linea = linea[:-1]
        generos.append(linea)
    m.close()
    return generos


def add_in_order(v, series):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].no_of_vote == series.no_of_vote:
            pos = c
            break
        if v[c].no_of_vote > series.no_of_vote:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [series]


def filtrar_linea(campos):
    res = True
    if campos[4] == "":
        res = False
    return res


def cargar_archivo(v, generos, path_file="series_aed.csv"):
    if os.path.exists(path_file):
        nro_linea = 0
        m = open(path_file, mode="rt")
        for linea in m:
            nro_linea += 1
            if nro_linea == 1:
                continue

            if linea[-1] == '\n':
                linea = linea[:-1]
            campos = linea.split('|')

            if filtrar_linea(campos):
                poster_link = campos[0]
                series_title = campos[1]
                runtime_of_series = campos[2]
                certificate = campos[3]
                runtime_of_episodes = campos[4][0]
                genre = campos[5]
                imdb_rating = campos[6]
                overwiew = campos[7]
                star1 = campos[8]
                star2 = campos[9]
                star3 = campos[10]
                star4 = campos[11]
                no_of_vote = campos[12]

                proyecto = Series(poster_link, series_title, runtime_of_series, certificate, runtime_of_episodes,
                                  genre, imdb_rating, overwiew, star1, star2, star3, star4, no_of_vote)
                add_in_order(v, proyecto)
        m.close()


def mostrar_series(v, a, b):
    prom, suma, cant = 0, 0, 0
    for series in v:
        if a <= series.runtime_of_episodes <= b:
            print(series)
            cant += 1
            suma += int(series.runtime_of_episodes)

    prom = round(suma / cant, 2)

    print('la duracion promedio de las series es de: ', prom)


def principal():
    generos = []
    v = []
    op = -1
    while op != 0:
        mostrar_menu()
        op = int(input('ingrese opcion: '))
        if op == 1:
            grabar_nombres(generos)
        elif op == 2:
            cargar_archivo(v, generos)
        elif op == 3:
            a = input('ingrese minutos a comparar(A): ')
            b = input('ingrese minutos a comparar(B): ')
            mostrar_series(v, a, b)
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 0:
            print('programa finalizaco')
        else:
            print('ingrese opcion correcta')


if __name__ == '__main__':
    principal()
