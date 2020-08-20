# 튜플
# 변경되지 않는 목록
# 속도가 리스트보다 빠르다.
# 괄호를 쓴다.
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 오류가 뜬다

# name = "김종국"
# age = 20
# hobby = "코딩"

# print(name,age,hobby)

(name , age , hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)