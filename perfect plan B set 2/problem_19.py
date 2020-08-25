read_file=open("file.txt","r")
write_file=open("text.txt","w")
var=read_file.readlines()
for i in var:
    if var.index(i)%2==0:
        write_file.write(i)
