# 랜덤 함수
from random import *

# 0과1 사이의 임의의 난수를 출력한다.
print(random())
print(random() * 10)
#정수형으로 보고싶을때 int()로 감싼다.
print(int(random()*10))
# 1부터 10이하의 임의의 값 생성
print(int(random()*10)+1)
# 로또번호 값 생성
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

# 더쉽게 사용 가능
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성