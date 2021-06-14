def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def get_private_key(e, tot):
    k=1
    while (e*k)%tot != 1 or k == e:
        k+=1
    return k

def get_public_key(tot):
    e=2
    while e<totient and gcd(e, totient)!=1:
        e += 1
    return e

m = input("변환 할 문자열을 입력:")

# 두개의 소수 설정
p = 1117
q = 1123

print("Two prime numbers(p and q) are:", str(p), "and", str(q))

# 두 소수의 계수 구하기
n = p*q
print("n(p*q)=", str(p), "*", str(q), "=", str(n))

# 피함수 값 totient 구하기
totient = (p-1)*(q-1)
print("(p-1)*(q-1)=", str(totient))

# 공개키
e = get_public_key(totient)
print("공개키 (n, e):("+str(n)+","+str(e)+")")

# 개인키
d = get_private_key(e, totient)
print("개인키 (n, d):("+str(n)+","+str(d)+")")


encrypted_msg = encrypt((e,n), m)
print('암호화된 메세지 :', ''.join(map(lambda x: str(x), encrypted_msg)))


print('복호화된 메세지 :', decrypt((d,n),encrypted_msg))
