import re

fname = input('Enter the file name:')
try:
    fhandle = open(fname)
except:
    print('invalid file')
    quit()

count = 0
tmp = list()
for lines in fhandle:
    x = re.findall('([0-9]+)', lines)
    for n in x:
        tmp.append(int(n))
        count = count + 1

print(count)
print(sum(tmp))
