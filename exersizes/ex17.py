from sys import argv
from os.path import exists


script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#   OPTIMIZE
indata= open (from_file)


print(f"the input file is {len(to_file)} bytes long")
print(f"does the output file exist? {exists(to_file)}")
print(f"ready, hit RETURN to continue,CTRL-C to abort.")
input()
out_file = open(to_file, 'a')
out_file.write(indata)
print("done")
out_file.close()
in_file.close()
