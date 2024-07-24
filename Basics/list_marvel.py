Hero = ['spiderman', 'thor', 'hulk','iron man', 'captain america']
print('Length of the list is ', len(Hero))
Hero.append('black panther')
print(Hero)
Hero.remove('black panther')
Hero.insert(3,'black panther')
Hero[1:3] = ['doctor strange']
print(Hero)
print(sorted(Hero))
