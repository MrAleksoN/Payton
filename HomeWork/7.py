n = 1234
result = 1
m = n % 10
while( m > 0 )
result = result * n
n = n / 10
m = n % 10
print( result ) 