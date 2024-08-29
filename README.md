 Trivia Quiz Game

## Overview

This is a simple trivia quiz game implemented in Python. It fetches random trivia questions from the [Open Trivia Database API](https://opentdb.com/) and quizzes the user. The game tracks the user's score based on their answers and provides feedback for each question.

## Features

- Fetches trivia questions from an API.
- Allows the user to specify the number of questions.
- Provides feedback on each answer.
- Displays the final score at the end of the game.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Install the Required Python Packages**:
   Make sure you have Python and pip installed. Then, install the `requests` library:
   ```bash
   pip install requests
   ```

## Usage

1. **Run the Game**:
   ```bash
   python trivia_game.py
   ```

2. **Follow the Prompts**:
   - Enter the number of questions you want to answer (default is 20).
   - Answer each question by selecting the correct option (1-4).

3. **View Your Score**:
   - After all questions have been answered, your final score will be displayed.

## Code Explanation

- **`fetch_questions(amount=20)`**: Fetches trivia questions from the Open Trivia Database API.
- **`play_game()`**: Runs the quiz game, asks the user for the number of questions, displays questions, processes answers, and calculates the final score.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
