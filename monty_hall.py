"""
Monty Hall Problem simulation
"""

import argparse
import logging
import random
import time


def run_simulation(change_selection):
    """Runs the Monty Hall Problem simulation

    Args:
        change_selection (bool): If the door selection should be changed
    """
    # Simulation variables
    num_simulations = 500_000
    num_wins = 0

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

        # Monty Hall picks a door
        if prize_door in possible_doors:
            for door in possible_doors:
                if door != prize_door:
                    montys_door = door
        else:
            montys_door = random.choice(possible_doors)
        possible_doors.remove(montys_door)

        # Change the chosen door, if we're changing our selection
        if change_selection:
            chosen_door = possible_doors[0]

        # Check if we picked the winning door and update the win counter
        if chosen_door == prize_door:
            num_wins += 1

    # Calculate winning percentage
    winning_percentage = num_wins / num_simulations * 100

    if change_selection:
        logging.info(f'Given {num_simulations:,} simulations, the chance of '
                     f'winning when changing door selection is '
                     f'{winning_percentage:.2f} %')
    else:
        logging.info(f'Given {num_simulations:,} simulations, the chance of '
                     f'winning when not changing door selection is '
                     f'{winning_percentage:.2f} %')

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
