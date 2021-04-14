def run():
    
    from ui import input_view
    from lotto import lotto
    from ui import printer
    from lotto_statistics import lotto_statistics
    from lotto_statistics import profit

    # 몇개 살지 돈 입력
    times = input_view.times()
    
    # 해당 개수만큼 구매하여 번호 저장 및 출력
    lotto_sum = lotto.lotto_maker(times)
    printer.lotto_printer(times,lotto_sum)

    # 정답 입력
    win = input_view.win()

    # 결과 기록
    rank_sum = lotto_statistics.check(lotto_sum, win)

    # 결과 출력
    printer.rank_printer(rank_sum)

    # 수익률 계산
    profit = profit.profit(rank_sum, times)

    #수익률 출력
    printer.profit_printer(profit)
    
    return


def main():
    run()


if __name__ == '__main__':
    main()
