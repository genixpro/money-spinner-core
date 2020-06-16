from ..core.engine import Engine
from threading import Thread



def main():
    engine = Engine()

    mainLoopThread = Thread(target=lambda: engine.runMainLoop())
    mainLoopThread.start()

    engine.runAPIServer()




