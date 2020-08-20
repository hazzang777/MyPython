# 기본값
# 줄바꿈할때 역슬래쉬 하고 엔터 
# def profile(name,age,main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
#         .format(name,age,main_lang))

# profile("유재석",20,"python")
# profile("김태호",25,"java")

# 같은 학교 같은 학년 같은 반 같은 수업.
# 이럴떄 기본값을 사용한다.

# 전달 받지 않을떄는 기본으로 17과 파이썬을 넣고 전달하면 값 변경
def profile(name,age=17,main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
        .format(name,age,main_lang))

profile("유재석")
profile("김태호")        