import typing
import serial
import serial.serialutil


from siriuspy.bsmp.serial import (
    IOInterface as _IOInterface,
)

from siriuspy.bsmp.entities import Entities as _Entities
from siriuspy.bsmp.commands import BSMP as _BSMP

from siriuspy.pwrsupply.bsmp.entities import EntitiesPS as _EntitiesPS


class SerialInterface(_IOInterface):
    def __init__(self, path: str, baudrate: int):
        super().__init__()
        self._path = path
        self._baudrate = baudrate
        self._serial: typing.Optional[serial.serialutil.SerialBase] = None

    def open(self) -> None:
        if not self._serial or self._serial.closed():
            # Open serial
            pass

    def close(self) -> None:
        raise NotImplementedError

    def UART_read(self) -> typing.List[str]:
        raise NotImplementedError

    def UART_write(self, stream, timeout: float) -> typing.Optional[typing.Any]:
        raise NotImplementedError

    def UART_request(self, stream, timeout: float) -> typing.Optional[typing.List[str]]:
        raise NotImplementedError


class PyDrsBasePS(_BSMP):
    """Essa classe espera receber como parâmetro um objeto do tipo siriuspy.bsmp.Entities,
    que possui a relação entre endereço e tipo de entidade bsmp que o dispositivo
    que desejamos controlar possui. Caso esse objeto seja nulo, diversas funções
    deverão ser implementadas novamente.
    ver from siriuspy.pwrsupply.bsmp.entities import EntitiesPS"""

    def __init__(self, pru: _IOInterface, slave_address: int, entities: _Entities):
        super().__init__(pru, slave_address, entities)


if __name__ == "__main__":
    ser = SerialInterface(path="/serial.....")
    entities = _EntitiesPS()

    ps = PyDrsBasePS(pru=ser, entities=entities, slave_address=0)
    res = ps.read_variable(var_id=0, timeout=500)
    print(res)
