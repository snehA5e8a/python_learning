import fileinput

with open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\poem.txt', 'r') as p:

    word_dict = {}
    for line in p:
        word = line.split(' ')
        for w in word:
            if w in word_dict:
                word_dict[w]+= 1
            else:
                word_dict[w] = 1
word_occurances = list(word_dict.values())
n = max(word_occurances)
print('Max occurance of any word is: ', n)
print('The most occured words are:\n')
for items in word_dict:
    if word_dict[items] == n:
        print(items)
