# Create collatz() function
def collatz(number) :
        if int(number)%2 == 0 :
            print ( int(number)//2 )
            return int(number)//2
        else:
            print( 3* int(number) + 1 )
            return 3 * int(number) + 1

# Launch Collatz sequence
print('Enter number:')
while True:
    try:
        number=int(input())
        break
    except ValueError:
        print('Enter a number.')
while int(number) > 1:
    number=collatz(number)
    print(number)
