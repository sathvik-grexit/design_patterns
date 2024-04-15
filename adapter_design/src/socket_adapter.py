from src.adapter import Adapter
from src.socket import Socket

class SocketAdapter(Adapter):

    def __init__(self) -> None:
        self.socket: Socket = Socket()

    def get_3_volts(self) -> int:
        # you handle other parameters like current flow, heating, AC to DC conversion
        return self.socket.get_volts() // 40
    
    def get_12_volts(self) -> int:
        # you handle other parameters like current flow, heating, AC to DC conversion
        return self.socket.get_volts() // 10
    
    def get_120_volts(self) -> int:
        # you handle other parameters like current flow, heating, AC to DC conversion
        return self.socket.get_volts()