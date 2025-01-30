import turtle
import pandas
import time

# Initialize screen
screen = turtle.Screen()
# screen.setup(width=725, height=800)  # Keep width same, increase height
screen.bgcolor("black")
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# Load data
data = pandas.read_csv("50_states.csv")
all_states = data["state"].str.lower().tolist()  # Convert to lowercase for case-insensitive comparison
correct_guesses = []
score = 0
start_time = time.time()  # Start timer

# Function to display hints
def get_hint(state):
    return f"The first letter is '{state[0].upper()}'."

# Main game loop
while len(correct_guesses) < 50:
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct",
        prompt="Guess the name of a state (or type 'end' to exit, 'hint' for a hint):"
    ).strip().lower()  # Normalize input

    if answer_state == "end":
        break

    if answer_state == "hint":
        if correct_guesses:
            hint_state = correct_guesses[-1]  # Hint for the last guessed state
            screen.textinput("Hint", get_hint(hint_state))
        else:
            screen.textinput("Hint", "No states guessed yet. Try guessing a state!")
        continue

    if answer_state in all_states and answer_state not in correct_guesses:
        score += 1
        correct_guesses.append(answer_state)
        state_data = data[data.state.str.lower() == answer_state]
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(arg=state_data.state.item(), font=("Times New Roman", 9, "normal"), align="center")
        state_name.color("green")  # Visual feedback for correct guesses
    elif answer_state in correct_guesses:
        screen.textinput("Already Guessed", "You've already guessed that state. Try another one!")
    else:
        screen.textinput("Incorrect", "That's not a valid state. Try again!")

# Calculate elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

# Calculate missing states
missing_states = [state for state in all_states if state not in correct_guesses]

# Save missing states to a file
missing_states_df = pandas.DataFrame(missing_states, columns=["Missing States"])
missing_states_df.to_csv("missing_states.csv", index=False)

# Save score and time to a file
with open("high_score.txt", "a") as file:
    file.write(f"Score: {score}/50 | Time: {minutes}m {seconds}s\n")

# Read high score from file
def read_high_score():
    try:
        with open("high_score.txt", "r") as file:
            lines = file.readlines()
            if lines:
                # Extract scores and times from each line
                scores = []
                for line in lines:
                    parts = line.strip().split(" | ")
                    score_part = parts[0].split(": ")[1]
                    score = int(score_part.split("/")[0])
                    scores.append((score, line.strip()))
                
                # Find the highest score
                highest_score_entry = max(scores, key=lambda x: x[0])
                return highest_score_entry[1]  # Return the entire line with the highest score
    except FileNotFoundError:
        return "No high score yet."
    return "No high score yet."

# Clear the screen and create a new black screen for results
screen.clear()
screen.bgcolor("black")
screen.title("Game Results")

# Create a turtle for displaying results
results_turtle = turtle.Turtle()
results_turtle.hideturtle()
results_turtle.penup()
results_turtle.color("white")

# Display game over message
results_turtle.goto(0, 350)
results_turtle.write("Game Over!", align="center", font=("Arial", 24, "bold"))

# Display time taken
results_turtle.goto(0, 300)
results_turtle.write(f"Time taken: {minutes} minutes {seconds} seconds", align="center", font=("Arial", 16, "normal"))

# Display score
results_turtle.goto(0, 250)
results_turtle.write(f"Your score: {score}/50", align="center", font=("Arial", 16, "normal"))

# Display high score
results_turtle.goto(0, 200)
results_turtle.write(f"High Score: {read_high_score()}", align="center", font=("Arial", 16, "normal"))

# Display missed states
results_turtle.goto(0, 150)
results_turtle.write("States you missed:", align="center", font=("Arial", 16, "normal"))

# Display missed states in multiple columns
def display_missing_states():
    num_states = len(missing_states)
    if num_states <= 10:
        num_columns = 1
        font_size = 12
    elif num_states <= 20:
        num_columns = 2
        font_size = 10
    else:
        num_columns = 3
        font_size = 8  # Further reduce font size for more states

    states_per_column = (num_states + num_columns - 1) // num_columns  # Divide states evenly
    x_positions = [-200, 0, 200]  # X positions for each column

    for col in range(num_columns):
        x = x_positions[col]
        y = 100  # Start lower to fit more states
        for i in range(col * states_per_column, min((col + 1) * states_per_column, num_states)):
            results_turtle.goto(x, y)
            results_turtle.write(missing_states[i].title(), align="center", font=("Arial", font_size, "normal"))
            y -= 20  # Spacing between states

# Display missing states
display_missing_states()

# Keep the window open until clicked
screen.exitonclick()