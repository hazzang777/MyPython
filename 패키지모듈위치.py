# 패키지와 묘듈위치

# 패키지를 호출하는 동일한 폴더에 있거나
# 파이썬 내의 라이브러리들이 모여있는 폴더에 있어야 사용가능

# 위치 확인하는 방법
import inspect
import random


print(inspect.getfile(random))
from travel import *
print(inspect.getfile(thailand))