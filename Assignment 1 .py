import sys
import time
import random

SLEEP_BETWEEN_ACTIONS = 0.5    #for the sake of convenience we take a time gap of 1.0 seconds between any event.

MAXIMUM_VALUE = 100           # maximum value to be reached.

DICE_FACES = 6                # number of faces in dice is 6

# snake takes you down from 'key' to 'value'
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

# ladder takes you up from 'key' to 'value'
ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

player_turn_text = [
   "it's your turn now ",
    "\n good luck"
]

snake_bite = [
   "ohh noo",
    "\n snake bite"
]

ladder_jump = [
    "yeah" ,
    "\n rocked"
]


def welcome_msg():
    msg = """
    !! Welcome to the Game !!.
    Developed by: Akshita Jain

    points :
      1. At first both the players are at starting position i.e. 0.  
         Move forward the number of spaces shown on the dice.
      2. Hit enter to roll the dice.

    """
    print(msg)


def get_players_name():
    player1_name = None
    while not player1_name:
        player1_name = input("please enter your name of player 1 ").strip()

        #strip function will remove the extra white spaces given in name at start and end.

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter your name of player 2 ").strip()

    print("\nMatch is between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACES)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(past_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper())
    print("\n" + player_name + " got a snake bite. Down from " + str(past_value) + " to " + str(current_value))


def got_ladder_jump(past_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper())
    print("\n" + player_name + " climbed the ladder from " + str(past_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    past_value = current_value
    current_value = current_value + dice_value

    if current_value > MAXIMUM_VALUE:
        print("You need " + str(MAXIMUM_VALUE - past_value) + " to win this game. Keep trying.")
        return past_value

    print("\n" + player_name + " moved from " + str(past_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_winner(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAXIMUM_VALUE == position:
        print("\n\n\nFinally, here's the result and :  \n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing ")
        sys.exit(1)


def start():
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_name, player2_name = get_players_name()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\n!!Rolling dice!!")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player1_name + " !!moving!!")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_winner(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\n!!Rolling dice!!")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        print(player2_name + " !! moving !!")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_winner(player2_name, player2_current_position)


if __name__ == "__main__":
    start()