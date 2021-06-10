def encipher(p, k): #암호화 함수 p:평문, k:몇 번을 뛸 건가
    c = '' #c: 암호문
    for i in range(len(p)): #평문의 길이만큼 반복
        a = ord(p[i]) #아스키 코드값 구하기
        if a == 32:
            a = 64
        t = a + k #k만큼 더해주기
        if t > 90: t -= 27
        if t == 64: t = 32
        c += chr(t)
    return c

def decipher(p, k): #복호화 함수
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: a = 91
        t = a - k #k만큼 빼주기
        if t < 65: t += 27
        if t == 91: t = 32
        c += chr(t)
    return c

plainText = input("암호화할 내용을 입력하시오.")
k = int(input("얼마만큼 띄어 쓸 지 입력하시오."))
print('평 문 : ', plainText)
cipherText = encipher(plainText, k)
print('암호문 : ', encipher(plainText, k))
print('복호문 : ', decipher(cipherText, k))