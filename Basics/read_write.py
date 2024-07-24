f = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\first.txt', 'w')
f.write('Hello, How are you?')
f = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\first.txt', 'a')
f.write('\nThis is the next line added')
f.close()

p = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\text added.txt', 'r')
print('Whole text in the file:\n', p.read())
print('Line by line content in file by for loop\n')
p = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\text added.txt', 'r')
for line in p:
    print(line)
p = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\text added.txt', 'r')
word = 0
p_out = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\wordcount.txt', 'w')
for line in p:
    sep = line.split(' ')
    print(str(sep))
    p_out.write('word count: '+ str(len(sep))+' '+line)
    word = word+ len(sep)
print('The count of words in text is:', word)
p.close()
p_out.close()
with open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\wordcount.txt', 'r') as f1:
    print(f1.read())
print('Word count file closed?:' f1.closed)

