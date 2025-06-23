from collections import Counter

def imprimir_top(titulo, valores, n):
    if not valores:
        print(f"\nPara la {titulo}:\n  No hay datos.")
        return

    contador = Counter(valores)
    mas_comunes = contador.most_common(n)

    print(f"\nPara la {titulo}:")
    
    def ordinal(i):
        sufijos = ["primer", "segundo", "tercer", "cuarto", "quinto", "sexto", "séptimo", "octavo", "noveno", "décimo"]
        if i < len(sufijos):
            return f"El {sufijos[i]} más común"
        else:
            return f"El {i+1}° más común"

    for i, (valor, cant) in enumerate(mas_comunes):
        print(f"  {ordinal(i)} es '{valor}' con {cant} apariciones.")

def analizar_respuestas(k=1, n=5):
    with open("respuestas.csv", "r", encoding="utf-8") as archivo:
        lista = archivo.readlines()

    with open("normalizado.csv", "r", encoding="utf-8") as archivo:
        normalizados = archivo.readlines()

    valores1 = []
    valores2 = []
    valores3 = []

    intereses = []

    for i, linea in enumerate(lista):
        valor = linea.replace("\xa0;", ";").strip(";\n").split(";")
        if i >= len(normalizados):
            continue
        normalizado = normalizados[i].strip().split(",")
        if len(valor) < 2:
            continue
        if valor[0] == "G23":
            valores1.append(valor[1])
        elif valor[0] == "G24":
            valores2.append(valor[1])
        else:
            valores3.append(valor[1])

        intereses += normalizado[:k]

    valores_total = valores1 + valores2 + valores3
    valores_peso = valores1 * 3 + valores2 * 2 + valores3

    imprimir_top("G23", valores1, n)
    imprimir_top("G24", valores2, n)
    imprimir_top("G25", valores3, n)
    imprimir_top("carrera", valores_total, n)
    imprimir_top("carrera con peso", valores_peso, n)
    imprimir_top("carrera real", intereses, n)

analizar_respuestas()
