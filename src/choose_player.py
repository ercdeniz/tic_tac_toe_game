import random
import utils as u

def choose_player():
    u.clear()
    print(f"{u.LGREEN}Welcome to Tic Tac Toe!{u.RES}")
    while u.player != 'X' and u.player != 'O':
        try:
            u.player = input(f"{u.MAGENTA}Do you want to be X or O?: {u.RES}").upper().strip()
            if u.player in ['X', 'O']:
                u.computer = 'O' if u.player == 'X' else 'X'
                if u.computer == 'X':
                    u.board[random.randint(0, 8)] = u.computer
            else:
                u.clear()
                print(f"{u.RED}Invalid input. Try again.{u.RES}")
                continue
            u.clear()
            print(f"{u.GREEN}You are {u.player}. Computer is {u.computer}.{u.RES}")
            break
        except KeyboardInterrupt:
            print(f"\n{u.CYAN}Exiting the game...{u.RES}")
            return 1
        except Exception as e:
            u.clear()
            print(f"{u.RED}Error: {e}{u.RES}")
            continue