data = 'xbox 360 | 250 | new'
data[:data.index('|')]
data[data.index('|') + 1 : data.index('|') + 5 ]
data[0:9]
data[::-1]
data[0:-1]
data[0:29:2]
data[0:29:3]
#better way than string indexing
data[data.find('|')+1:data.find('|',10)]
