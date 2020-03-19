a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a%2==0 and b%2==0:
    r1=42
elif a%2!=0 and b%2!=0:
    r1=42
else:
    r1=13

if c%2==0 and d%2==0:
    r2=42
elif c%2!=0 and d%2!=0:
    r2=42
else:
    r2=13

if r1 == r2:
    print('OBA SU ISTE BOJE')
else:
    print('NISU ISTE BOJE')

# if a%2==0 and b%2==0:
#     print('CRNO')
# elif a%2!=0 and b%2!=0:
#     print('CRNO')
# else:
#     print('BIJELO')
