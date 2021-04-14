
from lotto import lotto_generator

# 구매 가격 만큼 n개의 로또를 만드는 함수
def lotto_maker(times):
    lotto_sum = []

    for i in range(times):
        lotto_sum.append(lotto_generator.gen_num())
    
    return lotto_sum



