import subprocess

sub=subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)

sub.wait()

print (sub.read())