# mis_estadisticas/cualitativos.py

class Cualitativo:
    """Clase para cálculos de estadísticas cualitativas usando lógica pura."""
    
    def __init__(self):
        # Inicialización de la clase de cálculo cualitativo
        pass 

    def calcular_frecuencias_absolutas(self, datos):
        """
        Calcula la frecuencia absoluta usando lógica de diccionario y bucle for (Tarea 1/6).
        """
        frecuencias = {} 
        
        # Bucle para contar las ocurrencias (Lógica Pura)
        for elemento in datos:
            if elemento in frecuencias:
                frecuencias[elemento] += 1
            else:
                frecuencias[elemento] = 1
                
        return frecuencias