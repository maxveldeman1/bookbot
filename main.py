def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    char_list = filter_and_list_change(chars_dict)
    print_report(book_path, num_words, char_list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["amount"]

def filter_and_list_change(dict):
    new_list =[]
    for char in dict:
        unique_char = dict[char]
        if char.isalpha():
            new_list.append({"char": char, "amount": unique_char})
    new_list.sort(reverse=True, key=sort_on)
    return new_list   

def print_report(book_path, num_words, char_list ):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for dict in char_list:
        char = dict["char"]
        amount = dict["amount"]
        print(f"The '{char}' character was found {amount} times")

main()
