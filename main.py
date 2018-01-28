def main():
   menu = input('Do you wish to 1) encrypt or 2) decrypt? ')
   if menu == '1':
       encrypt()
   elif menu == '2':
       decrypt()
   else:
       print('Please enter either 1 or 2!')
       main()


def encrypt():
    value = input('Please enter the string you wish to encrypt: ')
    length = len(value)
    onetime = input('Please enter a one-time pad: ')

    if len(onetime) < length:
        print('Your one-time pad is too short.')
        encrypt()

    else:
        pos = 0
        result = ''
        for char in value:
            result += chr(ord(char) ^ ord(onetime[pos]))
            pos +=1
        f = open('result.txt', 'w')
        f.write(result)
        f.close()

def decrypt():
    onetime = input('Enter one-time pad: ')
    f = open('result.txt', 'r')
    encrypted = f.read()
    f.close()

    answer = ''
    pos = 0
    for char in encrypted:
        answer += chr(ord(char) ^ ord(onetime[pos]))
        pos +=1
    print(answer)
    
    

main()