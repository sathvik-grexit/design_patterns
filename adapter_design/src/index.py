from src.adapter import SocketAdapter

class Charge:
    
    def charge_mobile(self) -> None:
        socket_adapter: SocketAdapter = SocketAdapter()
        mobile_voltage = socket_adapter.get_12_volts()
        print(f"Charging mobile with {mobile_voltage} Volts")


charge = Charge()
charge.charge_mobile()