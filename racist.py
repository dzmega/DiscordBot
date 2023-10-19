class racist:
    n_word_counter = 0

    def __init__(self,username):
        self.username = username
        self.n_word_counter += 1

    def count(self):
        self.n_word_counter += 1