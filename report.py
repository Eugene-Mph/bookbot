
head = "============ BOOKBOT ============"
word_count_title = "----------- Word Count ----------"
char_count_title = "--------- Character Count -------"
end_line = "============= END ==============="


def sort_chars(char_dict, order=True):
    sorted_chars = sorted(char_dict.items(), key=lambda item: item[1], reverse=order)
    return sorted_chars


def print_report(book, word_count, char_count):
    print(head)
    print(f"Analyzing book found at {book}...")
    print(word_count_title)
    print(f"Found {word_count} total words")
    print(char_count_title)
    items = sort_chars(char_count)

    for item in items:
        if item[0].isalnum():
            print(f"{item[0]}: {item[1]}")
    print(end_line)
    
    