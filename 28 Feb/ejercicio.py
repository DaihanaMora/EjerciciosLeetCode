# ESTRATEGIA GREEDY:
# La idea es ordenar los intervalos por su tiempo de fin (end).
# Esto nos permite ir tomando siempre el intervalo que termina
# mas pronto, dejando el mayor espacio posible para los que siguen.
# Si el siguiente intervalo empieza antes de que termine el anterior,
# hay solapamiento y lo eliminamos. Si no, lo conservamos y
# actualizamos hasta donde llegamos.

# JUSTIFICACION:
# En clase vimos que para maximizar intervalos no solapados,
# la estrategia es ordenar por end y ser greedy: quedarse con
# el que termina antes. Este problema es exactamente el complemento:
# en vez de contar cuantos conservamos, contamos cuantos eliminamos.
# La logica es la misma, solo cambia lo que reportamos al final.
# Si de n intervalos conservamos k, entonces eliminamos n - k.
# En el codigo lo hacemos directamente contando los solapamientos.

# REGLA DE DECISION EN CADA PASO:
# Si interval[start] < ultimo_fin → se solapa → eliminar (count += 1)
# Si interval[start] >= ultimo_fin → no se solapa → conservar

# COMPLEJIDAD:
# Tiempo O(n log n), el ordenamiento domina. El recorrido es O(n).
# Espacio O(1), solo usamos dos variables auxiliares sin importar
# el tamaño de la entrada.

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Ordenar por tiempo de fin
        intervals.sort(key=lambda x: x[1])

        count      = 0
        ultimo_fin = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < ultimo_fin:
                # Se solapa con el ultimo conservado → eliminar
                count += 1
            else:
                # No se solapa → conservar y mover el limite
                ultimo_fin = intervals[i][1]

        return count