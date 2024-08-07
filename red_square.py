# ****************
# EL CUADRADO ROJO
# ****************

import math
def run(arc_A: float) -> float:
    # TU CÓDIGO AQUÍ
    PI=3.14
    radio=arc_A/(2*PI)
    diagonal=2*radio
    lado = diagonal/(2**0.5)
    area = lado * lado

    return round(area,10)


if __name__ == '__main__':
    run(1)