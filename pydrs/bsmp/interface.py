import typing
import serial
import serial.serialutil


from siriuspy.bsmp.serial import IOInterface as _IOInterface


class TCPInterface(_IOInterface):
    pass


class SerialInterface(_IOInterface):
    def __init__(self, path: str, baudrate: int):
        super().__init__()
        self._port = path
        self._baudrate = baudrate
        self._serial: typing.Optional[serial.serialutil.SerialBase] = None
        self._encoding = "utf-8"

        self.open()

    def open(self) -> None:
        """Open the serial connection"""

    def close(self) -> None:
        if self._serial:
            self._serial.close()

    def UART_read(self) -> typing.List[str]:
        # @todo: Usar a especificação do bsmp para ler o número correto de bytes
        raise NotImplementedError

    def UART_write(
        self, stream: typing.List[str], timeout: float
    ) -> typing.Optional[typing.Any]:
        raise NotImplementedError

    def UART_request(
        self, stream: typing.List[str], timeout: float
    ) -> typing.Optional[typing.List[str]]:
        # @todo: Usar a especificação do bsmp para ler o número correto de bytes
        self._serial.write(stream)
        _response = self._serial.read_all()
        _decoded = _response.decode(self._encoding)
        return [s for s in _decoded]
