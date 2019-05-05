import re

text_to_search = open('text.txt').read()

result = re.findall(r"autor", text_to_search)
print(result)

result2 = re.findall(r"[\d]+%", text_to_search)
print(result2)

result3 = re.findall(r"[\w]+\.", text_to_search)
print(result3)

result4 = re.findall(r"polski", text_to_search, re.I)
print(result4)