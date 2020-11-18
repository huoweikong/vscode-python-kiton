
path = r"F:\docu\multifas\123_single.fas"


# multi transfer to list
f=open(path)
ls=[]
for line in f:
        if not line.startswith('>'):
                ls.append(line.replace('\n','')) #去掉行尾的换行符真的很重要！  
f.close()
# print(ls) #多序列 --> 列表 ***

    
print("-----------------------------split line--------------------------")



# Create a two-dimensional array of 567 rows (can only keep the last one-dimensional unknown)
# Because the amino acids sequnces length is 567
site_n = [[] for i in range(567)]    
for j in range(len(ls[1])):
    for i in range(len(ls)):
        site_n[j-1].append(ls[i-1][j-1])    # Equivilent to converting rows and colums
        print(ls[i-1][j-1],end=" ")


print('len(site_n) is : ', len(site_n))

# Scan site by site, if the amino acids of all sequences at the site are the same, no processing will be done, otherwise, it will be extracted
# Saving the qualified results to a file
with open(r"F:\docu\multifas\123_single.txt",'w') as f:
    for i in site_n:
        print(i)
        len(set(i))
        print(len(list(set(i))))
        if len(list(set(i))) > 1:
            f.write(str(site_n.index(i))+'\t')
            f.write('\t'.join(i)+'\n')