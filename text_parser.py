with open('text.md') as file:
    text = file.read()

text_parsed = text.split('*****')

if __name__ == "__main__":
    print(text_parsed[1])    
