import random


class PasswordGenerator:
    CHARS = "abcdefghijklmnopqrstufvxyzABCDEFGHIJKLMNOPQRSTUFVXYZ"
    NUMBERS = "0123456789"
    SPECIAL_CHARS = "()-._!äöü+&@"

    passwords = []

    def generate(self, length, special_chars):
        all_chars = self.CHARS + self.NUMBERS
        if special_chars:
            all_chars += self.SPECIAL_CHARS
        result_list = random.sample(all_chars, length)
        result = "".join(result_list)
        self.passwords.append(result)

        return result

    def get_history_limited(self, limit):
        result = []
        offseted_limit = limit + 1
        if len(self.passwords) >= offseted_limit:
            result = self.passwords[-offseted_limit: -1]
        elif len(self.passwords) > 1:
            result = self.passwords[:-1]

        result.reverse()
        return result
