# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    # TU CÓDIGO AQUÍ
    distcms= gap_pillars*100
    distotal = (num_pillars - 1) * distcms

    inter_distance = distotal-(2*pillar_width)


    return inter_distance


if __name__ == '__main__':
    run(10, 5, 30)