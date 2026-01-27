users = []
for i in range(2):
    while True:
        user_id = input("아이디: ")

        duplicate = False
        for user in users:
            if user["id"] == user_id:
                duplicate = True
            break

        if duplicate:
            print("이미 존재하는 아이디입니다. 다시 입력하세요")
        else:
            break
    user_pw = input("비밀번호: ")

    user = {
        "id" : user_id,
        "pw" : user_pw
    }
    users.append(user)

    print("회원가입 완료")


    

login_id = input("아이디 입력: ")
login_pw = input("비밀번호 입력: ")

id_found = False
pw_correct = False

for user in users:
    if user["id"] == login_id:
        id_found = True
        if user["pw"] == login_pw:
            pw_correct = True
        break

if pw_correct:
    print("로그인 성공")
elif id_found:
    print("비밀번호 오류")
else:
    print("존재하지 않는 아이디")