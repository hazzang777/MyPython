# 사전
# key/value 쌍
cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3]) # key값을 넣어준다.
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) # cabinet에 5라는 key가 없기떄문에 오류발생시키고 바로 프로그램종료
# print(cabinet.get(5)) # none을 발생시키고 프로그램 지속시킨다.
# print(cabinet.get(5,"사용가능"))
# print("hi")

# 사전자료형안에 값을 확인하는법
# key in 변수
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 손님 등장
print(cabinet)
# cabinet에 C-20 이라는 key를 만들고 조세호라는 value를 넣는다.
cabinet["C-20"] = "조세호"
print(cabinet)

# 기존의 값에 수행하면 UPDATE 된다.
cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력ㄴ
print(cabinet.values())

# 쌍으로 출력
print(cabinet.items())

# 목욕탕 영업 종료
cabinet.clear()
print(cabinet)