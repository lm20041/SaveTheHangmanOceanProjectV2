import random
def Errors(err):
  print('    >>> an error has occurred at part', err,'<<<')
#-------------------------------#
def Aesthetics(aes):
  if aes == 'START':
    Buttons_dec('START')
  elif aes == 'MS':
    Buttons_dec('MS')
  elif aes == 'IS':
    Buttons_dec('IS')
  elif aes == 'GS':
    Buttons_dec('GS')
  elif aes == 'GPS':
    Buttons_dec('GPS')
  elif aes == 'SBS':
    Buttons_dec('SBS')
  else:
    Errors('Def Aesthetic')
#-------------------------------#
def MainScreen():
  print(""" 
Welcome to Plastic Pollution Hangman
    
""")
def IntroScreen():
  print(""" 
rules of this game is simple a random word about our ocean pollution will be selected your job is to guess what that word is. you have 8 lives every time you get a letter wrong you loss a live. if you managed to guess the word you win. but loss all 8 lives and you lose
  """)
def GenerateScreen():
  print(""" 
alright let's get started, select the generate button and we can begin
  """)

def draw_hangman(attempts):
    hangman_pics = [
        """
          +---+
              |
              |
              |
             ===
        """,
        """
          +---+
          O   |
              |
              |
             ===
        """,
        """
          +---+
          O   |
          |   |
              |
             ===
        """,
        """
          +---+
          O   |
         /|   |
              |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
              |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         /    |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         / \\  |
             ===
        """
    ]
    return hangman_pics[0:attempts]
#=====================================#
def GamePlayScreens():
    words = ['plastic', 'pollution', 'ocean', 'environment', 'marine']
    play_again = True

    while play_again:
        secret_word = random.choice(words)
        guessed_letters = []
        incorrect_guesses = 0

        print("Welcome to Plastic Pollution Hangman!")
        print("Guess the letters to reveal the word associated with plastic pollution in our oceans.")

        while incorrect_guesses < 8:
            display_word = ''
            for letter in secret_word:
                if letter in guessed_letters:
                    display_word += letter + ' '
                else:
                    display_word += '_ '

            print("\n" + " ".join(draw_hangman(incorrect_guesses)))
            print(display_word)
            print(f"Incorrect guesses: {incorrect_guesses}/{8}")
            
            if display_word.replace(' ', '') == secret_word:
                print(f"Congratulations! You've guessed the word: '{secret_word}'")
                break

            guess = input("Enter your guess: ").lower()

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                elif guess in secret_word:
                    guessed_letters.append(guess)
                else:
                    incorrect_guesses += 1
            else:
                print("Invalid input. Please enter a single letter.")

        if incorrect_guesses == 8:
            print("Sorry, you've run out of guesses. The word was:", secret_word)
        Buttons_dec('GPS')

def ScoreBoardScreen():
  print('print(\' game end, you have\',gameresults,\'with only\',incorrect_guesses,\'incorrect guesses\')')
  #print(' game end, you have',gameresults,'with only',incorrect_guesses,'incorrect guesses')

def Screens(scr):
  if scr == 'MS':
    MainScreen()
  elif scr == 'IS':
    IntroScreen()
  elif scr == 'GS':
    GenerateScreen()
  elif scr == 'GPS':
    GamePlayScreens()
  elif scr == 'SBS':
    ScoreBoardScreen()
  else:
    Errors('Def Screens')

#-------------------------------#
def Buttons_dec(but):
  if but == 'START':
    decision = 'shall I start the program(yes/no): '
    choices = {'yes':'MS', 'no':'repeat_START'}
  elif but == 'MS':
    decision = 'would you like to play (yes/no): '
    choices = {'yes':'IS', 'no':'repeat_MS'}
  elif but == 'IS':
    decision = 'would you like to continue and play (continue): '
    choices = {'continue':'GS'}
  elif but == 'GS':
    decision = 'would you like to generate a word (yes/no):'
    choices = {'yes':'GPS', 'no':'repeat_GS'}
  elif but == 'GPS':
    decision = 'would you like to see the scoreboard (yes/no)'
    choices = {'yes':'SBS', 'no':'repeat_GPS'}
  elif but == 'SBS':
    decision = 'would you like to play again or go Return to Main (PlayAgain/ReturnToMain)'
    choices = {'playagain':'GS', 'returntomain':'MS'}
  else:
    Errors('Def Buttons')

  print(decision)
  Button_input = input('> ')
  Button_input = Button_input.lower()

  if Button_input in choices:
    for choice in choices:
      if Button_input == choice:
        ChangeScreen(choices[choice])
  else:
    print('that is not the option try again')
    Buttons_rep(but)
#------------------------------------------------#
def Buttons_rep(but):
  if but == 'START':
    choices = {'yes':'MS', 'no':'repeat_START'}
    repeat_Q = 'are you sure... (yes/no): '
  elif but == 'MS':
    choices = {'yes':'IS', 'no':'repeat_MS'}
    repeat_Q = 'are you sure you don\'t want to play (yes/no): '
  elif but == 'IS':
    choices = {'continue':'GS'}
    repeat_Q = 'are you sure you don\'t want to continue (continue): '
  elif but == 'GS':
    choices = {'yes':'GPS', 'no':'repeat_GS'}
    repeat_Q = 'are you sure you don\'t want to generate a word (yes/no):'
  elif but == 'GPS':
    choices = {'yes':'SBS', 'no':'repeat_GPS'}
    repeat_Q = 'are you sure you don\'t want to see the scoreboard (yes/no):'
  elif but == 'SBS':
    choices = {'playagain':'GS', 'returntomain':'MS'}
    repeat_Q = 'well which is it (PlayAgain/ReturnToMain):'
  else:
    Errors('Def Buttons')

  print(repeat_Q)
  Button_input = input('> ')
  Button_input = Button_input.lower()
  if Button_input in choices:
    for choice in choices:
      if Button_input == choice:
        ChangeScreen(choices[choice])
  else:
    print('that is not the option try again')
    Buttons_rep(but)
#-------------------------------#
def ChangeScreen(Cp):
  if Cp == 'START':
    Aesthetics('START')
  elif Cp == 'MS':
    Screens('MS')
    Aesthetics('MS')
  elif Cp == 'IS':
    Screens('IS')
    Aesthetics('IS')
  elif Cp == 'GS':
    Screens('GS')
    Aesthetics('GS')
  elif Cp == 'GPS':
    Screens('GPS')
    Aesthetics('GPS')
  elif Cp == 'SBS':
    Screens('SBS')
    Aesthetics('SBS')
  elif Cp == 'repeat_START': #repeat_Q
    Buttons_rep('START')
  elif Cp == 'repeat_MS': 
    Buttons_rep('MS')
  elif Cp == 'repeat_IS': 
    Buttons_rep('IS')
  elif Cp == 'repeat_GS': 
    Buttons_rep('GS')
  elif Cp == 'repeat_GPS': 
    Buttons_rep('GPS')
  elif Cp == 'repeat_SBS':
    Buttons_rep('SBS')
  else:
    Errors('Def ChangeScreen')
ChangeScreen('START')