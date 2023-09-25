"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
def kg_a_gr(kg):
    gr= kg*1000
    return gr
def kg_a_ton(kg):
    ton = kg/1000
    return ton
def  gr_a_kg(gr):
    kg= gr/1000
    return kg
def gr_a_ton(gr):
    ton= gr/1000000
    return ton
def ton_a_kg(ton):
    kg= ton*1000
    return kg
def ton_a_gr(ton):
    gr= ton*1000000
    return gr



if __name__ == "__main__":
    print("Ejemplos de conversión de masa:")
    print("12 kilogramos a gramos:", kg_a_gr(12))
    print("25000 kilogramos a toneladas:", kg_a_ton(25000))
    print("12000 gramos a kilogramos", gr_a_kg(12000))
    print("200000 gramos a toneladas:", gr_a_ton(200000))
    print("3 toneladas a kilogramos:", ton_a_kg(3))
    print("2 toneladas a gramos:", ton_a_gr(2))



    