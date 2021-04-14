import random


# 단어장 시작점
HANGMAN_SUGGESTED_WORD_START_INDEX = 1
# 문자 입력
INPUT_ATTEMPT_WORD_MESSAGE = "도전할 문자를 적어주세요: "
#
INPUT_ATTEMPT_WRONG_WORD_MESSAGE = "올바른 형식으로 입력해주세요.(영어, 한글자)"

# 게임 다 끝났을때 메세지
PRINT_FINISH_GAME_MESSAGE = "MISSION COMPLETE: 행맨을 살렸습니다."


# 
PRINTER_WRONG_LETTER_MESSAGE = "단어에 없는 문자입니다!"

PRINTER_FAIL_GAME_MESSAGE = "GAME OVER: 행맨이 죽었습니다."

# 단어장(여기서 랜덤으로 선택된걸 맞추는거임)
hangman_suggested_word = {
    1: "around",
    2: "complain",
    3: "improve",
    4: "sweet",
    5: "able",
    6: "arrange",
    7: "complete",
    8: "govern",
    9: "notice",
    10: "represent",
    11: "precious",
    12: "proud",
    13: "strength",
    14: "work",
    15: "complex",
    16: "claim",
    17: "flavor",
    18: "honest",
    19: "include",
    20: "order",
    21: "precise",
    22: "prove",
    23: "reputation",
    24: "stretch",
    25: "well",
    26: "above",
    27: "against",
    28: "devote",
    29: "harm",
    30: "grade",
    31: "income",
    32: "ordinary",
    33: "march",
    34: "provide",
    35: "realize", 
    36: "abroad",
    37: "before", 
    38: "compose",
    39: "gradual",
    40: "mark",
    41: "reason",
    42: "shy",
    43: "therefore",
    44: "absent",
    45: "classify",
    46: "turn",
    47: "graduate",
    48: "indeed",
    49: "original",
    50: "receive",
}



# 단어장 길이 함수
def get_hangman_suggested_word_size():
    return len(hangman_suggested_word)


# 랜덤으로 단어장에서 단어 하나 가져옴
def get_hangman_answer_word():
    random_word_index = random.randint(HANGMAN_SUGGESTED_WORD_START_INDEX,
    get_hangman_suggested_word_size())
    hangman_answer_word = hangman_suggested_word.get(random_word_index)
    return hangman_answer_word


# 알파벳 하나 입력 받는 함수
def input_attempt_word():
    input_word = input(INPUT_ATTEMPT_WORD_MESSAGE)
    return input_word

# 제대로 입력했는지 보는 함수
def check_input_attempt_word():
    while True:
        input_word = input_attempt_word()
        if input_word.isalpha() and len(input_word) == 1:
            break
        print(INPUT_ATTEMPT_WRONG_WORD_MESSAGE)
    return input_word


# attempt_word 안에 있는지 없는지(반복 방지) 시도한 알파벳 이어붙여놈
def append_letter_attempt_word(letter, attempt_word):
    if letter not in attempt_word:
        attempt_word += letter
    return attempt_word

# 지금까지 입력했던 알파벳 들이랑 정답이랑 비교하는 함수

def compare_suggested_word(attempt_word, hangman_answer_word):
    is_succeed = True

    # 한글자씩 차례대로 불러와서 비교/ 맞는거만 출력하고 아닌거 언더바로 찍음
    for lettering in hangman_answer_word:
        if lettering in attempt_word:
            print_matched_lettering(lettering)
        else:
            print_under_bar()
            is_succeed = False
    return is_succeed


#실패시 fail_count 추가
def check_letter_in_answer_word(letter, hangman_answer_word, fail_count):
    
    if letter not in hangman_answer_word:
        printer_wrong_letter()
        print()
        fail_count +=1
    return fail_count


def is_fail_game(fail_count):
    if fail_count == 7:
        return True
    return False







#print





#두개 한세트
# 맞춘 부분  표시하는 함수
def print_matched_lettering(lettering):
    print(lettering, " ", end='')
# 틀린 부분 언더바
def print_under_bar():
    print("_", " ", end='')







# 성공시 찍어주기
def printer_finish_game():
    print(PRINT_FINISH_GAME_MESSAGE)

def printer_hangman_answer_word(hangman_answer_word):
    print("정답 단어: ", hangman_answer_word)

def printer_wrong_letter():
    print(PRINTER_WRONG_LETTER_MESSAGE)


def printer_fail_game():
    print(printer_fail_game)







def printer_hangman(count):
    if count >= 1:
        head = "(.,.)"
    else:
        head = "     "
    if count >= 2:
        body = "|"
    else:
        body = " "
    if count >= 3:
        left_arm = "/"
    else:
        left_arm = " "
    if count >= 4:
        right_arm = "\\"
    else:
        right_arm = " "
    if count >= 5:
        left_leg = "/"
    else:
        left_leg = " "
    if count >= 6:
        right_leg = "\\"
    else:
        right_leg = " "

    print("----------")
    print("  |     ||")
    print("%s   ||" % head)
    print(" %s%s%s    ||" % (left_arm, body, right_arm))
    print("  %s     ||" % body)
    print(" %s %s    ||" % (left_leg, right_leg))
    print("        ||")
    print("     -----")


















# 행맨게임 함수
def run():
    # 시도해본 모든 단어 문자열
    attempt_word =""
    hangman_answer_word = get_hangman_answer_word() # 랜덤 단어 하나
    fail_count = 0
    
    print(hangman_answer_word)
    while True:

        game_succeed = compare_suggested_word(attempt_word, hangman_answer_word)

        print()
        if game_succeed:
            printer_finish_game()
            printer_hangman_answer_word(hangman_answer_word)
            break
        
        


        #알파벳 하나 입력받은거 letter에 넣음
        letter = check_input_attempt_word() # 입력받는 함수
        
        # 맞는지 틀린지 확인하고 attempt_word 늘려감
        attempt_word = append_letter_attempt_word(letter, attempt_word)

        fail_count = check_letter_in_answer_word(letter, hangman_answer_word, fail_count)

        if is_fail_game(fail_count):
            printer_fail_game()
            printer_hangman_answer_word(hangman_answer_word)
            break

        printer_hangman(fail_count)








def main():
    run()


if __name__ == "__main__":
    main()