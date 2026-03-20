f = open("demofile.txt")
print(f.read())
f.close()


with open("demofile.txt") as f:
    print(f.read()) # Then you do not have to worry about closing your files, the with statement takes care of that.

f = open("demofile.txt")
print(f.readline())
f.close()


with open("demofile.txt") as f:
  print(f.read(5))


with open("demofile.txt") as f:
  print(f.readline())


with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())


with open("demofile.txt") as f:
  for x in f:
    print(x)