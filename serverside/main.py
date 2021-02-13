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
            data=self.screenShot.takeScreen()
            print(sys.getsizeof(data))
            self.socket.send(self.screenShot.takeScreen())

            t=1/60-time.time()+t#frame controller 60
            print(t)
            if t>0:
                time.sleep(t)
        self.socket.send(bytes('','utf8'))
        print(time.time()-tt)



    def close(self):
        self.socket.close()

        self.screenShot.close()
        print('Closed')


if __name__=="__main__":
    s=Server()
    s.mainLoop()
    s.close()
    time.sleep(11000)