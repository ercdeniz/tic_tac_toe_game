import print_board as pb
import check_game_over as cg
import choose_player as cp
import computer_move as cm
import utils as u

def game():
    try:
        pb.print_board(1)
        input(f"{u.YELLOW}Press Enter to start the game...{u.RES}")
        u.clear()
        var = 1
        while True:
            try:
                if var:
                    var = 0
                else:
                    u.clear()
                pb.print_board()
                user_move = int(input(f"{u.BLUE}Enter your move (1-9): {u.RES}").strip())
                if user_move < 1 or user_move > 9 or u.board[user_move - 1] != ' ':
                    u.clear()
                    print(f"{u.RED}Invalid move. Try again.{u.RES}")
                    var = 1
                    continue
                u.board[user_move - 1] = u.player
                game_over, result = cg.check_game_over()
                if game_over:
                    u.clear()
                    pb.print_board()
                    print(u.CYAN + result + u.RES)
                    break
                while True:
                    computer_move = cm.computer_move()
                    if u.board[computer_move] == ' ':
                        u.board[computer_move] = u.computer
                        break
                game_over, result = cg.check_game_over()
                if game_over:
                    u.clear()
                    pb.print_board()
                    print(u.CYAN + result + u.RES)
                    break
            except Exception as e:
                u.clear()
                print(f"{u.RED}Error: {e}{u.RES}")
                var = 1
                continue
    except KeyboardInterrupt:
        print(f"\n{u.CYAN}Exiting the game...{u.RES}")

if cp.choose_player():
    exit()
game()