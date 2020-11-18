path = r"F:\docu\multifas\123_single.fas"

f=open(path)
ls=[]
for line in f:
        if not line.startswith('>'):
                ls.append(line.replace('\n','')) #去掉行尾的换行符真的很重要！  
f.close()
# print(ls) #多序列 列表 ***

    
print("-----------------------------fdsfsdfsf--------------------------")



site_n = [[] for i in range(567)]    #创建一个3行5列的二维数组
for j in range(len(ls[1])):
    for i in range(len(ls)):
        site_n[j-1].append(ls[i-1][j-1])
        print(ls[i-1][j-1],end=" ")


print(len(site_n))

with open(r"F:\docu\multifas\123_single.txt",'w') as f:
    for i in site_n:
        print(i)
        len(set(i))
        print(len(list(set(i))))
        if len(list(set(i))) > 1:
            f.write(str(site_n.index(i))+'\t')
            f.write('  '.join(i)+'\n\n')