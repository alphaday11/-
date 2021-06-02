passwd = input("암호를 입력하세요 : ")
passwd_s = ""
passwd2 = ""
print("입력한 암호는 [%s] 입니다. > 암호화를 진행하겠습니다." %passwd)
c = ''
ac = 0
for i in range(len(passwd)) :
    c = passwd[i]
    ac = ord(c)
    ac += 2
    c = chr(ac)
    passwd_s += c
    
print("암호화된 비밀번호 : %s" %passwd_s)
print("암호화된 비밀번호를 복화하겠습니다.")
for i in range(len(passwd_s)):
    c = passwd_s[i]
    ac = ord(c)
    ac -= 2
    c = chr(ac)
    passwd2 += c

if passwd == passwd2:
    print("복호화한 암호를 공개합니다. : %s" %passwd2)
    print("처음 입력했던 암호와, 복호화한 암호가 일치합니다.")