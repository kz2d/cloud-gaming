import screenLoader.main as screen
import sockett.main as sockett
import sys, time
import pickle


class Server:
    def __init__(self):
        self.screenShot=screen.ScreenRecorderInterface()
        self.socket=sockett.Sockett()
        settings=f"{self.screenShot.height}-{self.screenShot.width}"
        self.socket.send(settings.encode('utf-8'))


    
    def mainLoop(self):
    
        tt=time.time()
        for i in range(120):
            t=time.time()
            
            self.socket.send(pickle.dumps(self.screenShot.takeScreen()))
            t=1/25-time.time()+t#frame controller 25
            print(t)
            if t>0:
                time.sleep(t)
        self.socket.send(pickle.dumps(0))
        print(time.time()-tt)



    def close(self):
        self.socket.close()

        self.screenShot.close()
        print('Closed')


if __name__=="__main__":
    s=Server()
    while True:
       s.mainLoop()