# monty-hall-simulation
Simulations for the Monty Hall problem and a variation on the problem.


# Monty Hall Problem
In the Monty Hall problem there are three possible doors, two of which contain nothing behind them and one which contains a prize. The host, Monty Hall, asks the contestant to pick a door.  Next, he chooses from among the remaining two doors, randomly if neither is the prize door and specifically choosing a non-prize door if the prize door was not chosen by the contestant.  After opening the door and revealing nothing behind the door, he asks the contestant if they would like to change their selection.  After deciding to either keep the initial door choice or change to the other door, Monty Hall reveals where the prize is located.  This simulation shows which method (changing door selection or staying put) is statistically more likely to lead to choosing the winning door.


# Variation
The variation on the Monty Hall problem is different in that Monty Hall no longer chooses the non-prize door when the prize door is still available.  Instead, he will randomly pick from the remaining two doors, even if that means he picks the winning door, at which point the game is over.  This simulation aims to answer the following question: when Monty Hall doesn't pick the winning door, is it still advantageous to switch doors?


# Usage and Output
Run either python file and supply one of the two optional arguments (either change_selection or keep_selection) in order to specify if the door choice should be changed when given the opportunity.  If neither argument is given then the default behavior is to change selection.  The output shows the probability of winning based on the specified strategy.

```
python monty_hall.py --change_selection
Given 500,000 simulations, the chance of winning when changing door selection is 66.71 %

python monty_hall.py --keep_selection
Given 500,000 simulations, the chance of winning when not changing door selection is 33.38 %
```
