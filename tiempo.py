"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
def sec_a_min(sec):
    min= sec/60
    return min
def sec_a_hr(sec):
    hr= sec/3600
    return hr
def min_a_sec(min):
    sec= min*60
    return sec
def min_a_hr(min):
    hr= min/60
    return hr
def hr_a_sec(hr):
    sec= hr*3600
    return sec
def hr_a_min(hr):
    min= hr*60
    return min

if  __name__ == "__main__":
    print("Ejemplos de conversión de masa:")
    print("12 kilogramos a gramos:", sec_a_min(500))
    print("25000 kilogramos a toneladas:", sec_a_hr(10000))
    print("12000 gramos a kilogramos", min_a_sec(12))
    print("200000 gramos a toneladas:", min_a_hr(230))
    print("3 toneladas a kilogramos:", hr_a_sec(3))
    print("2 toneladas a gramos:", hr_a_min(2))