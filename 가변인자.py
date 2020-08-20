# 가변인자
# 매개변수의 개수를 유동적일때
# def profile(name,age, lang1,lang2,lang3,lang4,lang5):
#     print("이름:{0}\t나이:{1}\t".format(name,age), end=" ") # end=" " 해주면 줄바꿈X
#     print(lang1,lang2,lang3,lang4,lang5) 

def profile(name,age,*language):
    print("이름:{0}\t나이:{1}\t".format(name,age), end=" ") # end=" " 해주면 줄바꿈X
    for lang in language:
        print(lang, end=" ")
    print()    


profile("유재석",20,"python","java","c","c++","c#")
profile("김태호",25,"kotlin","swift")
    