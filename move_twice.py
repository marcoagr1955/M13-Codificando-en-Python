# *******************
# TIRO PORQUE ME TOCA
# *******************


def run(current_pos: int, dice: int) -> int:
    # TU CÓDIGO AQUÍ
    desplaz=dice*2

    final_pos =current_pos+desplaz

    return final_pos


if __name__ == '__main__':
    run(3, 6)