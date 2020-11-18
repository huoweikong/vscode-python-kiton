

path2 = r'D:\docu\H1N1G4_single_list.txt'
f = open(path2,'r')
eachc = f.read()
#print(eachc)
eachc = list(eachc)
print(type(eachc))
d = eachc[1]
print(d)