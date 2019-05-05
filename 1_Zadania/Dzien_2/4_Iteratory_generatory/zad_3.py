
def piosenka():
    yield "Wlazł kotek na płotek"
    yield "i mruga,"
    yield "ładna to piosenka,"
    yield "nie długa."
    yield "Nie długa, nie krótka,"
    yield "lecz w sam raz,"
    yield "zaśpiewaj koteczku,"
    yield "jeszcze raz."

for k in piosenka():
    print(k)