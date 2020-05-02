file = input("File name: ")
try:
    handle = open(file)
except:
    print("Invalid file")
    quit()
lst = list()
#nake a list consisting email addresses
for lines in handle:
    if not lines.startswith('From '):
        continue
    words = lines.split()
    lst.append(words[1])

counts = dict()
#counts every word
for word in lst:
    counts[word] = counts.get(word, 0) + 1

maxWord = None
maxCount = None

#finds the max count
for word,count in counts.items():
    if maxCount is None or maxCount < count:
        maxWord = word
        maxCount = count

print(maxWord, maxCount)
