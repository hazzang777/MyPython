# 전달값과 반환값
# 함수
# def 함수이름():
#   수행되는 내용
# 함수는 정의만 되지 실제로 호출하기 전까지는 아무것도 하지 않는다. 
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money


def withdraw(balance,money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance,money): # 저녁에 출금 수수료 붙는다.
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 튜플 형식으로 보낸다.
balance = 0 #잔액
balance = deposit(balance,1000)
# balance = withdraw(balance,2000)
# balance = withdraw(balance,500)
commission,balance = withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1} 원입니다.".format(commission,balance))