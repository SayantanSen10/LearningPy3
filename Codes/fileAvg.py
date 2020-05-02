file = input('Enter a file name: ')
try:
    f = open(file)
except:
    print('Invalid file type', file)
    quit()

count = 0
a = 0
for lines in f:
    if not lines.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    tmp = float(lines[19:])
    for n in [0, tmp]:
        a = a + n
        avg = a / count

print('sum:', a)
print('Average spam confidence:', avg)
