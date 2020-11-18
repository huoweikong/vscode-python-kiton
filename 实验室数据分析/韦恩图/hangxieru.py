import csv
 
datas = [['俄罗斯', '1707'],
         ['加拿大', 997],
         ['中国', 960],
        ['美国', '936']]
 
with open('country.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer  = csv.writer(csvfile)
    for row in datas:
        writer.writerow(row)