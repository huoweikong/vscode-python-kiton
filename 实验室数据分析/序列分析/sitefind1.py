seq=open(r"F:\docu\h1n1-bidui-kiton2.fas")  #输入文件路径,该文件格式要求为序列名称占一行，序列只占一行的fasta格式序列。
out=open(r"F:\docu\h1n1-bidui-kiton2-out2.fas","w")     #输出文件路径
a=[]  #建立一个空的列表a
for line in seq:
    line=line.strip()
    a.append(line)   #把输入文件里的每一行都存入到列表a中，一行即一个元素
s=""
for n in range(len(a)): #len表示长度，对于列表a而言，len(a)表示列表a里元素的数目
    s=a[n]  #把每一个元素（相当于输入文件里的每一行）的值赋给s
    if n % 2 == 1:   #判断是否是第偶数行
        if s[i-1:i]=="M": #判断对齐后的第i个位点,具体i值依据实际情况来定
            out.write(a[n-1]+"\n"+s+"\n")
        
seq.close()
out.close()