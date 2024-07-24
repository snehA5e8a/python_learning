import json
db = {} # starting a dict named db
db['sneha'] = {
    'name': 'sneha',
    'address': 'painel',
    'blood group': 'O-ve'
}
db['aiden'] = {
    'name': 'aiden',
    'address': 'chundans',
    'blood group': 'A+ve'
}
db['Jino'] = {
    'name': 'Jino',
    'address': 'Kotte',
    'blood group': 'O+ve'
}
print('Initial dict file: \n', db)
dbs = json.dumps(db) # dict file to json string
print('JSON of dict: \n', dbs)
print('\n Data type of dict changed to s json: ', type(dbs))
# Opening text file to write dbs
with open('C://Users//91974//Dropbox//My PC (LAPTOP-8H6ILBDB)//Documents//dbs.txt', 'w') as f:
    f.write(dbs)

# File saved in c/doc, that file is being read and stored to string variable s

f1 = open('C://Users//91974//Dropbox//My PC (LAPTOP-8H6ILBDB)//Documents//dbs.txt', 'r')
s = f1.read()
print('JSON TEXT to variable:\n', s)
print('Data type of json text to variable is', type(s))

# The first JSON file is loaded as a dictionary data type

db_dict = json.loads(dbs)
print('\n First dict same as the JSON loaded dict: ', db==db_dict)
print('\n', db_dict)
print('Type of the above:', type(db_dict))
print(db_dict['sneha'])
print(db_dict['Jino']['blood group'])
print('\nDICTIONARY DATA PRINTED USING FOR LOOP')
for person in db_dict:
    print(db_dict[person])
