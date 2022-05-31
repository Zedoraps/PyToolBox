from datetime import datetime


class Tippgeschwindigkeit:

    def __init__(self):
        self.start_time = None
        self.result = 0

    def start(self):
        if not self.start_time:
            self.start_time = datetime.now()
            return True
        else:
            return False

    def finish(self, tipped_text):
        if self.start_time:
            words = len(tipped_text.split(" "))
            time_difference = datetime.now() - self.start_time
            seconds = time_difference.total_seconds()

            self.result = (words / (seconds / 60))
            return True
        else:
            return False

    def number_of_words_per_minute(self):
        return self.result
