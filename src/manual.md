# User manual

To learn how to run the code. Please see the readme.

The Python script that is made to create models of Pokemon battles is already set up with lists of teams and moves.

A user can further use this to investigate Pokemon by providing their own data on Pokemon and moves, if it is in the same json format as the existing data.
With new data provided, the script can read the data in and produce a model of the battle between the Pokemon teams that have been specified, with the moveset that has been specified.

PRISM is then used to evaluate the probabilities of these models (refer to readme for this). The result of evaluating a query will be a decimal between zero and one. This corresponds to the probability of the set query.
The queries relate to how likely player 1 (team 1) and player 2 (team 2) is to win when both players perform optimally in game.
