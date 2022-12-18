from threading import Thread

def back(): 
    import autotimer

def gui():
    import GUI

Thread(target = back).start() 
Thread(target = gui).start()
