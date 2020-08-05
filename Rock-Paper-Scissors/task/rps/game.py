import random


class RockPaperScissors:

    variants = ["rock", "paper", "scissors"]

    def __init__(self):
        self.name = ''
        self.losing = []
        rating_file = open('rating.txt')
        self.ratings = {line.split()[0]: line.split()[1] for line in rating_file}
        rating_file.close()

    def new_player(self, player_name):
        self.ratings[player_name] = 0

    def play(self, choice):
        bot_choice = random.choice(self.variants)
        if choice == bot_choice:
            print(f'There is a draw ({bot_choice})')
            self.ratings[self.name] += 50
        elif bot_choice in self.losing:
            print(f'Sorry, but computer chose {bot_choice}')
        else:
            print(f'Well done. Computer chose {bot_choice} and failed')
            self.ratings[self.name] += 100

    def get_losing_list(self, choice):
        choice_index = self.variants.index(choice)
        after = self.variants[choice_index + 1:]
        before = self.variants[:choice_index]
        except_choice = after + before
        return except_choice[:int(len(except_choice) / 2)]

    def start_game(self):
        self.name = input('Enter your name:')
        print('Hello,', self.name)
        if self.name not in self.ratings:
            self.new_player(self.name)
        variant = input().split(',')
        if not variant:
            self.variants = variant
        print("Okay, let's start")

        while True:
            command = input()
            if command == "!exit":
                print('Bye!')
                break
            if command == "!rating":
                print('Your rating:', self.ratings[self.name])
            elif command in self.variants:
                self.losing = self.get_losing_list(command)
                self.play(command)
            else:
                print('Invalid input')


new_game = RockPaperScissors()
new_game.start_game()
