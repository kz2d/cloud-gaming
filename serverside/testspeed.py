import screenLoader.main as screen
import sockett.main as sockett
import sys, time
import pickle, marshal, gc
import d3dshot


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
        socket.send(data)
        t=1/60-time.time()+t
        print(t)
        if t>0:
            time.sleep(t)
    socket.send(pickle.dumps([]))
    print(time.time()-tt)

    socket.close()

    screenShot.close()
    print('lol')


if __name__=="__main__":
    gc.disable()
    screenShot=d3dshot.create(capture_output="pil")
    screenShot.capture()
    time.sleep(1)
    screenShot.stop()
    data=pickle.dumps(screenShot.get_frame(0))
    print(sys.getsizeof(data))
    tt=time.time()
    for i in range(120):
        a=pickle.loads(data)
    print(time.time()-tt)