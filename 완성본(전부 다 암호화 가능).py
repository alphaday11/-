plainText = input("암호를 입력하세요 : ")
plainText_s = ""
plainText2 = ""

c = ''
ac = 0
for i in range(len(plainText)) :
    c = plainText[i]
    ac = ord(c)
    ac += 2
    c = chr(ac)
    plainText_s += c
    
print("암호문 : %s" %plainText_s)

for i in range(len(plainText_s)):
    c = plainText_s[i]
    ac = ord(c)
    ac -= 2
    c = chr(ac)
    plainText2 += c

print("복호문 : %s" %plainText2)
