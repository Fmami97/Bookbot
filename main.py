def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(file_path):
    with open(file_path)as f:
        return f.read()

def count_characters(text):
    lowercase_text = text.lower()
    characters_dict = {}
    for character in lowercase_text:
        if(characters_dict.get(character)== None):
            characters_dict[character] = 0
        else:
            characters_dict[character]+= 1
    return characters_dict

def print_report(text):
        num_words = get_num_words(text)
        characters_dict = count_characters(text)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        for character in characters_dict:
             print(f"the '{character}' was found {characters_dict[character]} times")
        print("--- End report ---")

def main():
        text = get_book_text("books/frankenstein.txt")
        print_report(text)

if __name__ == "__main__":
    main()