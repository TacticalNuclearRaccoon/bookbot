import os

here = os.getcwd()

def word_counter(book_path):
    with open(book_path, 'r') as f:
        text = f.read()
        words = text.split(' ')
    return len(words)

print(word_counter(f'{here}/books/frankenstein.txt'))

def letter_counter(book_path):
    freq = {}
    with open(book_path, 'r') as f:
        text = f.read()
        low_text = text.lower()
    for letter in set(low_text):
        freq[letter] = low_text.count(letter)
    return freq

words = word_counter(f'{here}/books/frankenstein.txt')
letters = letter_counter(f'{here}/books/frankenstein.txt')

print(f"""--- Begin report of books/frankenstein.txt --- \n
      {words} words were found in the text.
      \n
      The 'a' character was found {letters.get('a')} times
      \
      The 'b' character was found {letters.get('b')} times
      \n
      The 'c' character was found {letters.get('c')} times
      \n
      The 'd' character was found {letters.get('d')} times
      \n
      The 'e' character was found {letters.get('e')} times
      \n
      The 'f' character was found {letters.get('f')} times
      \n
      The 'g' character was found {letters.get('g')} times
      \n
      The 'h' character was found {letters.get('h')} times
      \n
      The 'i' character was found {letters.get('i')} times
      \n
      The 'j' character was found {letters.get('j')} times
      \n
      The 'k' character was found {letters.get('k')} times
      \n
      The 'l' character was found {letters.get('l')} times
      \n
      The 'm' character was found {letters.get('m')} times
      \n
      The 'n' character was found {letters.get('n')} times
      \n
      The 'o' character was found {letters.get('o')} times
      \n
      The 'p' character was found {letters.get('p')} times
      \n
      The 'r' character was found {letters.get('r')} times
      \n
      The 's' character was found {letters.get('s')} times
      \n
      The 't' character was found {letters.get('t')} times
      \n
      The 'u' character was found {letters.get('u')} times
      \n
      The 'v' character was found {letters.get('v')} times
      \n
      The 'x' character was found {letters.get('x')} times
      \n
      The 'y' character was found {letters.get('y')} times
      \n
      The 'z' character was found {letters.get('z')} times
      \n
      --- End report ---

""")
