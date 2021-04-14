
def profit(rank_sum, times):

    sum = 0
    price = [5000000, 100000, 20000, 5000]
    for i in range(4):
        sum += price[i]*rank_sum[i]

    profit = sum/times/1000

    return profit