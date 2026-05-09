# -----------------------------------------------------------------------------
# SOLUCION FUERZA BRUTA O(n^2)
# -----------------------------------------------------------------------------

# SUBPROBLEMA:
# Para cada indice i, acumular la suma extendiéndose hacia la derecha
# y comparar con la mejor suma vista hasta el momento.

# RECURRENCIA:
# Para cada i, ir sumando nums[j] conforme j avanza desde i.
# mejor = max(mejor, suma_acumulada)

# CASOS BASE:
# Si el arreglo tiene un solo elemento, ese es el resultado.

# COMPLEJIDAD:
# Tiempo O(n^2), dos ciclos anidados sin suma interna separada.
# Espacio O(1), solo se usan variables auxiliares.

def maxSubArray_on2(nums: list[int]) -> int:
    n = len(nums)
    mejor = nums[0]
    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += nums[j]  # acumula sin tercer ciclo
            if suma_actual > mejor:
                mejor = suma_actual
    return mejor