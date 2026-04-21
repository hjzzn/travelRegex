import re

inputFileName='浏阳烟花.txt'
outputFileName='out_'+inputFileName

def greet(name):
    print(f"Hello, {name}!")


def modify_text():
    symbol = "!"
    pattern1 = r'^(0\d|1[0-2])(-[0-2]\d|3[0-1])'  #MM-dd日期模式
    pattern2 = r'^([0-1]\d|2[0-4])(:[0-5]\d)'    #hh:mm时间模式

    with open(inputFileName, 'r', encoding='utf-8') as file, \
         open(outputFileName, "w", encoding='utf-8') as fo:
        str1 = ""

        for line in file:
            res1 = line.strip() + symbol

            # Process date pattern
            repl1 = r'\n\1\2!'
            res2 = re.sub(pattern1, repl1, res1)

            # Extract date if matched
            temp = re.match(pattern1, res1)
            if temp:
                str1 = temp.group(1) + temp.group(2)

            # Process time pattern
            repl2 = r'\n' + str1 + r'!\1\2'
            res3 = re.sub(pattern2, repl2, res2)

            print(res3)
            fo.write(res3)


def main():
    # greet("World")
    # print("This code runs when the script is executed directly.")
    modify_text()


if __name__ == "__main__":
    main()
