def centToEuroString(valore_cent: int)->str:
    centesimi = valore_cent % 100
    if valore_cent >= 100:
        euro = int((valore_cent - centesimi) / 100)
    else:
        euro = 0
    return '{euro}.{cent}€'.format(euro=euro, cent=centesimi)
