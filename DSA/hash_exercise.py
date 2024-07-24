with open('nyc_weather.csv', 'r') as f:
    next(f)
    weather = {}
    for line in f:
        wea = line.split(',')
        weather[wea[0]] = int(wea[1])
    print(weather)

    print('temp of Jan 9: ', weather['Jan 9'])
    print('temp of Jan 4: ', weather['Jan 4'])

with open('nyc_weather.csv', 'r') as f:
    weather = []
    next(f) #skipping header
    for line in f:
        wea = line.split(',')
        weather.append(int(wea[1]))
    print(weather)
    temp = 0
    for i in range(7):
        temp += weather[i]
    avg = temp/7
    print('average temp of first week: ', avg)
    print('Max weather in first 10 days: ', max(weather))

with open('poem for hash.txt','r') as f:
    word_count = {}
    for line in f:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n', '')
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    print(word_count)
