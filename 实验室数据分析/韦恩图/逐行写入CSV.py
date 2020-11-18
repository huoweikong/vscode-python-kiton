
import csv
 
list = ['abc', 'def' , 'ghi']
with open("CVE.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file ,delimiter=',')
        writer.writerow(list)