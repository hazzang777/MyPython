# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 대문자가 맞는지
print(len(python)) # 길이
print(python.replace("Python","Java")) #문자열 교체

# 인덱스 알기
index = python.index("n")
print(index)
# 두번쨰 n찾기
index = python.index("n", index+1 )
print(index)

# 내가 원하는 값이 없으면 -1 반환
print(python.find("java"))
# 오류 
# print(python.index("java"))

# n이 몇번 등장하는가
print(python.count("n"))