# Brooklen Ashleigh
# April 16, 2022
# Project Two: Text-based Game (Beware the Alien)

from themap import story_map

# Initialize global variables for current player location, inventory
location = "Central Elevator"
inventory = []

# Copy item set of story_map in uppercase for validation of user commands
# Allows user to type "get item" commands in any case
valid_set = {k: v['Item'].upper() for (k, v) in story_map.items()}

# Functions

# Prints menu borders 100 characters long
def print_border():
    print("-" * 100)


# Prints story introduction. Invoked only when the game is started
def print_introduction():
    print_border()

    print(
        "> INTERCOM: Hello, this is the captain of Space Station X. We are currently under siege by an \n"
        "unidentified organism. We've lost a lot of crew members, but we have managed to get the **** \n"
        "thing stuck in an airlock, not sure exactly where. We still have some big problems to solve. \n"
        "You'll need to assemble a weapon to keep the thing occupied long enough to prime, activate the \n"
        "airlock, and blast it out into the cold depths of space. Don't confront it before you have all \n"
        "of your tools though, or we'll all be dead. Good luck and -BZZZ- speed."
    )


# Prints instructions for game mechanics at the beginning of the game and when user enters "help" command
def print_help():
    print_border()
    print("> INSTRUCTIONS:")
    print("You must collect eight unique items in order to prime the air lock and defend \n"
          "yourself from the organism. Do not face the organism before you have all eight tools \n"
          "or it will mean the death of you and everyone on the space station.")
    print_border()
    print("> HOW TO PLAY:")
    print("- To move between rooms, enter 'Go North', 'Go South', 'Go East', or 'Go West'.")
    print("- To pick up items you can see, enter 'Get [Item name]'.")
    print("- For help, enter 'Help'. To quit, enter 'Quit'.")
    print("Commands are not case sensitive. Good luck.")


# Print player location and inventory after every player action
def show_status():
    print_border()

    # Print player location and location description
    print("> You are in the [{}]. {}".format(location, story_map[location]['Comment']))
    # Print player inventory
    print("> Your inventory contains:", end=" ")

    # Wraps and prints the inventory list depending on the length of inventory
    # Prints "Nothing" if inventory is empty
    if 0 < len(inventory) <= 4:
        print(*inventory[0:4], sep=", ")
    elif len(inventory) >= 5:
        print(*inventory[0:4], sep=", ", end="")
        print(",", end="\n")
        print(*inventory[4:], sep=", ")
    elif len(inventory) == 0:
        print("Nothing")

    # If an item is available in the room, print that the player sees it
    if story_map[location]['Item'] != "":
        print("> You see a {}".format(story_map[location]['Item']))

    print_border()


# Check player input and move player if input is valid direction
def movement(direction):
    # Initialize set of directions to check against
    cardinal = {"North", "South", "East", "West"}
    # Initialize global location - function directly modifies
    global location
    # Capitalize user input for conformity
    direction = direction.title()

    # Check if user's direction is a valid and available direction
    if direction[3:] in story_map[location]:
        # Set user location to new location based on direction
        location = story_map[location][direction[3:]]
    # If player enters "exit", give them the option to quit
    elif direction == "Exit":
        # Ask user if they want to quit. Returning True will break game loop
        # Returning false will resume the game from previous location
        print("If you would like to exit, enter 'quit'. Otherwise, type anything to continue:")
        check_input = input("> ").title()

        if check_input == "Quit":
            print("Goodbye!")
            return True
        else:
            return False
    # Check if direction is valid (NSEW) but not available
    elif direction[3:] in cardinal and direction[3:] not in story_map[location]:
        print("Sorry, you can't go that way.")
    else:
        print("Invalid Input")


# Allow player to pick up items and add them to their inventory.
# When item is picked up, removes item from item set
def manage_inventory(user_decision):
    global inventory
    # Remove "get" from player input and set to uppercase to help validation
    user_decision = user_decision[4:].upper()

    # If input item is in the current location, add it to inventory and delete it from available item set
    if user_decision in valid_set[location]:
        inventory.append(story_map[location]['Item'])
        print("You've added {} to your inventory.".format(story_map[location]['Item']))
        story_map[location]['Item'] = ""
    else:
        print("Sorry, you can't do that.")


# Victory or Death: Assesses whether the player wins or loses when they go into air lock
# and print victory or death message. Main loop will subsequently break.
def v_or_d():
    print_border()
    if len(inventory) == 8:
        # Print success message
        print(
            "The organism sulks in the corner of the air lock as you enter. The walls have been slashed \n"
            "beyond repair in its efforts to find an exit. It seems to have expended much of its energy, \n"
            "but when it sees you enter, it lifts itself from its stupor and quickly springs for you.\n"
            "You light your makeshift flame thrower with your butane lighter and a cloud of flame bursts\n"
            "toward the creature. In its panic, you manage to lurch toward the air lock's console and \n"
            "enter the access codes needed to prime the air lock. You set down the flame thrower, still\n"
            "pointed at the organism, and manage to exit the air lock quicker than the organism can sidestep\n"
            "and lunge for you. You seal the door with a satisfying pneumatic hiss, then start the evacuation\n"
            "sequence from the outer console. You pound 'Enter' with the flat of your fist and the entire\n"
            "air lock erupts as the outer door aperture opens, sucking everything in the room out into\n"
            "the cold depths of space. You think you heard a faint scream as the door opened, but it is\n"
            "quickly cut off. Congratulations, you have saved Space Station X."
        )
        print_border()
    else:
        # Print death message
        print(
            "The organism sulks in the corner of the air lock as you enter. The walls have been slashed\n"
            "beyond repair in its efforts to find an exit. It seems to have expended much of its energy, \n"
            "but when it sees you enter, it lifts itself from its stupor and quickly springs for you.\n"
            "Without the proper tools needed to defend yourself, you quickly succumb to the organism's\n"
            "long, blood-sticky claws. You have failed your mission, along with the crew of Space Station X."
        )
        print_border()


def main():
    # Print introduction text at beginning of game
    print_introduction()
    print_help()

    # Loop until player decides to exit game or they win or lose
    while True:
        # Print player location and inventory after every action
        show_status()
        # Take user input
        print("What would you like to do? (go, get, help, or exit)")
        user_decision = input("> ").title()

        # Check if input begins with go, get, or exit and responds with the proper method
        if location == "Maintenance Room" and user_decision == "Go East":
            v_or_d()
            break
        elif user_decision[0:2] == "Go":
            movement(user_decision)
        elif user_decision[0:3] == "Get":
            manage_inventory(user_decision)
        elif user_decision == "Exit":
            if movement("exit"):
                break
            else:
                continue
        elif user_decision == "Help":
            print_help()
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
