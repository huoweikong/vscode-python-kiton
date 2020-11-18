
# path_input = r"F:\docu\multifas\bidui8_1.FAS"
# path_output=r"F:\docu\multifas\bidui8_1_single.FAS"
  
def guifan_fas_single(path_input,path_output):  
    fr=open(path_input, 'r')
    fw=open(path_output, 'w')
    seq={}
    for line in fr:
        if line.startswith('>'):    #判断字符串是否以‘>开始’
            name=line.split()[0]    #以空格为分隔符，并取序列为0的项。
            seq[name]=''
        else:
            seq[name]+=line.replace('\n', '')
    fr.close()                           

    for i in seq.keys():
        fw.write(i)
        fw.write('\n')
        fw.write(seq[i])
        fw.write('\n')
    fr.close()


print('-----欢迎使用单行规范化Fas序列程序-----')

# path1 = input("请输入原Fas地址")
# path1.replace('\\', '\\\\')
# path1.replace('\'', '')
# print(path1)
# print(type(path1))
# path2 = ''.join([path1[:-4], '_single.fas'])
# path2.replace('\"', '')
# print(path2)
# print(type(path2))

path1 = r"F:\docu\multifas\123.fas"
path2 = r"F:\docu\multifas\123_single.fas"
guifan_fas_single(path1, path2)

# "F:\docu\multifas\bidui8_pro.FAS"