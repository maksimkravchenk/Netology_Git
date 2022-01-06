import sys
from transliterate import translit, get_available_language_codes

#i = 0
for line in sys.stdin:
    line = line.strip().split(',')
    line = translit(line[0], 'ru', reversed=True)
    line = line.split(' ')
    for j in range(len(line)):
        print(f'{line[j]},1')
 #   i += 1
 #   if i > 10: break
