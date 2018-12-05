#!/usr/bin/python3

def main():
    with open('data/conspiracy.txt') as text:
        for line in text:
            lines = line.split('\n')
            for smline in lines:
                if (smline != '' and smline != ' '):
                    with open('data/corpora.txt', 'a') as output:
                        output.write(smline.lower() + "\n")

if __name__ == '__main__':
    main()
