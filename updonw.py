import random


def upndown_game():
    best_count = 0
    while True:
        count = 0
        random_num = random.randint(1, 100)
        print(random_num)  # 테스트 랜덤 숫자
        while True:
            try:
                user_guess = int(input("Guess a number between 1 and 100: "))
                count += 1
                if 1 <= user_guess <= 100:
                    if user_guess < random_num:
                        print("Up!")
                        print(f"{count}번째 시도입니다.")
                    elif user_guess > random_num:
                        print("Down!")
                        print(f"{count}번째 시도입니다.")
                    else:
                        print("Right!")
                        print(f"{count}번째 시도만에 맞추셨습니다.")
                        if best_count == 0 or count < best_count:
                            best_count = count
                            print(f"최고 시도 횟수 갱신: {best_count}")
                        else:
                            print(f"이전 게임 최고 시도 횟수: {best_count}")
                        break  # 내부 루프 종료
                else:
                    print("범위 밖 숫자입니다. 1과 100 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("유효한 값을 입력해주세요.")

        re_game = input("다시 도전하시겠습니까? (y/n): ")
        if re_game.lower() != 'y':
            break  # 외부 루프 종료


# 게임 시작
upndown_game()
