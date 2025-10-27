import math

class Cuantitativos:
    """
    Calcula estadísticas descriptivas para variables cuantitativas
    utilizando únicamente Lógica Pura (bucles primitivos).
    
    """

    def __init__(self, data: list):
        """
        El constructor de la clase.
        Prepara los datos y pre-calcula la media.
        """
        # 1. Limpieza y orden de los datos
        self.datos = sorted([num for num in data if isinstance(num, (int, float))])
        
        if not self.datos:
            raise ValueError("La lista no contiene datos numéricos válidos.")
            
        self.n = len(self.datos)
        
        # 2. Pre-cálculo de la Media 
        suma_total = 0
        for num in self.datos:
            suma_total += num
        
        # Guardamos la media calculada
        self.media_calculada = suma_total / self.n

    # --- Media ---
    def calcular_media(self):
        """
        Devuelve la media (promedio) de los datos.
        """
        return self.media_calculada

    # --- Tarea 2: Mediana ---
    def calcular_mediana(self):
        """
        Calcula la mediana 
        """
        if self.n % 2 == 1:
            # Impar
            indice = self.n // 2
            return self.datos[indice]
        else:
            # Par
            indice_sup = self.n // 2
            indice_inf = indice_sup - 1
            return (self.datos[indice_inf] + self.datos[indice_sup]) / 2

    # --- Varianza ---
    def calcular_varianza(self, es_muestra: bool = True):
        """
        Calcula la varianza usando la fórmula 
        """
        media = self.media_calculada
        
        suma_diferencias_sq = 0
        for x in self.datos:
            suma_diferencias_sq += (x - media) ** 2
        
        if es_muestra and self.n > 1:
            denominador = self.n - 1 # Muestral
        else:
            denominador = self.n # Poblacional
            
        return suma_diferencias_sq / denominador

    # --- Desviación Estándar ---
    def calcular_desviacion_estandar(self, es_muestra: bool = True):
        """
        Calcula la desviación estándar usando la Varianza y math.sqrt().
        """
        varianza = self.calcular_varianza(es_muestra=es_muestra)
        return math.sqrt(varianza)

    # --- Percentiles (Q1, Q3) ---
    def _calcular_percentil(self, p: float):
        """
        Función auxiliar para calcular percentiles 
        """
        posicion = (self.n - 1) * p
        k = int(posicion)
        d = posicion - k
        
        if d == 0:
            return self.datos[k]
        else:
            if k + 1 < self.n:
                return self.datos[k] + d * (self.datos[k+1] - self.datos[k])
            else:
                return self.datos[k]

    # --- Tarea 6: Rango Intercuartílico (IQR) ---
    def calcular_cuartiles_iqr(self):
        """
        Calcula Q1, Q3 y el IQR (Q3 - Q1).
        """
        q1 = self._calcular_percentil(0.25)
        q3 = self._calcular_percentil(0.75)
        iqr = q3 - q1
        
        return {
            "q1": q1,
            "q3": q3,
            "iqr": iqr
        }

