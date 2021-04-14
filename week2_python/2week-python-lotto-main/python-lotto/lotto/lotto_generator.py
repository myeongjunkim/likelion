
import random
# random.sample


def gen_num():
    num=[]
    while len(num) < 6:
        tem = random.randint(1,45)
        if tem not in num:
            num.append(tem)
    # num = num.sort()
    return sorted(num)




