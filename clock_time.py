# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    # TU CÓDIGO AQUÍ
    milhours=hours*60*60*1000
    milmin=minutes*60*1000
    milsec=seconds*1000
    time_since_midnight =milhours+milmin+milsec

    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)