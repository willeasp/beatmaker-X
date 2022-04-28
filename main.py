from playsound import playsound
from threading import Thread
import time
import sys

if len(sys.argv) < 2:
    print("sorry")
    sys.exit(1)
    
print('playing sound using playsound')

with open(sys.argv[1], 'r') as song:
    while 1:
        song.seek(0)    
        while (line := song.readline()):
            for sound in [x.strip() for x in line.split(',')]:
                Thread(target=playsound, args=(f'.\{sound}.wav',)).start()
            time.sleep(0.20)
