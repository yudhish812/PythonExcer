from pygame import mixer
import datetime

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input("Enter stopper\n")
        if a ==stopper:
            mixer.music.stop()
            break

def log_now(nsg):
    with open("logs.txt","a") as m:
        m.write(f"{nsg} {datetime.datetime.now()}")
if __name__=='__main__':
    musiconloop("1_Water.mp3","stopper")
