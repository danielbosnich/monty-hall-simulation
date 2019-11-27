"""
Monty Hall Variation Simulation

The only difference here is that after the contestant chooses a door, Monty
Hall RANDOMLY picks a door from the two remaining doors. If he chooses
correctly, then the game is over. If he doesn't choose correctly, then the
contenstant is given the chance to change doors or stick with the original
choice.
The output of this simulation is the overall chance of winning,
as well as the chance of winning, when either switching or not, when given
the chance to switch doors.

Created on Sat May  4 11:26:39 2019

@author: danielb
"""

import random
import logging
import time

def main():
    """Run the Monty Hall variation simulation"""
    # Simulation variables
    num_simulations = 10000
    change_selection = True
    num_wins = 0
    num_monty_wins = 0

    # Seed the random number generator
    random.seed()

    # Start time
    start_time = time.time()

    # Start up logging
    logging.basicConfig(format='[%(asctime)s] %(levelname)s : %(message)s',
                        level=logging.INFO)

    # Run the simulation
    for i in range(num_simulations):
        logging.debug("Running simulation number %i", i)
        possible_doors = [0, 1, 2]
        prize_door = random.randint(0, 2)
        logging.debug("The prize is located in door: %i", prize_door)
        chosen_door = random.randint(0, 2)
        logging.debug("The chosen door is: %i", chosen_door)

        # Remove the chosen door from the list of possible doors
        possible_doors.remove(chosen_door)
        logging.debug("The remaining two doors are: %i and %i",
                      possible_doors[0], possible_doors[1])

        # Monty Hall randomly picks a door
        montys_door_index = random.randint(0, 1)
        montys_door = possible_doors[montys_door_index]
        possible_doors.remove(montys_door)
        logging.debug("Monty Hall chose door: %i", montys_door)

        # Check if Monty Hall chose the winning door
        if montys_door == prize_door:
            num_monty_wins += 1
            continue

        # Change the chosen door - if we're changing our selection
        if change_selection:
            chosen_door = possible_doors[0]

        # Check if we picked the winning door and update the win counter
        logging.debug("The final door chosen is door: %i", chosen_door)
        if chosen_door == prize_door:
            num_wins += 1


    # Calculate winning percentage
    win_percentage = num_wins / num_simulations * 100

    # Calculate winning percentage when giving the chance to switch
    change_win_percentage = num_wins / (num_simulations - num_monty_wins) * 100

    if change_selection:
        logging.info("Given %i simulations, the chance of winning when "
                     "changing door selection is %.3f %%",
                     num_simulations,
                     win_percentage)
        logging.info("Given %i simulations, the chance of winning when "
                     "given the chance to change door selection, and choosing "
                     "to change door selection, is %.3f %%",
                     num_simulations,
                     change_win_percentage)
    else:
        logging.info("Given %i simulations, the chance of winning when "
                     "not changing door selection is %.3f %%",
                     num_simulations,
                     win_percentage)
        logging.info("Given %i simulations, the chance of winning when given "
                     "the chance to change door selection, and not choosing "
                     "to change door selection, is %.3f %%",
                     num_simulations,
                     change_win_percentage)

    # Calculate program execution time
    end_time = time.time()
    execution_time = end_time - start_time
    logging.debug("It took the program %.3f seconds to run", execution_time)

    # Close the logger
    logging.shutdown()

if __name__ == '__main__':
    main()
