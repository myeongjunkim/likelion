
INPUT_MONEY = "> 구입 금액을 입력해 주세요\n"
INPUT_WIN = "\n> 지난주 당첨번호를 입력해주세요\n"
STR_ERROR = "> 숫자를 입력해주세요\n"
ZERO_ERROR = "> 로또의 최소 가격은 1000원 입니다\n"
CNT_ERROR = "> 로또는 6개의 숫자로 이루어집니다\n"
RANGE_ERROR = "> 1~45까지의 숫자를 입력해주세요\n"
OVERAP_ERROR = "> 중복된 숫자를 입력하실 수 없습니다\n"


def times():
    
    flag = 1
    while flag:
        str = input(INPUT_MONEY)
        try:
            price = int(str)
            if price == 0:
                print(ZERO_ERROR)
                flag = 1
            else: flag = 0

        except ValueError:
            print(STR_ERROR)

    return int(price/1000)


def win():
    
    flag = 1
    while flag:
        str = input(INPUT_WIN)
        win_num = list(map(int, str.split(',')))

        cnt = 0
        for i in win_num:
            cnt += 1
            if i>45:
                print(RANGE_ERROR)
                flag = 1
                break
            else : flag = 0
            for j in range(cnt,len(win_num)-1):
                if i == win_num[j]:
                    print(OVERAP_ERROR)
                    flag = 1
                    break
                else : flag = 0
            if flag:
                break
        if len(win_num) != 6:
            print(CNT_ERROR)
            flag = 1

    return win_num


