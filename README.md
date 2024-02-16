# This script implements a strategic approach for playing the Nim Game.
# It takes into account the number of stacks and coins in the game and then makes moves that will maximxe the chances of winning.
# The player's strategy takes into account the number of stacks and coins. When there is an odd number of stacks, it  removes all coins from the smallest stack. Otherwise, it removes all coins except for one from the smallest stack. 
  
# When there are two nonempty stacks remaining, it removes either 1 coin (if there are an odd number of coins) or 2 coins (if there are an even number of coins) from the largest stack.
# If there is 1 coin in both stacks, it removes 1 coin. 
# Finally, if there is one stack remaining it removes all coins from the stack, guaranteeing a win. 
# I came to this strategy by noticing how important it is for the number of stacks and coins to be odd. This makes it so that it is possible to win the game.
# The opponent will always have an advantage if the number of stacks and coins is even, so this strategy does its best to keep that from happening.
# This strategy also tries to force the other player to leave a single nonempty stack, because it will always win. 


# Other things I tried were only using the number of coins and attempting something similar to a search-based approach. 
# While the number of coins is useful to know, it can helpful to consider the number of stacks so I decided to use both. 
# A search-based approach can be tedious and time-intensive so I decided it would not be a good idea. 
# In addition, I used the nim player functions (nim2_strategy, random_nim_strategy, and human_player) to experiment with the strategy.

# I attempted to find weaknesses to improve The strategy through such experimentation. The human_player function, in particular, was especially useful to test this strategy since it enabled me to experiment and find out
what would happen in certain scenarios. 
