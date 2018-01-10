from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleChat(WebSocket):

    def handleMessage(self):
        data = self.data
        print(data)
        if data == 'play':
            self.sendMessage('spotify:track:7amMgNDcObIDkIXv4xcvc2')

            '''for client in clients:
          if client != self:
             client.sendMessage(self.address[0] + u' - ' + self.data)'''

    def handleConnected(self):
       print(self.address, 'connected')
       for client in clients:
          client.sendMessage(self.address[0] + u' - connected')
       clients.append(self)

    def handleClose(self):
       clients.remove(self)
       print(self.address, 'closed')
       for client in clients:
          client.sendMessage(self.address[0] + u' - disconnected')

print('Python Websocket server - Guy Turner')
server = SimpleWebSocketServer('', 8000, SimpleChat)
server.serveforever()