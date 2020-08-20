# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#     남자 : 키(m) X 키(m) x 22
#     여자 : 키(m) X 키(m) X 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#             * 함수명 : std_weight
#             * 전달값 : 키(height),성별(gender)
# 조건2 : 표준 체중은 소수점 둘째짜리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# from math import *

# def std_weight(h,g):
#     if g == "남자":
#         std = ((h//100)**2)*22
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(h,g,std))
#     else:
#         std = ((h//100)**2)*21
#          print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(h,g,std))

# std_weight(175,"남자")

# 위에거 틀림

# 답

def std_weight(height,gender): # 키 m단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21

height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))            
