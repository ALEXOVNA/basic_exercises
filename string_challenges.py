# Вывести последнюю букву в слове
word = 'Архангельск'.lower()
lst = []
count = 0
for i in range(len(word)):
    lst.append(word[i])
end_s = lst[-1]
print(f'end_s: {end_s}')

# Вывести количество букв "а" в слове
for i in range(len(word)):
  j = lst[i]
  if j == 'а':
    count += 1
print(f'count: {count}')


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
glas_lst = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'я']
count_glas = 0

for glas in glas_lst:
    for i in word:
        if glas == i:
            count_glas +=1
print(f'count_glas: {count_glas}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence_word_list = sentence.split()
count_word = len(sentence_word_list)
print(count_word)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
first_symbol = []
for cw in range(len(sentence_word_list)):
    first_symbol.append(sentence_word_list[cw][0])
    print(first_symbol[cw])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
average_len_of_word = 0
sum_len_of_word = 0
for word in range(count_word):
    sum_len_of_word += len(sentence_word_list[word])
average_len_of_word = sum_len_of_word/count_word


print(f'average_len_of_word: {average_len_of_word}')