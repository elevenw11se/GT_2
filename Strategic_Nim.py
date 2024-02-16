from nimsupport import *



"""
The player's strategy takes into account the number of stacks and coins. When there is an odd number of stacks, it
removes all coins from the smallest stack. Otherwise, it removes all coins except for one from the smallest stack. 
When there are two nonempty stacks remaining, it removes either 1 coin (if there are an odd number of coins) or 2 coins 
(if there are an even number of coins) from the largest stack. If there is 1 coin in both stacks, it removes 1 coin. 
Finally, if there is one stack remaining it removes all coins from the stack, guaranteeing a win. I came to this
strategy by noticing how important it is for the number of stacks and coins to be odd. This makes it so that it is 
possible to win the game. The opponent will always have an advantage if the number of stacks and coins is even, so
this strategy does its best to keep that from happening. This strategy also tries to force the other player to leave
a single nonempty stack, because it will always win. 

Other things I tried were only using the number of coins and attempting something similar to a search-based approach. 
While the number of coins is useful to know, it can helpful to consider the number of stacks so I decided to use both. 
A search-based approach can be tedious and time-intensive so I decided it would not be a good idea. In addition, 
I used the nim player functions (nim2_strategy, random_nim_strategy, and human_player) to experiment with the 
strategy. I attempted to find weaknesses to improve The strategy through such experimentation. The human_player 
function. in particular, was especially useful to test this strategy since it enabled me to experiment and find out
what would happen in certain scenarios. 

"""


def nim_strategy(nim_piles_list):
    """
    takes the list of nim piles as a parameter and returns a tuple representing the move it will take
    :param nim_piles_list: (list) represents the piles
    :return: (tuple) first element is the pile number, second element is the number to remove from
    that pile
    """

    if num_stacks(nim_piles_list) == 1:  # if one pile left
        for i in range(len(nim_piles_list)):
            if nim_piles_list[i] != 0:
                pile_num = i  # index of only nonempty pile
                num_to_remove = nim_piles_list[pile_num]  # remove entire pile
                return pile_num, num_to_remove

    elif num_stacks(nim_piles_list) == 2:  # two piles left
        maximum = -1
        pile_num = 0

        for i in range(len(nim_piles_list)):
            if nim_piles_list[i] >= maximum and nim_piles_list[i] != 0:  # finding largest stack
                pile_num = i  # index of the largest stack
                maximum = nim_piles_list[i]

        if get_coin_count(nim_piles_list) % 2 == 1:  # odd, remove 1 from stack
            return pile_num, 1
        elif get_coin_count(nim_piles_list) % 2 == 0 and nim_piles_list[pile_num] > 1:
            return pile_num, 2  # even, remove 2 from stack
        else:
            return pile_num, 1  # stack size = 1, can only remove 1

    else:  # over three piles left
        minimum = 101
        pile_num = 0

        for i in range(len(nim_piles_list)):  # finding smallest stack
            if nim_piles_list[i] <= minimum and nim_piles_list[i] != 0:
                minimum = nim_piles_list[i]
                pile_num = i  # index of the smallest stack

        if num_stacks(nim_piles_list) % 2 == 1:
            return pile_num, minimum  # remove entire stack
        else:
            return pile_num, minimum - 1   # remove entire stack - 1


def num_stacks(nim_piles_list):
    """
    takes the list of nim piles as a parameter and returns the number of nonempty stacks
    :param nim_piles_list: (list) represents the piles
    :return: (int) the number of nonempty stacks
    """
    count = 0
    for i in range(len(nim_piles_list)):
        if nim_piles_list[i] != 0:
            count += 1

    return count


def get_coin_count(nim_piles_list):
    """
    takes the list of nim piles as a parameter and returns the number of coins
    :param nim_piles_list: (list) represents the piles
    :return: (int) the total number of coins
    """
    count = 0
    for i in range(len(nim_piles_list)):
        count += nim_piles_list[i]

    return count


