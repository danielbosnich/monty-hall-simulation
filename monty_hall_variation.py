"""
Monty Hall Variation simulation

The only difference here is that after the contestant chooses a door, Monty
Hall RANDOMLY picks a door from the two remaining doors. If he chooses
correctly, then the game is over. If he doesn't choose correctly, then the
contenstant is given the opportunity to change doors or stick with the original
choice.

The output of this simulation is the overall chance of winning as well as
the chance of winning when given the opportunity to switch doors.
"""

import argparse
import logging
import random
import time


def run_simulation(change_selection):
    """Runs the Monty Hall Variation simulation

    Args:
        change_selection (bool): If the door selection should be changed
    """
    # Simulation variables
    num_simulations = 100_000
    num_wins = 0
    num_monty_wins = 0

    # Simulation start time
    start_time = time.time()

    # Run the simulation
    for _ in range(num_simulations):
        # Randomly pick a door to be the prize door and then also randomly
        # choose a door for the game and remove that door from possible_doors
        possible_doors = [0, 1, 2]
        prize_door = random.choice(possible_doors)
        chosen_door = random.choice(possible_doors)
        possible_doors.remove(chosen_door)

        # Monty Hall randomly picks a door
        montys_door = random.choice(possible_doors)
        possible_doors.remove(montys_door)

        # Check if Monty Hall chose the winning door
        if montys_door == prize_door:
            num_monty_wins += 1
            continue

        # Change the chosen door, if we're changing our selection
        if change_selection:
            chosen_door = possible_doors[0]

        # Check if we picked the winning door and update the win counter
        if chosen_door == prize_door:
            num_wins += 1

    # Calculate winning percentage
    win_percentage = num_wins / num_simulations * 100

    # Calculate winning percentage when giving the chance to switch
    change_win_percentage = num_wins / (num_simulations-num_monty_wins) * 100

    if change_selection:
        logging.info(f'Given {num_simulations:,} simulations, the chance of '
                     f'winning when changing door selection is '
                     f'{win_percentage:.2f} %')
        logging.info(f'Given {num_simulations:,} simulations, the chance of '
                     f'winning when given the chance to change door selection,'
                     f' and choosing to change door selection, is '
                     f'{change_win_percentage:.2f} %')
    else:
        logging.info(f'Given {num_simulations:,} simulations, the chance of '
                     f'winning when not changing door selection is '
                     f'{win_percentage:.2f} %')
        logging.info(f'Given {num_simulations:,} simulations, the chance of '
                     f'winning when given the chance to change door selection,'
                     f' and not choosing to change door selection, is '
                     f'{change_win_percentage:.2f} %')

    # Calculate program execution time
    execution_time = time.time() - start_time
    logging.debug(f'It took the program {execution_time:.3f} seconds to run')


def parse_args():
    """Parses the passed argument. In order to set the boolean value, one of
    the two optional arguments should be specified. If neither argument is
    used, True will be returned

    Returns:
        (bool): If the door selection should be changed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--keep_selection',
                        dest='change_selection',
                        action='store_false',
                        help='Keep the door selection')
    parser.add_argument('--change_selection',
                        dest='change_selection',
                        action='store_true',
                        help='Change the door selection')
    return parser.parse_args().change_selection


def main():
    """Sets up logging and starts the simulation"""
    logging.basicConfig(format='[%(asctime)s] %(levelname)s : %(message)s',
                        level=logging.INFO)

    change_selection = parse_args()
    run_simulation(change_selection)

    logging.shutdown()


if __name__ == '__main__':
    main()
