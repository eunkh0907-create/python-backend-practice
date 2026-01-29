def signup(users):

    while True:
        user_id = input("아이디: ")

        duplicate = False
        for user in users:
            if user["id"] == user_id:
                duplicate = True
                break

        if duplicate:
            print("이미 존재하는 아이디 입니다. 다시 입력하세요.")
        else:
            break

    user_pw = input("비밀번호: ")

    user = {
        "id" : user_id,
        "pw" : user_pw
    }
    users.append(user)

    print("회원가입 완료")

def login(users):

    login_id = input("아이디 입력: ")
    login_pw = input("비밀번호 입력: ")

    id_found = False

    for user in users:
        if user["id"] == login_id:
            id_found = True
            if user["pw"] == login_pw:
                print("로그인 성공")
                return
            else:
                print("비밀번호 오류")
                return
    if not id_found:
        print("존재하지 않는 아이디")

users = []

while True:
    print("\n1. 회원가입")
    print("2. 로그인")
    print("3. 종료")

    action = input("작업 선택:")

    if action == "1":
        signup(users)
    elif action == "2":
        login(users)
    elif action == "3":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력")

