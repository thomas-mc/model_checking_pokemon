# Readme

## File Structure
* best_moves_stats.json contains the necessary data for all of the moves involved in the model generation with this specific set of Pokemon
* best_pokemon_best_moves.txt contains the list of 4 moves that correspond to each Pokemon that is in use in this implementation
* best_pokemon_by_type_LEGENDS.py prints out lists of Pokemon ordered by the coded metrics, this file involves legendary Pokemon
* best_pokemon_by_type_NO_LEGENDS.py prints out lists of Pokemon ordered by the coded metrics, this file excludes legendary Pokemon
* best_pokemon_by_type_NO_SPEED.py prints out lists of Pokemon ordered by the coded metrics, this file excludes legendary Pokemon and the speed stat from the total stat calculation at the beginning of the file
* pokedex_no_legends.txt is the list of Pokemon with their stats, with the legendary Pokemon excluded
* pokedex_real.txt is the list of Pokemon with their stats
* prism_model_script_final.py is the python file that generates the PRISM models for Pokemon battles involving legendary Pokemon
* prism_model_script_final_no_legends.py is the python file that generates the PRISM models for Pokemon battles for the teams that don't involve legendary Pokemon
* prism_model_script_final_winners.py is the python file that generates a single PRISM model for the Pokemon battle between the two strongest teams
* teams.txt is the list of teams with their label and corresponding list of Pokemon for teams involving legendary Pokemon
* teams_no_legends.txt is the list of teams with their label and corresponding list of Pokemon for teams without legendary Pokemon, but with the speed stat
* teams_no_legends_no_speed.txt is the list of teams with their label and corresponding list of Pokemon for teams without legendary Pokemon and the supplementary teams that don't include speed
* teams_no_speed.txt is the list of teams with their label and corresponding list of Pokemon for teams that don't involve speed, this is the aforementioned list of 'supplementary' Pokemon teams
* teams_winners.txt is the list of teams with their label and corresponding list of Pokemon for the two strongest teams
* type_effectiveness.txt is the list of Pokemon types and their corresponding list of type effectiveness values
* p1vp2_winner_props.props has been included in each PRISM model folder, this is the PRISM properties file that is necessary to evaluate the probability of a team winning

## Instructions

* ***IMPORTANT:*** file paths in the Python files must be changed to match your own correct paths, only up to the point of the 'src' folder should be changed. The following file names and line numbers denote where these changes should be made:
  * best_pokemon_by_type_LEGENDS.py - line 4, line 63
  * best_pokemon_by_type_NO_LEGENDS.py - line 4, line 63
  * best_pokemon_by_type_NO_SPEED.py - line 4, line 63
  * prism_model_script_final.py - line 7, line 12, line 17, line 22, line 27, line 152
  * prism_model_script_final_no_legends.py - line 7, line 12, line 17, line 22, line 27, line 152
  * prism_model_script_final_winners.py - line 7, line 12, line 17, line 22, line 27, line 152
* To generate ordered lists of Pokemon based on metrics, with all Pokemon included, execute the best_pokemon_by_type_LEGENDS.py. It prints out the lists with all their details. These lists were used to inform the creation of the teams.txt file.
* To generate ordered lists of Pokemon based on metrics, with all legendary Pokemon excluded, execute the best_pokemon_by_type_NO_LEGENDS.py. It prints out the lists with all their details. These lists were used to inform the creation of the teams_no_legends.txt file.
* To generate ordered lists of Pokemon based on metrics, with all legendary Pokemon excluded and with the speed stat excluded, execute the best_pokemon_by_type_NO_SPEED.py. It prints out the lists with all their details. These lists were used to inform the creation of the teams_no_speed.txt file.
* To generate the models for the Pokemon battles involving legendary Pokemon, execute prism_model_script_final.py
* To generate the models for the Pokemon battles excluding legendary Pokemon, execute prism_model_script_final_no_legends.py
* To generate the models for the Pokemon battle between the two strongest teams, execute prism_model_script_final_winners.py
* To build a PRISM model, open the PRISM command line, and run the following command:
  prism total_duplicate_legend_VERSUS_team_of_interest_no_speed.prism p1vp2_winner_props.props -prop 1 -nopre

  This would build the model 'total_duplicate_legend_VERSUS_team_of_interest_no_speed.prism' and verify the first property of the file 'p1vp2_winner_props.props'.

  prop 1 = player 1 win

  prop 2 = player 2 win

  prop 3 = deadlock check

  Given that the PRISM command line opens on the bin directory of PRISM, it may be useful to insert the models of interest into the PRISM program file folder, and in the command navigate to the files. This would look like:
  
  prism ..\prism-examples\pokemon_new\total_duplicate_legend_VERSUS_team_of_interest_no_speed.prism ..\prism-examples\pokemon_new\p1vp2_winner_props.props -prop 1 -nopre


### Requirements

* Python 3.7
* PRISM Model Checker
* PRISM-games
* Tested on Windows 10
