import random

def select_random_hand():
    hands = ["가위", "바위", "보"]
    return random.choice(hands)

def get_user_input():
    while True:
        try:
            user_input = int(input("숫자를 입력하세요 (1: 가위, 2: 바위, 3: 보): "))
            if 1 <= user_input <= 3:
                return user_input
            else:
                print("1, 2, 3 중 하나를 입력하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def play_game():
    hands = ["가위", "바위", "보"]
    re_game = "y"
    win, lose, draw = 0, 0, 0

    while re_game == 'y' :
        computer_hand = select_random_hand()
        user_input = get_user_input()
        user_hand = hands[user_input - 1]

        if user_hand == computer_hand:
            draw += 1
            print(f"user: {user_hand} vs {computer_hand}")
            print("무승부")
        elif (user_hand == "가위" and computer_hand == "보") or (user_hand == "바위" and computer_hand == "가위") or (user_hand == "보" and computer_hand == "바위"):
            win += 1
            print(f"user: {user_hand} vs {computer_hand}")
            print("유저 승")
        else:
            lose += 1
            print(f"user: {user_hand} vs {computer_hand}")
            print("컴퓨터 승")

        total_games = win + lose + draw
        if total_games > 0:
            win_rate = win / total_games
        else:
            win_rate = 0

        print(f"전적은 {win}승, {draw}무, {lose}패입니다. 승률은 {win_rate:.1%}입니다.") # %로 바꾸는 것 : .1% 여기서 1은 소수점단위

        re_game = input("한판 더? (y/n): ").strip().lower() # strip lower 대문자 소문자로
        if re_game == 'n':
            print("게임을 종료합니다.")


play_game()
