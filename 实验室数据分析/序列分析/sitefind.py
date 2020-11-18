#第一步，定义子函数panbieweidian
def panbieweidian (seqline,outline,i,aa):
    seq=open(seqline) 
    out=open(outline,"w")
    a=[]  
    for line in seq:
        line=line.strip()
        a.append(line)    
    s=""
    for n in range(len(a)): 
        s=a[n]  
        if n % 2 == 1:  
            if s[i-1:i]==aa: 
                out.write(a[n-1]+"\n"+s+"\n")
            
    seq.close()
    out.close()    
 
#第二步，调用子函数panbieweidian   
panbieweidian (r"F:\docu\h1n1-bidui-kiton2.fas",r"F:\docu\h1n1-bidui-kiton2_out1.fas",10,"M") #与定义的子函数里的参数一一对应即可
#上面为判断第10位是不是氨基酸M，以后只需在调用函数这里修改相应位点和氨基酸类型即可，而第一步的子函数部分不需要改动。

#注意，seq.fas该输入文件格式要求为序列名称占一行，序列只占一行。
#采用定义子函数的方法写代码后，对相关位点和氨基酸的判别进行修改比较方便，代码重复利用率高。