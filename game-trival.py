import requests
import random

# Function to fetch trivia questions from the Open Trivia Database API
def fetch_questions(amount=20):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

# Function to play the game
def play_game():
    score = 0
    
    # Ask the user for the number of questions
    try:
        num_questions = int(input("How many questions would you like to answer? (default 20): ") or 20)
    except ValueError:
        print("Invalid input. Using default of 20 questions.")
        num_questions = 20
    
    # Fetch the specified number of questions
    questions = fetch_questions(amount=num_questions)

    print("Welcome to the Trivia Quiz Game!")
    print("Answer the questions to the best of your ability.\n")

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")

        # Combine correct and incorrect answers, then shuffle
        options = question['incorrect_answers']
        options.append(question['correct_answer'])
        random.shuffle(options)

        # Display the options
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")

        # Get the user's answer
        try:
            answer = int(input("Your answer (1-4): "))
            if options[answer - 1] == question['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.\n")

    print(f"Game over! Your final score is: {score} out of {len(questions)}")

# Run the game
if __name__ == "__main__":
    play_game()
