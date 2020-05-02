score = input("Enter Score: ")

try:
    x = float(score)
except:
    print('Enter a proper score')

if x < 0.6 :
    print('F')
elif x < 0.7 :
    print('D')
elif x < 0.8 :
    print('C')
elif x < 0.9 :
    print('B')
elif x <= 1.0 :
    print('A')
else :
    print('Out of range')
