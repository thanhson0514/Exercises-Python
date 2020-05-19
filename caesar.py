string = input('Input string:')
print('Step: 0 < d < 26')
d = int(input('Input step:'))

if d <= 0 or d >= 26:
    print('Step must be from 0 to 26')
elif not string.isupper():
    print('string must be uppercase')
else:
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'*2
    # alphabet = alphabet.upper()
    alphabet = ''
    for i in range(26):
        alphabet += chr(ord('A') + i)

    alphabet *= 2
    st = ''
    
    for i in range(len(string)):
        index = alphabet.index(string[i])
        index += d
        st += alphabet[index]

    print('encode:', st)