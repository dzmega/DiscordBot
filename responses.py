import racist
def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "whats up!"

def get_score(list,username):
    for i in list:
        if i.username == username:
            return i.n_word_counter

def get_top(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j].n_word_counter < list[j + 1].n_word_counter:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list