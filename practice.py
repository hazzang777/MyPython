#숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자 자료형
print('풍선')
print("나비")
print("zzzzzzzzz")
print("ㅋ"*9) #문자와 숫자를 곱해서 반복 가능

#boolean(참 & 거짓)
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not(5>10))

#변수
# ex) 애완동물을 소개해 주세요~
print("우리집 강아지의 이름은 연탄입니다.")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 만약 이름이 바뀌면 다 바꿔야 하는 불상사가 일어난다 그렇기 때문에 변수를 사용한다.
# 변수란 값을 저장하는 공간을 의미한다.
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"입니다.")
hobby = "공놀이"
# print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요") #문자열사이에 정수형 넣을때 str(int)해줘야한다.
# ,로도 사용가능 이떄는 str 사용안해도 됨 그러나 무조건 공백 발생
print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult)) # 불리언 형도 마찬가지 이다.

# 이것은 주석입니다. 프로그램 실행시 무시한다.
''' 이렇게 하면
여러문장의 주석처리가 
됩니다. '''

# ctrl + / 은 주석 단축키 & 해제도 동일

# 퀴즈1
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

