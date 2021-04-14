LOTTO_RESULT = "\n> 로또 당첨 결과"


def lotto_printer(n,lotto_sum):
    print("> %d 장의 로또를 구입하셨습니다." % n)
    
    for i in range(n):
        print(lotto_sum[i])

    return


def rank_printer(rank_sum):
    
    print(LOTTO_RESULT)
    print("4등(3개가 맞을 때) - 5000원 - %d개" % rank_sum[3])
    print("3등(4개가 맞을 때) - 20000원 - %d개" % rank_sum[2])
    print("2등(5개가 맞을 때) - 100000원 - %d개" % rank_sum[1])
    print("1등(6개가 맞을 때) - 500000원 - %d개" % rank_sum[0])

    return

def profit_printer(profit):
    print("\n> 수익률")
    print("%d 배" % profit)
    return