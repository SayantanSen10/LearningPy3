fname = input("Enter file name:")
try:
    handle = open(fname)
except:
    print('Invalid File')
    quit()

counts = dict()
tmp = list()
for lines in handle:
    if not lines.startswith('From '):
        continue
    words = lines.split()
    time = words[5].split(':')
    tmp.append(time[0])

for hour in tmp:
    counts[hour] = counts.get(hour, 0) + 1

#  FOR SORTING BY COUNTS(VALUE)
#hrs = list()
#for k,v in counts.items():
    #newTup = (v,k)
    #hrs.append(newTup)
#hrs = counts.items()
#hrs = sorted(hrs)

#print(hrs)

lst = sorted([(k,v) for k,v in counts.items()])

for (k, v) in lst:
    print(k, v)
