import os
p=os.popen('dot -Tpdf allElectronicInformationGainOri.dot -o output1.pdf')


print (p.read())