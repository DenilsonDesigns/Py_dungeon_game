import random
import os

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw the player in the grid
# take the input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(current_player, current_move):
    x, y = current_player
    if current_move == "LEFT":
        x -= 1
    if current_move == "RIGHT":
        x += 1
    if current_move == "UP":
        y -= 1
    if current_move == "DOWN":
        y += 1
    return x, y


def get_moves(current_player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = current_player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


def draw_map(current_player, current_monster, current_door):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == current_player:
                output = tile.format("X")
            elif cell == current_monster:
                output = tile.format("M")
            elif cell == current_door:
                output = tile.format("^")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == current_player:
                output = tile.format("X|")
            elif cell == current_monster:
                output = tile.format("M|")
            elif cell == current_door:
                output = tile.format("^")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player, monster, door)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player))  # fill with player position
        print("You can move {}".format(", ".join(valid_moves)))  # fill with available moves
        print("Enter QUIT to quit")

        move = input("> ").upper()
        if move == 'QUIT':
            print("\n ** See you next time! ** \n")
            break
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** Oh no! Monster killed you! Try again! ** \n ")
                playing = False
            if player == door:
                print("\n ** You escaped! Congrats! ** \n")
                playing = False

        else:
            input("\n ** Walls are hard! Don't run into them! ** \n")
    else:
        if input("Playing again? [Y/n] ").lower() != "n":
            game_loop()


clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
