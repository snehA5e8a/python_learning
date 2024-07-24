with open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\stocks.csv', 'r') as s, open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\stock_out.csv', 'w') as out:
    out.write('Company Name, PE ratio, PB ratio\n')
    next(s)
    for line in s:
        items = line.split(',')
        stock = items[0]
        pe = float(items[1])/float(items[2])
        pb = float(items[1])/float(items[3])
        out.write(f'{stock},{pe},{pb}\n')
