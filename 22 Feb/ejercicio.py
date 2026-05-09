class Solution:
    # SOLUCION SIN OPTIMIZAR (fuerza bruta)

    # SUBPROBLEMA:
    # Probar todos los subarreglos contiguos posibles y quedarse
    # con la suma maxima encontrada.

    # RECURRENCIA:
    # Para cada par (i, j) con i <= j, calcular la suma de nums[i..j]
    # y comparar con la mejor suma vista hasta el momento.

    # CASOS BASE:
    # Si el arreglo tiene un solo elemento, ese es el resultado.

    # COMPLEJIDAD:
    # Tiempo O(n^2), dos ciclos anidados para probar todos los pares (i, j).
    # Espacio O(1), solo se usan variables auxiliares.

    def maxSubarray_brute_force(nums: list[int]) -> int:
        n = len(nums)
        mejor = nums[0]

        for i in range(n):
            suma_actual = 0
            for j in range(i, n):
                suma_actual += nums[j]
                if suma_actual > mejor:
                    mejor = suma_actual

        return mejor
        