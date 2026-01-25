
user_id = input("아이디: ")
user_pw = input("비밀번호: ")

if user_id == "":
    print("아이디를 입력하세요.")
elif user_pw == "":
    print("패스워드를 입력하세요.")
elif user_id != "admin":
    print("아이디가 존재하지 않습니다.")
elif user_pw != "1234":
    print("패스워드가 틀렸습니다.")
else:
    print(user_id + "님 환영합니다.")
