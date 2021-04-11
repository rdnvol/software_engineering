import requests
from bs4 import BeautifulSoup


def main():
    inp = input("Please write URL: ")
    r = requests.get(inp)
    soup = BeautifulSoup(r.text, 'html.parser')
    text = soup.body.getText()
    get_words_frequency(text)
    tags_frequency = get_tags_frequency(soup.recursiveChildGenerator())
    print(f'''links count : {tags_frequency.get('link', 0)}''')
    print(f'''images count : {tags_frequency.get('img', 0)}''')


def get_words_frequency(text):
    frequency = {}
    for word in text.split():
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    print_dictionary(frequency)


def get_tags_frequency(tags_array):
    frequency = {}
    for tag in tags_array:
        if tag.name:
            count = frequency.get(tag.name, 0)
            frequency[tag.name] = count + 1
    print_dictionary(frequency)
    return frequency


def print_dictionary(dictionary):
    for key in dictionary:
        print(f'''{key} : {dictionary[key]}''')


main()
