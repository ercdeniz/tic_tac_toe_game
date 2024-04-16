import utils as u

def choose_player():
    u.clear()
    print(f"{u.LGREEN}Welcome to Tic Tac Toe!{u.RES}")
    while True:
        try:
            u.game_status = input(f"{u.YELLOW}Do you want to play single or multiplayer? (S/M): {u.RES}").strip().upper()
            if u.game_status == 'M':
                u.player, u.player_2 = 'X', 'O'
                u.clear()
                print(f"{u.GREEN}Player 1 is {u.player}. Player 2 is {u.player_2}.{u.RES}")
                return 0
            elif u.game_status == 'S':
                u.clear()
                while u.player != 'X' and u.player != 'O':
                    u.player = input(f"{u.MAGENTA}Do you want to be X or O?: {u.RES}").upper().strip()
                    if u.player in ['X', 'O']:
                        u.computer = 'O' if u.player == 'X' else 'X'
                        if u.computer == 'X':
                            u.board[4] = u.computer
                    else:
                        u.clear()
                        print(f"{u.RED}Invalid input. Try again.{u.RES}")
                        continue
                    u.clear()
                    print(f"{u.GREEN}You are {u.player}. Computer is {u.computer}.{u.RES}")
                    return 0
            else:
                raise ValueError("Invalid input. Try again.")
        except KeyboardInterrupt:
            print(f"\n{u.CYAN}Exiting the game...{u.RES}")
            return 1
        except Exception as e:
            u.clear()
            print(f"{u.RED}Error: {e}{u.RES}")
            continue
