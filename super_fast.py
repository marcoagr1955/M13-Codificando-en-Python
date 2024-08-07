# **********************
# ANIMALES SUPER RÁPIDOS
# **********************


def run(speed_km_h: float) -> float:
    # TU CÓDIGO AQUÍ
    vms=speed_km_h*1000/3600

    speed_cm_s = vms*100

    return speed_cm_s


if __name__ == '__main__':
    run(1.08)