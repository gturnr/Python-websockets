import websocket, os
import _thread
import time


def on_message(ws, message):
    print (message)
    os.system('spotify-remote play ' + message)

def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("closed connection")

def on_open(ws):
    def run(*args):
        ws.send('play')

    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()
