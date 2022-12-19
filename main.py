from threading import Thread

def back(): 
    import autotimer

def gui():
    import GUI

with open('activities.json', 'w') as f:
    pass
Thread(target = back).start() 
Thread(target = gui).start()
