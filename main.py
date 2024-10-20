import random


LETTER_SCORES = {
    "А" : 1, "Б": 3, "В": 1, "Г" : 3, "Д": 2, "Е": 1, "Ё": 3, "Ж": 5, "3": 5, "И": 1,
    "Й": 4, "К": 2, "Л": 2, "М": 2, "Н": 1, "О": 1, "П": 2, "Р": 1, "С": 1, "Т": 1,
    "У": 2, "Ф": 10, "Х": 5, "Ц": 5, "Ч" : 5, "Ш": 8, "Щ": 10, "Ъ": 10, "Ы": 4, "Ь": 3,
    "Э": 8, "Ю": 8, "Я": 3
}


def get_random_letter():
    converted_dictionary = list(LETTER_SCORES.keys())
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(letter, number):
    while True:
        word = input(f"Игрок {number} введите слово на букву '{letter}': ")
        if word[0].upper() == letter:
            return word
        else:
            print(f"Слово должно начинаться с буквы '{letter}'. Попробуйте снова")


def calculate_score(word):
    all_scores = []
    for letter in word:
        scores = LETTER_SCORES.get(letter.upper(), 0)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    random_letter = get_random_letter()
    print(f"Начальная буква: {random_letter}")
    first_player_word = get_word_with_letter(random_letter, 1)
    second_player_word = get_word_with_letter(random_letter, 2)
    first_player_score = calculate_score(first_player_word)
    second_player_score = calculate_score(second_player_word)
    print(f"Игрок 1 ввел слово {first_player_word} и заработал {first_player_score}")
    print(f"Игрок 2 ввел слово {second_player_word} и заработал {second_player_score}")
    if first_player_score > second_player_score:
        print("Первый игрок Победил!!!")
    elif second_player_score > first_player_score:
        print("Второй игрок Победил!!!")
    else:
        print("Ничья!!!")


if __name__ == '__main__':
    main()




