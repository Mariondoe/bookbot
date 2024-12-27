print("--- Begin report of books/frankenstein.txt ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
        count = len(words)
    print(f"The book contains {count} words.")

main()

letter_counts = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

def second():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        for letter in file_contents:
            if letter.lower() in letter_counts:
                letter_counts[letter.lower()] += 1
        #print(letter_counts)
    for letter, count in letter_counts.items():
        print(f"the '{letter}' letter was used {count} times.")

second()

print("--- End report of books/frankenstein.txt ---")