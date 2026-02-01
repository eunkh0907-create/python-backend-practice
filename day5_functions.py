import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "user.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

def load_users():
    ensure_data_dir()

    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            f.write("[]")
        return []
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return[]
    except json.JSONDecodeError:
        return []
    
def save_users(users):
    ensure_data_dir()
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

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
    save_users(users)
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

users = load_users()
print(f"저장된 사용자 수: {len(users)}명")

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

