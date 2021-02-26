from datetime import date

from emoji import Emoji

class Reaction:
    def __init__(self, user, message):
        self.user = str(user)
        self.message = message

        # Each of the unique Discord ids for the users
        self.users = {
			# @UnitZer0
			'211258171094859776': Emoji([], []),
			# @tjx1212
			'214581352689958922': Emoji(['🦀'], ['TJ is a crustacean']),
			# @naps
			'180729155829104640': Emoji(['🐒'], ['Return to monke']),
			# @ZaqueXIII
			'153673650929664000': Emoji([], []),
			# @Blitztraum
			'196317961890299904': Emoji([], []),
			# @Coop
			'214861395211059201': Emoji([], []),
			# @JorJor The Dinosaur
			'205043049024323584': Emoji(['💧'], ['¯\_(ツ)_/¯']),
			# @Roost
			'181914855706460160': Emoji([], []),
			# @Zega(Tyler)
			'272442562177007619': Emoji([], []),
			# @Blahman
			'220341843315916800': Emoji([], []),
			# @GaryArk3443
			'388449127333232642': Emoji([], []),
			# @A Single Neuron
			'187039157426585600': Emoji([], []),
			# @lucii
			'424766351622537216': Emoji([], [])
        }

        year = date.today().year

        # Emoji for each of the different days (Format MM-DD)
        self.days = {
			# New years Day
			'01-01': Emoji(['🎉'], [f'New Year\'s Day ({year}-01-01)']),
			# Valentines Day
			'02-14': Emoji(['💘', '🌵'], [f'Valentine\'s Day ({year}-02-14)', f'Ariziona\'s {year - 1912} Birthday ({year}-02-14)']),
			# 4th of July
			'07-04': Emoji(['🇺🇸'], [f'America\'s {date.today().year - 1776} Birthday ({year}-07-04)']),
			# Thanksgiving
			'11-26': Emoji(['🦃'], [f'Thanksgiving (US) ({year}-11-25)']),
			# Hanukkah 2020 Dates
			'12-10': Emoji(['🕎'], [f'Hanukkah ({year}-11-28 to {year}-12-06)']),
			# X-Mass
			'12-25': Emoji(['🎄'], [f'Christmas Day ({year}-12-25)']),
			# Boxing day
			'12-26': Emoji(['📦'], [f'Boxing Day ({year}-12-26)']),
			# New Years Eve
			'12-31': Emoji(['🎉'], [f'New Year\'s Eve ({year}-12-31)'])
		}

        self.message_emojis = {
            'games': Emoji(['🎮'], ['You asked to play games']),
            'pen15': Emoji(['🍆'], ['Your message contained \'pen\' and numbers that summed to 15'])
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
            return self.users[self.user].emojis
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
            return self.days[today].emojis
        except Exception:
            return []

    def message_reaction(self) -> list:
        """
            Adds emojis based on the content of the message sent

            Return:
                List of UTF-8 Emoji
        """
        lst = []
        if any(['games' in self.message, 'gamez' in self.message, 'gamz' in self.message]):
            lst += self.message_emojis['games'].emojis

        if self.contains_pen15():
            lst += self.message_emojis['pen15'].emojis

        return lst

    def contains_flags(self) -> bool:
        """
            Check to see if the user message has any of the command flags

            Return:
                If there are any command flags
        """
        if '--help' in self.message:
            return True
        elif '--why' in self.message:
            return True
        return False

    def get_flag_response(self) -> str:
        """
            Get response from the entered flag
        """
        if '--help' in self.message:
            return '\n'.join([
                'Command     Description',
                '--help      Shows this menu',
                '--why       Why do I have these emojis',
                '--why_all   What does every emoji mean?'])

        elif '--why_all' in self.message:
            s = "User specific reactions:\n"
            for _, v in self.users.items():
                s += v.explain()

            s += "\nDate specific reactions:\n"
            for _, v in self.days.items():
                s += v.explain()

            s += "\nMessage specific reactions:\n"
            for _, v in self.message_emojis.items():
                s += v.explain()

            return s

        elif '--why' in self.message:
            lst = self.get_all_emoji_explanation()

            s = ""
            for emoji in lst:
                s += emoji
            return s if len(s) > 0 else "I couldn't find any reason you would have emojis\n¯\_(ツ)_/¯"

        return ""

    def get_all_emoji_explanation(self) -> list:
        """
            Gets the reasons for each emoji on the server

            Return:
                list of strings
        """
        lst = []
        try:
            lst += self.users[self.user].explain()
        except Exception:
            lst += []

        try:
            today = str(date.today())[5:]
            lst += self.days[today].explain()
        except Exception:
            lst += []

        if any(['games' in self.message, 'gamez' in self.message, 'gamz' in self.message]):
            lst += self.message_emojis['games'].explain()

        if self.contains_pen15():
            lst += self.message_emojis['pen15'].explain()

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
            if self.message.find('pen15') != -1: return True

            nums = self.message[pen + 3:].strip()

            return True if eval(nums) == 15 else False
        except Exception:
            return False
