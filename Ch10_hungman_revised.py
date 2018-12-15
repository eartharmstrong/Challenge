
def hangman(word):
    wrong = 0
    num = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        while True:
            msg = "Guess a letter:"
            guess = input(msg)
            num = len(guess)
            if num == 1:
                break
            else:
                print("Type again one letter\n")
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0 : wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")


