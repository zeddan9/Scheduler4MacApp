import subprocess
import sys
import schedule
import time


def start_program(program_name):
    f = open("log", "w+")
    args = ["open", program_name]
    try:
        subprocess.check_call(args)
        f.write("Success this time!\n")
    except:
        f.write("Unexpected Error:", sys.exc_info()[0])
    f.close()


def kill_program(program_name):
    f = open("log", "w+")
    args = ["killall", program_name]
    try:
        subprocess.check_call(args)
        f.write("Successfully kill this time!\n")
    except:
        f.write("Unexpected Error:", sys.exc_info()[0])
    f.close()


def main():
    startp = "/Applications/Backup and Sync.app"
    killp = "Backup and Sync"
    schedule.every().day.at("23:59").do(start_program, startp)
    schedule.every().day.at("07:00").do(kill_program, killp)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
