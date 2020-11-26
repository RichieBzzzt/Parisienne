import sys
print(sys.argv)
fin = open("packagetokenised.json", "rt")
fout = open("package.json", "wt")
for line in fin:
  fout.write(line.replace('<<version_number>>', sys.argv[1]))
fin.close()
fout.close()