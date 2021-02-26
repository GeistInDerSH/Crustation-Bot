class Emoji:
    def __init__(self, emojis: list, reasons: list):
        if len(emojis) != len(reasons):
            raise Exception(f"Incompatible lengths given {len(emojis)} vs {len(reasons)}")

        self.emojis = emojis
        self.reasons = reasons
        self.length = len(emojis)

    def explain(self) -> str:
        """
            Prints out the emoji and the reason for the emoji

            Return:
                An emoji and a description
        """
        explanation = ""
        for i in range(0, self.length):
            explanation += f'{self.emojis[i]} : {self.reasons[i]}\n'
        return explanation

