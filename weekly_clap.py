import schedule
import time

def clap():
    pass

schedule.every().tuesday.at("20:00").do(clap)


while True:
    schedule.run_pending()
    time.sleep(1)