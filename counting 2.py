fin= open('Input.txt', 'r')
fout= open('counting2.txt', 'w')
for line in fin:
    fout.write(line)
fin.close()
fout.close()
fin= open('counting2.txt','r')
for line in fin:
    print(line,end="")

fin.close()
