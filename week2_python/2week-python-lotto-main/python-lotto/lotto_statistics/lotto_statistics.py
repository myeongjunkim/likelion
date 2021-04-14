
def check(lotto_sum,win):

    rank_sum=[0,0,0,0]
    for lotto in lotto_sum:

        cnt = 0
        for num in lotto:
            for win_num in win:
                if num == win_num:
                    cnt += 1
        
        if cnt == 6:
            rank_sum[0] += 1
        elif cnt == 5:
            rank_sum[1] += 1
        elif cnt == 4:
            rank_sum[2] += 1
        elif cnt == 3:
            rank_sum[3] += 1

    return rank_sum

    