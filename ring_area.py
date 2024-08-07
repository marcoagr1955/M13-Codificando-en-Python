# ***************
# ÁREA DEL ANILLO
# ***************


def run(z: float) -> float:
    # TU CÓDIGO AQUÍ
    PI=3.14
    radio= z/(2*PI)
    white_area=PI *(radio*radio)

    return white_area


if __name__ == '__main__':
    run(6)