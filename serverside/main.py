import screenLoader.main as screen
import sockett.main as sockett
import sys, time
import pickle

def main():
    #settings
    screenShot=screen.ScreenRecorderInterface()
    socket=sockett.Sockett()
    settings=f"{screenShot.height}-{screenShot.width}"
    socket.send(settings.encode('utf-8'))
    #settings end
    data=pickle.dumps(screenShot.takeScreen())
    
    tt=time.time()
    for i in range(120):
        t=time.time()
        
        print(sys.getsizeof(data))
        socket.send(pickle.dumps(screenShot.takeScreen()))
        t=1/40-time.time()+t#frame controller 40
        print(t)
        if t>0:
            time.sleep(t)
    socket.send(pickle.dumps(0))
    print(time.time()-tt)

    socket.close()

    screenShot.close()
    print('lol')

if __name__=="__main__":
    while True:
       main()