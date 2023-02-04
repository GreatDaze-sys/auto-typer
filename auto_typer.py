import time

def auto_type(text, typing_speed=0.05):
    for char in text:
        print(char, end='')
        time.sleep(typing_speed)

text = input("Enter the text to type automatically: ")
typing_speed = float(input("Enter the typing speed (in seconds): "))

auto_type(text, typing_speed)
