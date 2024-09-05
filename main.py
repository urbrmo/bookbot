def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    character_count = count_characters(text)
    char_sorted_list = chars_to_sorted_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


def chars_to_sorted_list(chars_dict):
    sorted_list = []
    for character in chars_dict:
        sorted_list.append({"char": character, "num": chars_dict[character]})
    sorted_list.sort(reverse=True , key=sort_on)
    return sorted_list


def count_characters(text):
    lowered_text = text.lower()
    count = {}
    for character in lowered_text:
        if character not in count:
            count[character] = 1
        else:
            count[character] += 1
    return count


def count_words(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()


main()