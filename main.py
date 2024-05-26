def main():
    book = read()
    count = word_count(book)
    chars = char_count(book)
    print(f"""
--- Begin report of books/frankenstein.txt
{count} words found in the document"
""")
    for item in chars:
        print(f"The '{item['character']}' character was found {item['num']} times")
    print('--- End report ---')
def read():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
def word_count(string):
    words = string.split()
    count = 0
    for i in words:
        count += 1
    return count
def char_count(string):
    lowered_string = string.lower()
    chars = dict.fromkeys(char_range('a','z'), 0)
    for key in chars:
        for letter in lowered_string:
            if key == letter:
                chars[key] += 1
    char_list = []
    chars_sorted = []
    for char, count in chars.items():
        char_dict = {"character": char, "num": count}
        char_list.append(char_dict)
    char_list.sort(reverse = True, key=lambda item: item["num"])

    return char_list
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

main()
