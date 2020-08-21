# 모듈
# 필요한것 끼리 부품처럼 잘 만들어진 파일이다.
# 파이썬에서 함수정의나 클래스 정의등 파이썬 문장들을 담고있는 파일을 모듈이라 한다.
# 모듈은 확장자가 .py 이다.

# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을때
# theater_module.price_solider(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv # 별칭을 줄수 있다.
# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)

# from theater_module import *
# # from random import *

# price(3)
# price_morning(4)
# price_solider(5)

# from theater_module import price,price_morning
# price(5)
# price_morning(6)

from theater_module import price_solider as price # 별칭 
price(5) # price_solider()랑 동일 