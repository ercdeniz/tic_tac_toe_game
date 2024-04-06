import random
import clear as cl
import colors as c
import vars_and_board as vb

def choose_player():
    cl.clear()

    while vb.player != 'X' and vb.player != 'O':
        try:
            vb.player = input(f"{c.MAGENTA}Do you want to be X or O?: {c.RES}").upper().strip()
            if vb.player in ['X', 'O']:
                vb.computer = 'O' if vb.player == 'X' else 'X'
                if vb.computer == 'X':
                    vb.board[random.randint(0, 8)] = vb.computer
            else:
                cl.clear()
                print(f"{c.RED}Invalid input. Try again.{c.RES}")
                continue
            cl.clear()
            print(f"{c.GREEN}You are {vb.player}. Computer is {vb.computer}.{c.RES}")
            break
        except KeyboardInterrupt:
            print(f"\n{c.CYAN}Exiting the game...{c.RES}")
            return 1
        except Exception as e:
            cl.clear()
            print(f"{c.RED}Error: {e}{c.RES}")
            continue