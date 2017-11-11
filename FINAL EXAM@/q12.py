from sys import argv

script, f1, f2  = argv

file1 = open(f1, 'r')
file2 = open(f2, 'r')

read1 = file1.read()
read2 = file2.read()
app = read1 + read2
file1.close()
file2.close()
file2 = open(f2, 'w')
write = file2.write(app)
file2.close()

print("operation completed, please view your files")
