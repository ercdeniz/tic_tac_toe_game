import random
import clear as cl
import print_board as pb
import vars_and_board as vb
import check_game_over as cg
import choose_player as cp
import colors as c

def game():
    var = 1
    while True:
        try:
            if(var == 0):
                cl.clear()
            else:
                var = 0
            pb.print_board()
            user_move = int(input(f"{c.BLUE}Enter your move (1-9): {c.RES}").strip())
            if user_move < 1 or user_move > 9 or vb.board[user_move - 1] != ' ':
                cl.clear()
                print(f"{c.RED}Invalid move. Try again.{c.RES}")
                var = 1
                continue
            vb.board[user_move - 1] = vb.player
            game_over, result = cg.check_game_over()
            if game_over:
                cl.clear()
                pb.print_board()
                print(c.CYAN + result + c.RES)
                break
            while True:
                computer_move = random.randint(0, 8)
                if vb.board[computer_move] == ' ':
                    vb.board[computer_move] = vb.computer
                    break
            game_over, result = cg.check_game_over()
            if game_over:
                cl.clear()
                pb.print_board()
                print(c.CYAN + result + c.RES)
                break
        except KeyboardInterrupt:
            print(f"\n{c.CYAN}Exiting the game...{c.RES}")
            break
        except Exception as e:
            cl.clear()
            print(f"{c.RED}Error: {e}{c.RES}")
            var = 1
            continue

print(f"{c.LGREEN}Welcome to Tic Tac Toe!{c.RES}")
if cp.choose_player():
    exit()
game()