import random

# Define the board
board_size = 100
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll):
    position += roll
    if position > board_size:
        position = board_size  # Ensure player doesn't move beyond the last square
    return position

def check_snakes_and_ladders(position):
    if position in snakes:
        print(f"Oops! You landed on a snake. Go down from {position} to {snakes[position]}.")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! You landed on a ladder. Go up from {position} to {ladders[position]}.")
        return ladders[position]
    else:
        return position

def print_board(positions):
    print("\nBoard:")
    for i in range(board_size, 0, -10):
        line = ""
        for j in range(i, i - 10, -1):
            if j == positions[0]:
                line += f"[P1]"
            elif j == positions[1]:
                line += f"[P2]"
            else:
                line += f" {j:2d} "
        print(line)
    print("\n")

def main():
    positions = [1, 1]  # Initial positions for player 1 and player 2
    player_names = ["Player 1", "Player 2"]
    current_player = 0  # Start with player 1
    
    print_board(positions)
    
    while True:
        input(f"{player_names[current_player]}'s turn. Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"{player_names[current_player]} rolled a {roll}.")
        
        # Move the current player
        positions[current_player] = move_player(positions[current_player], roll)
        positions[current_player] = check_snakes_and_ladders(positions[current_player])
        print(f"{player_names[current_player]} is now on square {positions[current_player]}.")
        
        # Print the board
        print_board(positions)
        
        # Check for win condition
        if positions[current_player] == board_size:
            print(f"Congratulations! {player_names[current_player]} has reached the end of the board and won!")
            break
        
        # Switch to the other player
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
