import re


def greet(name):
    print(f"Hello, {name}!")


def modifyText():
    symbol = "!"
    fo = open("new.txt", "w", encoding='utf-8')
    with open('湘西秋韵.txt', 'r', encoding='utf-8') as file:
        count = 0
        str1 = ""
        while True:
            count += 1
            line = file.readline()
            if not line:
                break

            res1 = line.strip() + symbol
            pattern1 = r'^(0\d|1[0-2])(-[0-2]\d|3[0-1])'
            repl1 = r'\n\1\2!'
            # Search for the pattern
            res2 = re.sub(pattern1, repl1, res1, re.IGNORECASE)
            temp = re.match(pattern1, res1)
            if temp:
                str1 = temp.group(1) + temp.group(2)
            pattern2 = r'^([0-1]\d|2[0-4])(:[0-5]\d)'
            repl2 = r'\n' + str1 + r'!\1\2'
            # Search for the pattern
            res3 = re.sub(pattern2, repl2, res2, re.IGNORECASE)
            print(f"{res3}")
            fo.write(res3)
    fo.close()


def main():
    # greet("World")
    # print("This code runs when the script is executed directly.")
    modifyText()


# test in local

print(__name__)
if __name__ == "__main__":
    main()
