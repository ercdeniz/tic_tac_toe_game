import print_board as pb
import check_game_over as cg
import choose_player as cp
import computer_move as cm
import utils as u

def get_user_move(prompt):
    while True:
        try:
            user_move = int(input(f"{u.BLUE}{prompt}{u.RES}").strip())
            if user_move < 1 or user_move > 9 or u.board[user_move - 1] != ' ':
                raise ValueError(f"Invalid move. {user_move} is not empty. Try again.")
            return user_move
        except KeyboardInterrupt:
            print(f"\n{u.CYAN}Exiting the game...{u.RES}")
            return -1
        except ValueError as ve:
            u.clear()
            print(f"{u.RED}Error: {ve}{u.RES}")
            pb.print_board()
            continue

def make_move(player, prompt):
    while True:
        user_move = get_user_move(prompt)
        if user_move == -1:
            return False
        if u.board[user_move - 1] == ' ':
            u.board[user_move - 1] = player
            u.clear()
            pb.print_board()
            return True
        else:
            u.clear()
            print(f"{u.RED}Invalid move. Try again.{u.RES}")
            pb.print_board()

def game():
    try:
        if cp.choose_player():
            return
        pb.print_board(1)
        input(f"{u.YELLOW}Press Enter to start the game...{u.RES}")
        u.clear()
        pb.print_board()
        while True:
            if u.game_status == 'M':
                status = make_move(u.player, u.prompt_1)
                if not status:
                    break
            else:
                status = make_move(u.player, u.single)
                if not status:
                    break

            game_over, result = cg.check_game_over()
            if game_over:
                u.clear()
                pb.print_board()
                print(u.CYAN + result + u.RES)
                break

            if u.game_status == 'S':
                computer_move = cm.computer_move()
                u.board[computer_move] = u.computer
                u.clear()
                pb.print_board()
            else:
                status = make_move(u.player_2, u.prompt_2)
                if not status:
                    break

            game_over, result = cg.check_game_over()
            if game_over:
                u.clear()
                pb.print_board()
                print(u.CYAN + result + u.RES)
                break

    except KeyboardInterrupt:
        print(f"\n{u.CYAN}Exiting the game...{u.RES}")
        return

game()
