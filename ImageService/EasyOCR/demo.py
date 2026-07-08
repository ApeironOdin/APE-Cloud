import easyocr
import sys

reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext("henpri1.png")

sys.stdout = open('output.txt', 'w', encoding='utf-8')

for it in result:
    print(it[1])

sys.stdout = sys.__stdout__