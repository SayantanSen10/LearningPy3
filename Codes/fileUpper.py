file = input('Enter a file name: ')
try:
    f = open(file)
except:
    print('Invalid file type')
    quit();
#using read
lines = f.read();
lines = lines.rstrip()
print(lines.upper())

#using for loop
#for lines in f:
    #lines = lines.rstrip()
    #print(lines.upper())
