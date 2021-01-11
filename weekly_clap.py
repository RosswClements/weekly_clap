import schedule
import time
from playsound import playsound

def clap():
    playsound('clapping.mp3')

schedule.every().tuesday.at("20:00").do(clap)

while True:
    schedule.run_pending()
    time.sleep(1)