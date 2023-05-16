import random
import os


def encode(parameter):
    randString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{}]|:;.>,<?/'
    if len(parameter) == 1:
        print('Message size at least two')
    elif len(parameter) > 1:
        a = ''
        if len(parameter) == 2:
            i = 2
            while i > 0:
                a = a + parameter[i - 1]
                i -= 1
            parameter = a
            length = 3
            while length > 0:
                first = random.choice(randString)
                last = random.choice(randString)
                parameter = first + parameter + last
                length -= 1

        elif len(parameter) >= 3:
            size1 = len(parameter) // 2
            size2 = len(parameter) - size1
            split1 = parameter[:size1]
            split2 = parameter[size1:]
            rev1, rev2 = '', ''
            first, middle, last = '', '', ''

            while size1 > 0:
                first += random.choice(randString)
                middle += random.choice(randString)
                last += random.choice(randString)
                rev1 += split1[size1 - 1]
                size1 -= 1

            while size2 > 0:
                rev2 += split2[size2 - 1]
                size2 -= 1

            parameter = first + rev1 + middle + rev2 + last

    try:
        os.mkdir('Encrypted Messages')
    except:
        if not os.path.exists('Encrypted Messages/encodedMsg.txt'):
            open('Encrypted Messages/encodedMsg.txt', 'x')
        with open('Encrypted Messages/encodedMsg.txt', 'a') as w:
            w.write(parameter + '\n')

    print('Operation successful')


def decode():
    with open('Encrypted Messages/encodedMsg.txt', 'r') as r:
        msg = r.read()
        msgList = msg.split('\n')
        newList = msgList[:-1]
        i = 0
        while i < len(newList):
            if len(msgList[i]) == 8:
                val = msgList[i]
                msg = val[3:5:1]
                rev = ''
                j = len(msg)
                while j > 0:
                    rev += msg[j-1]
                    j -= 1

                if not os.path.exists('Decrypted Messages'):
                    os.mkdir('Decrypted Messages')
                    open('Decrypted Messages/decodedMsg.txt', 'x')
                    with open('Decrypted Messages/decodedMsg.txt', 'a') as w:
                        w.write(rev + '\n')
                else:
                    with open('Decrypted Messages/decodedMsg.txt', 'a') as w:
                        w.write(rev + '\n')

            elif len(msgList[i]) > 8:
                a = len(msgList[i]) // 5
                msg = msgList[i]
                revp1, revp2 = '', ''
                forp1, forp2 = '', ''
                if len(msgList[i]) % 5 == 1: #if splitted message size not same then go inside
                    revp1 += msg[a:a+a]
                    revp2 += msg[-(a+a+1):-a]
                    # print('inside if block = ', p1, p2)
                else:
                    revp1 += msg[a:a+a]
                    revp2 += msg[-(a+a):-a]
                    # print('Inside else block = ', p1, p2)

                j = len(revp1)
                while j > 0:
                    forp1 += revp1[j-1]
                    j -= 1

                k = len(revp2)
                while k > 0:
                    forp2 += revp2[k-1]
                    k -= 1

                if not os.path.exists('Decrypted Messages'):
                    os.mkdir('Decrypted Messages')
                    open('Decrypted Messages/decodedMsg.txt', 'x')
                    with open('Decrypted Messages/decodedMsg.txt', 'a') as w:
                        w.write(forp1 + forp2 + '\n')

                else:
                    with open('Decrypted Messages/decodedMsg.txt', 'a') as w:
                        w.write(forp1 + forp2 + '\n')

            i += 1
        print('Operation successful')


print('Welcome to SECRET CODE generator'.center(50))
print('*' * 50)

while True:
    print('1. Encode')
    print('2. Decode')
    print('3. Exit')
    userInput = input('Enter your desired Option : ')
    if userInput == '1':
        add = input('Write your message here : ')
        encode(add)
    elif userInput == '2':
        decode()
    elif userInput == '3':
        break
