import random
import timeit
import itertools

# ------------------------------------------------------------
# Función 1
# ------------------------------------------------------------
def funcion_alpha(lista):
    longitud = len(lista)                                     # O(1)
    suma_elementos = sum(lista)                               # O(n)
    media = suma_elementos / longitud if longitud > 0 else 0  # O(1)
    lista_modificada = [x + 1 for x in lista]                 # O(n)
    lista_ordenada = sorted(lista_modificada)                 # O(n log n)
    return lista_ordenada, media                              # O(1)
# orden de complejidad de la función alpha =                    O(n log n)


# ------------------------------------------------------------
# Función 2
# ------------------------------------------------------------
def funcion_beta(n):
    resultados = []                       # O(1)
    for i in range(2 ** n):               # O(2^n)
        combinacion = []                  # O(1)
        for j in range(n):                # O(n)
            if (i >> j) & 1:              # O(1)
                combinacion.append(1)     # O(1)
            else:
                combinacion.append(0)     # O(1)
        resultados.append(combinacion)    # O(1)
    return resultados                     # O(1)
# orden de complejidad de la función beta = O(n * 2^n)


# ------------------------------------------------------------
# Función 3
# ------------------------------------------------------------
def funcion_gamma(lista):
    x = 10                                 # O(1)
    y = 20                                 # O(1)
    z = x * y                              # O(1)
    elemento = lista[0]                    # O(1)
    resultado = elemento + z               # O(1)
    valor_extra = resultado * 2 - 3        # O(1)
    return valor_extra                     # O(1)
# orden de complejidad de la función gamma = O(1)


# ------------------------------------------------------------
# Función 4
# ------------------------------------------------------------
def funcion_delta(estructura):
    total = 0                              # O(1)
    for bloque in estructura:              # O(n)
        for fila in bloque:                # O(n²)
            for valor in fila:             # O(n³)
                total += valor             # O(1)
    return total                           # O(1)
# orden de complejidad de la función delta = O(n³)


# ------------------------------------------------------------
# Función 5
# ------------------------------------------------------------
def funcion_epsilon(lista):
    suma = 0                                 # O(1)
    promedio = sum(lista) / len(lista)       # O(n)
    for elemento in lista:                   # O(n)
        suma += elemento * 2                 # O(1)
    maximo = max(lista)                      # O(n)
    minimo = min(lista)                      # O(n)
    diferencia = maximo - minimo             # O(1)
    return suma + promedio + diferencia      # O(1)
# orden de complejidad de la función epsilon = O(n)


# ------------------------------------------------------------
# Función 6
# ------------------------------------------------------------
def funcion_zeta(matriz):
    total = 0                             # O(1)
    for fila in matriz:                   # O(n)
        for valor in fila:                # O(n²)
            total += valor                # O(1)
    return total                          # O(1)
# orden de complejidad de la función zeta = O(n²)


# ------------------------------------------------------------
# Función 7
# ------------------------------------------------------------
def funcion_theta(n):                                        
    elementos = list(range(n))                               # O(1)
    permutaciones = list(itertools.permutations(elementos))  # O(n * n!)
    return permutaciones                                     # O(1)
# orden de complejidad de la función theta =                   O(n * n!)


# ------------------------------------------------------------
# Función 8
# ------------------------------------------------------------
def funcion_omega(lista, objetivo):          
    izquierda, derecha = 0, len(lista) - 1 # O(1)
    while izquierda <= derecha:            # O(log n)
        medio = (izquierda + derecha) // 2 # O(1)
        if lista[medio] == objetivo:       # O(1)
            return True                    # O(1)
        elif lista[medio] < objetivo:      # O(1)
            izquierda = medio + 1          # O(1)
        else:
            derecha = medio - 1            # O(1)
    return False                           # O(1)
# orden de complejidad de la función omega = O(log n)

# ------------------------------------------------------------
# Parte 2: Pruebas de tiempo de ejecución (Corregida)
# ------------------------------------------------------------
if __name__ == "__main__":
    tamanos = [100, 250, 500, 750, 1000]
    
    for n in tamanos:
        print(f"\n--- Tamaño n = {n} ---")
        
        # 1. Generación de datos proporcionales a 'n'
        lista = [random.randint(1, 100) for _ in range(n)] 
        matriz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]  
        estructura = [[[random.randint(1, 100) for _ in range(n)] for _ in range(n)] for _ in range(n)]  
        
        # 2. Preparación previa para algoritmos (no medir esto en timeit)
        lista_ordenada = sorted(lista)
        objetivo_busqueda = random.choice(lista_ordenada)
        
        # 3. Medición de tiempos (promediando por el número de repeticiones)
        reps_rapidas = 100
        
        # t_gamma = timeit.timeit(lambda: funcion_gamma(lista), number=reps_rapidas) / reps_rapidas
        # t_omega = timeit.timeit(lambda: funcion_omega(lista_ordenada, objetivo_busqueda), number=reps_rapidas) / reps_rapidas
        # t_epsilon = timeit.timeit(lambda: funcion_epsilon(lista), number=reps_rapidas) / reps_rapidas
        # t_alpha = timeit.timeit(lambda: funcion_alpha(lista), number=reps_rapidas) / reps_rapidas
        
        # print(f"funcion_gamma: {t_gamma:.8f} s")
        # print(f"funcion_omega: {t_omega:.8f} s")
        # print(f"funcion_epsilon: {t_epsilon:.8f} s")
        # print(f"funcion_alpha: {t_alpha:.8f} s")
        
        # Las funciones con bucles anidados son más lentas, reducimos las repeticiones a 10
        reps_lentas = 10
        # t_zeta = timeit.timeit(lambda: funcion_zeta(matriz), number=reps_lentas) / reps_lentas
        # t_delta = timeit.timeit(lambda: funcion_delta(estructura), number=reps_lentas) / reps_lentas
        
        # print(f"funcion_zeta: {t_zeta:.8f} s (tamaño real usado: {n}^2)")
        # print(f"funcion_delta: {t_delta:.8f} s (tamaño real usado: {n}^3)")
    
    # 4. Ejemplos controlados para las de mayor complejidad
    # print("\n--- Pruebas para complejidad Exponencial y Factorial ---")
    reps_ext = 1
    # t_beta = timeit.timeit(lambda: funcion_beta(10), number=reps_ext) / reps_ext
    # t_theta = timeit.timeit(lambda: funcion_theta(6), number=reps_ext) / reps_ext
    # print(f"funcion_beta    (O(2^n)) n=10: {t_beta:.8f} s")
    # print(f"funcion_theta   (O(n!))  n=6 : {t_theta:.8f} s")