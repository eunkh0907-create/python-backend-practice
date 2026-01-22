# Day 1: 입력 -> 처리 -> 출력

name = input("이름을 입력하세요: ")
birth_year_str = input("태어난 연도(예:2000): ")
birth_year = int(birth_year_str)

this_year = 2026
age = this_year - birth_year

print("----- 결과 -----")
print("이름: ", name)
print("올해 기준 나이: ", age)
print("10년 뒤 나이: ", age + 10)
