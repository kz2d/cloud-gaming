import screenShow.main as screenshow
import sockett.main as sockett
import time, sys, threading, time, pickle


class Server:
    def __init__(self):
        self.frame=0
        self.socket=sockett.Socket()
        self.settings=self.socket.get().decode('utf-8')
        self.settings=[a for a in self.settings.split("-")]
        print(self.settings)
        self.screen=screenshow.ShowWindow(self.settings[0],self.settings[1])


    def show(self):
        i=0
        while True:
            if self.frame==0:
                i+=1
                if i>30:
                    break
                time.sleep(0.01)
                continue
            t=time.time()
            self.screen.show(self.frame)
            print(sys.getsizeof(self.frame),'lll')
            t=1/60-time.time()+t
            if t>0:
                time.sleep(t)

    def mainLoop(self):
        threading._start_new_thread(self.show,())
        t=time.time()
        while True:
            tt=time.time()
            data=self.socket.get()
            data=pickle.loads(data)
            if data==0:
                self.frame=0
                break
            self.frame=data
            
            tt=1/60-time.time()+tt
            print(tt)
            # if tt-0.005>0:
            #     time.sleep(tt)

        print(time.time()-t)
        self.socket.close()
        self.screen.close()

if __name__=='__main__':
    main=Server()
    main.mainLoop()