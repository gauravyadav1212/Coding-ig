#Normal rectangle:

for i in range(0,5):
    print('*'*5)

#Rectange pyramid:
print('/n')
for i in range(1,6):
    print('*'*i)

#Hollow Square:
print('\n')
n = 5
for i in range(0,n):
    if i == 0 or i == n-1:
        print('*'*n)
    else:
        print('*' + ' '*(n-2) + '*')

#Full Pyramid:
print('\n')
n = 5
for i in range(0,n):
    print(' '*(n-i-1)+'*'+'*'*(2*i))

#Diamond Pattern:
    
print('\n')
n = 5
for i in range(0,n):
    print(' '*(n-i-1)+'*'+'*'*(2*i))
for i in range(n-2,-1,-1):
    print(' '*(n-i-1)+'*'+'*'*(2*i))

#Hollow Triange:
print('\n')
n = 5
print('*')
for i in range(0,n):
    if i == n-1:
        print('*'*n)
    else:
        if i != 0:
            print('*'+' '*(i-1)+'*')

#Half Diamond:
print('\n')
n = 5
for i in range(1,n+1):
    print('*'*i)

for i in range(n-1,-1,-1):
    print('*'*i)

#Number Pyramid:
print('\n')
n = 4
for i in range(0,n):
    x = i+1
    x = str(x)
    print(' '*(n-i)+x+x*(2*i))

#Butterfly Pattern:
print('\n')
n = 4
for i in range(0,n):
    print('*'*(i+1)+' '*(2*(n-i))+'*'*(i+1))
for i in range(n-1,-1,-1):
    print('*'*(i+1)+' '*(2*(n-i))+'*'*(i+1))
