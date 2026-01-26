users = []

for i in range(3):
    user = input("아이디 입력: ")
    users.append(user)

login_id = input("아이디 입력: ")

if login_id in users:
    print("로그인 성공")
else:
    print("존재하지 않는 아이디")

for user in users:
    print(user)