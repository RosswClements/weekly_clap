import schedule
import time
from playsound import playsound
from pyfiglet import figlet_format

ascii_art = figlet_format("Weekly Clap")
cmd = None

def clap():
    playsound('clapping.mp3')

def main():
    schedule.every().tuesday.at("20:00").do(clap)

    print(ascii_art)
    print("Clapping will play every Tuesday at 8pm...")
    print("Enter 'quit' to stop running:")

    while True:
        schedule.run_pending()
        time.sleep(1)
        cmd = input()
        if cmd == 'quit':
            quit()

main()