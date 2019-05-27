# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
def countChars(chars, word):
    n = 0
    for char in word.lower():
        if char in chars:
            n += 1
    return print(n)
chars = 'аеёиоуыюя'
countChars(chars, word)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
list_words = len(sentence.split(' '))
print(list_words)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence:
    print(i)


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
l_word = sentence.split(' ')
len_words = 0
for word in l_word:
    len_words += len(word) 
avg_word = len_words / len(l_word)
print(avg_word)

