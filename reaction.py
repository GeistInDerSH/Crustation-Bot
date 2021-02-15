from datetime import date

class Reaction:
    def __init__(self, user, message):
        self.user = str(user)
        self.message = message

        # Each of the unique Discord ids for the users
        self.users = {
			# @UnitZer0
			'211258171094859776': [],
			# @tjx1212
			'214581352689958922': ['🦀'],
			# @naps
			'180729155829104640': ['🐒'],
			# @ZaqueXIII
			'153673650929664000': [],
			# @Blitztraum
			'196317961890299904': [],
			# @Coop
			'214861395211059201': [],
			# @JorJor The Dinosaur
			'205043049024323584': ['💧'],
			# @Roost
			'181914855706460160': [],
			# @Zega(Tyler)
			'272442562177007619': [],
			# @Blahman
			'220341843315916800': [],
			# @GaryArk3443
			'388449127333232642': [],
			# @A Single Neuron
			'187039157426585600': [],
			# @lucii
			'424766351622537216': []
        }

        # Emoji for each of the different days (Format MM-DD)
        self.days = {
			# New years Day
			'01-01': ['🎉'],
			# Valentines Day
			'02-14': ['💘', '🌵'],
			# 4th of July
			'07-04': ['🇺🇸'],
			# Thanksgiving
			'11-26': ['🦃'],
			# Hanukkah 2020 Dates
			'12-10': ['🕎'],
			'12-11': ['🕎'],
			'12-12': ['🕎'],
			'12-13': ['🕎'],
			'12-14': ['🕎'],
			'12-15': ['🕎'],
			'12-16': ['🕎'],
			'12-17': ['🕎'],
			'12-18': ['🕎'],
			# X-Mass
			'12-25': ['🎄'],
			# Boxing day
			'12-26': ['📦'],
			# New Years Eve
			'12-31': ['🎉']
		}

    def get_reactions(self) -> list:
        """
            Using the user and message, get all emoji reactions

            Return:
                A list of emoji
        """
        return self.user_reaction() + self.day_reaction() + self.message_reaction()

    def user_reaction(self) -> list:
        """
            Attempts to get the reaction for when a specific user sends a message

            Return:
                List of UTF-8 Emoji
        """
        try:
            return self.users[self.user]
        except Exception:
            return []

    def day_reaction(self) -> list:
        """
            Adds emojis based on the current date for the system

            Return:
                List of UTF-8 Emoji
        """
        try:
            today = str(date.today())[5:]
            return self.days[today]
        except Exception:
            return []

    def message_reaction(self) -> list:
        """
            Adds emojis based on the content of the message sent

            Return:
                List of UTF-8 Emoji
        """
        lst = []
        if '69' in self.message:
            lst += ['🇳', '🇮', '🇨', '🇪']

        if any(['games' in self.message, 'gamez' in self.message, 'gamz' in self.message]):
            lst += ['🎮', '❓']

        if self.contains_pen15():
            lst += ['🍆']

        return lst

    def contains_pen15(self) -> bool:
        """
            Checks if the message contains 'pen15' or 'pen' an expression
            that evaluates to 15

            Return:
                If the string contains 'pen15'
        """
        try:
            pen = self.message.find('pen')
            if pen == -1: return False

            nums = self.message[pen + 3:].strip()

            return True if eval(nums) == 15 else False
        except Exception:
            return False
