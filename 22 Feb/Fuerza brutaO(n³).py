
# SUBPROBLEMA:
# Para cada subarreglo posible nums[i..j], calcular su suma desde cero
# y comparar con la mejor suma vista hasta el momento.

# RECURRENCIA:
# Para cada par (i, j), sumar todos los elementos entre i y j.
# mejor = max(mejor, sum(nums[i..j]))

# CASOS BASE:
# Si el arreglo tiene un solo elemento, ese es el resultado.

# COMPLEJIDAD:
# Tiempo O(n^3), dos ciclos para los pares (i,j) y uno interno para sumar.
# Espacio O(1), solo se usan variables auxiliares.

def maxSubArray_on3(nums: list[int]) -> int:
    n = len(nums)
    mejor = nums[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):  # suma explícita del subarreglo
                suma += nums[k]
            if suma > mejor:
                mejor = suma
    return mejor
