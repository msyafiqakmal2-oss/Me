Just Any Small Game I Trying It But In The Next Time I can do more again again than from the previous and good
And Thanks For You all

This Python script is a simple  interactive Number Guessing Game. It uses basic programming concepts like loops, conditionals, and random number generation to create a fun, terminal-based experience.

Here is a breakdown of how the code works :
1. Setup and Initialization

    import random: This line imports Python's built-in random module, which allows the program to generate unpredictable numbers.and

    angka_rahasia = random.randint(1, 10): The program picks a random integer between 1 and 10 (inclusive) and stores it in the variable angka_rahasia (the "secret number").

    percobaan = 0: This variable acts as a counter to keep track of how many attempts the player has made.

2. The Game Loop (while True)

The program enters an infinite loop, meaning it will keep asking the player for guesses until they get the answer right and the break command is triggered.

    Input: tebakan = int(input(...)) captures the user's guess and converts it from text into an integer.

    Counter: percobaan += 1 increments the attempt count by 1 every time a guess is made.
