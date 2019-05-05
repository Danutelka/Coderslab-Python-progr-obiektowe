import re

def check_dice(dice):
    if re.match(r"[\d]*[dD][\d]([+-][\d]+){,1}", dice):
        return True
    else:
        return False



print(check_dice("9d7+10")) #- zwraca True

print(check_dice("9s7+10")) #- zwraca False

print(check_dice("9D7+10 abcdefghijk")) # - zwraca True

print(check_dice("9d-h")) #- zwraca False