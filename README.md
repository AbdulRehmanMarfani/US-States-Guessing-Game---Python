---

# U.S. States Guessing Game

## Overview
The U.S. States Guessing Game is a fun and educational Python program that tests your knowledge of the 50 U.S. states. The game displays a blank map of the United States, and you are prompted to guess the names of the states. If you guess correctly, the state's name will appear on the map. At the end of the game, you can see your score, the time taken, and the states you missed.

## Features
- **Interactive Map**: A blank map of the U.S. is displayed, and you can guess the names of the states.
- **Score Tracking**: The game keeps track of your score as you guess states correctly.
- **Timer**: The game records the time taken to complete the quiz.
- **High Score**: The game saves your high score and displays it at the end.
- **Missed States**: After the game ends, you can see a list of states you missed.
- **Hint System**: You can request hints to help you guess the states.

## How to Play
1. **Run the Game**: Execute the Python script to start the game.
2. **Guess States**: Enter the name of a state when prompted. The game is case-insensitive.
3. **Use Hints**: Type `hint` to get a hint for the last correctly guessed state.
4. **End the Game**: Type `end` to finish the game and see your results.
5. **View Results**: After the game ends, a new screen will display your score, time taken, high score, and the list of states you missed.

## Requirements
- Python 3.x
- `turtle` module (included in Python's standard library)
- `pandas` module (install using `pip install pandas`)
- `blank_states_img.gif` (map image file)
- `50_states.csv` (CSV file containing state names and coordinates)

## Installation
1. Clone the repository or download the Python script and required files.
2. Install the required Python modules:
   ```bash
   pip install pandas
   ```
3. Ensure that `blank_states_img.gif` and `50_states.csv` are in the same directory as the script.

## Running the Game
To run the game, execute the Python script:
```bash
python us_states_game.py
```

## Files
- `us_states_game.py`: The main Python script for the game.
- `blank_states_img.gif`: The blank map of the U.S. used in the game.
- `50_states.csv`: A CSV file containing the names and coordinates of the 50 U.S. states.
- `missing_states.csv`: A CSV file generated at the end of the game containing the list of missed states.
- `high_score.txt`: A text file that stores the high score and time.

## High Score Fix
The high score functionality has been updated to display the **highest score** instead of the last score. The game now reads all scores from `high_score.txt` and displays the one with the highest score.

## Example Output
```
Game Over!
Time taken: 5 minutes 30 seconds
Your score: 40/50
High Score: Score: 45/50 | Time: 4m 20s
States you missed:
Alabama
Alaska
Arizona
...
```

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions for improvements are always welcome!

## License
This project is open-source and available under the MIT License.

---
