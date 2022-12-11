f=open("Input.txt", "w")
f.write("Hello welcome to class/n Welcome/n Bye")
f.close()
fin=open("Input.txt" , "r+")
charCount = wordCount = lineCount = 0
for line in fin:
    lineCount +=1
    wordCount += len(line.split())
    charCount += len(line)
print("Line Count = ", lineCount)
print("Word COunt = ", wordCount)
print("Char Count = ", charCount)
