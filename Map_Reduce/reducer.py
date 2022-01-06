import sys

previous_word = None
word_count = 0

for line in sys.stdin:
    word, one = line.strip().split(',')
    one = int(one)
    if previous_word:
        if previous_word == word: 
            word_count += one
        else: 
            print(previous_word, word_count)
            previous_word = word
            word_count = one
    else:
        previous_word = word
        word_count = one
print(previous_word, word_count)
