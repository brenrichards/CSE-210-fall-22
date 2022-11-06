# Student: Brendan Richards
# Instructor: Brad Lythgoe

def draw_board():
    practice_grid_top = "1|2|3"
    practice_grid_mid = "4|5|6"
    practice_grid_bot = "7|8|9"
    print("\033[4m" + practice_grid_top + "\033[0m")
    print("\033[4m" + practice_grid_mid + "\033[0m")
    print(practice_grid_bot)

def win_determination(grid):
    # WIN DETERMINATION BY ROWS
    # TOP ROW
    if grid[0][2] == grid[1][2] == grid[2][2] and grid[1][2] != "_":
        print("top row filled")
        winning_sign = grid[0][2]
        return winning_sign
        # MIDDLE ROW
    elif grid[3][2] == grid[4][2] == grid[5][2] and grid[4][2] != "_":
        print("middle row filled")
        winning_sign = grid[3][2]
        return winning_sign
        # BOTTOM ROW 
    elif grid[6][2] == grid[7][2] == grid[8][2] and grid[6][2] != " ":
        print("Bottom row filled")
        winning_sign = grid[6][2]
        return winning_sign

    # WIN DETERMINATION BY COLUMNS
    # LEFT COLUMN
    elif grid[0][2] == grid[3][2] == grid[6][2] and grid[3][2] != "_":
        print("LEFT COLUMN FILLED")
        winning_sign = grid[0][2]
        return winning_sign
    # MIDDLE COLUMN
    elif grid[1][2] == grid[4][2] == grid[7][2] and grid[4][2] != "_":
        print("MIDDLE COLUMN FILLED")
        winning_sign = grid[1][2]
        return winning_sign
    # RIGHT COLUMN
    elif grid[2][2] == grid[5][2] == grid[8][2] and grid[5][2] != " ":
        print("RIGHT COLUMN FILLED")
        winning_sign = grid[2][2]
        return winning_sign

        # WIN DETERMINATION BY DIAGONALS
    elif grid[0][2] == grid[4][2] == grid[8][2]:
        print("DIAGONAL LEFT FILLED")
        winning_sign = grid[0][2]
        return winning_sign
    elif grid[2][2] == grid[4][2] == grid[6][2]:
        print("DIAGONAL RIGHT FILLED")
        winning_sign = grid[2][2]
        return winning_sign
    else:
        winning_sign = "nobody"
    return winning_sign
    
def main(game_state):
    while game_state == "in_progress":
        grid_player_input = int(input("Enter Grid space:\n"))
        marking_player_input = input("Enter the Desired marking:\n")
        
        if grid_player_input == 1:
            grid[0][2] = marking_player_input
        if grid_player_input == 2:
            grid[1][2] = marking_player_input
        if grid_player_input == 3:
            grid[2][2] = marking_player_input
        if grid_player_input == 4:
            grid[3][2] = marking_player_input
        if grid_player_input == 5:
            grid[4][2] = marking_player_input
        if grid_player_input == 6:
            grid[5][2] = marking_player_input
        if grid_player_input == 7:
            grid[6][2] = marking_player_input
        if grid_player_input == 8:
            grid[7][2] = marking_player_input
        if grid_player_input == 9:
            grid[8][2] = marking_player_input
        print(f"{grid[0][2]}|{grid[1][2]}|{grid[2][2]}\n{grid[3][2]}|{grid[4][2]}|{grid[5][2]}\n{grid[6][2]}|{grid[7][2]}|{grid[8][2]}")

        winning_sign = win_determination(grid)
        
        if winning_sign == "nobody":
            continue
        else:
            print(f"{winning_sign}'s Win!")
            break


play_again = "y"
game_state = "in_progress"

print(f"Welcome to Tic Tac Toe\nThis is what your grid looks like")
draw_board()
print("To Place an X or O, type the grid space,\nFollowed by the Desired Marking")



while play_again == "y":

    #CLEAR THE BOARD
    grid = [[1, 0, "_"], [2, 0, "_"], [3, 0, "_"], [4, 0, "_"], [5, 0, "_"], [6, 0, "_"], [7, 0, " "], [8, 0, " "], [9, 0, " "]]

    main(game_state)

    play_again = input("Play again? y or n\n")
    if play_again == "y":
        draw_board()
        continue
    if play_again == "n":
        print(f"Thanks for playing!")
        break