import typing
import serial
import serial.serialutil

from siriuspy.bsmp.commands import BSMP as _BSMP
from siriuspy.bsmp.entities import Entities as _Entities
from siriuspy.bsmp.serial import IOInterface as _IOInterface

from siriuspy.pwrsupply.bsmp.entities import EntitiesPS as _EntitiesPS
from siriuspy.pwrsupply.bsmp.constants import (
    ConstPSBSMP as _ConstPSBSMP,
    ConstFBP as _ConstFBP
)


class SerialInterface(_IOInterface):
    def __init__(self, path: str, baudrate: int):
        # @notas: Responsável pela comunicação direta c/ o hardware.
        # ": float"
        #  -> typing.Optional[typing.Any]:
        super().__init__()
        self._path = path
        self._baudrate = baudrate
        self._serial: typing.Optional[serial.serialutil.SerialBase] = None
        self._timeout = 1
        self._encoding = 'utf-8'

    def open(self) -> None:
        # 1 x Criar objeto serial
        # 2 x Passar configurações ao objeto
        # 3 x Conectar

        if not self._serial or self._serial.closed():
            # Open serial
            self._serial = serial.Serial(
                port=self._path, baudrate=self._baudrate, timeout=self._timeout
            )

    def close(self) -> None:
        # Caso exista e esteja aberta, feche
        if self._serial and not self._serial.closed():
            # Close serial
            self._serial.close()
            self._serial = None

    def UART_read(self) -> typing.List[str]:
        # Ler todos os bytes da serial, depois podemos usar 
        # características do protocolo para ler apenas o número desejado
        # Converter bytes -> str usando decode
        # Converter str -> List[str]
        #   b"ssssssss".decode('utf-8')
        #    "ssssssss".encode('utf-8')
        if not self._serial or self._serial.closed():
            raise RuntimeError('Unable to open serial port')
        port_readings = self._serial.read_all()
        port_readings = port_readings.decode(self._encoding)
        return [s for s in port_readings]
        
                    
    def UART_write(self, stream:typing.List[str], timeout: float) -> typing.Optional[typing.Any]:
        # Escrita
        raise NotImplementedError

    def UART_request(
        self, stream: typing.List[str], timeout: float
    ) -> typing.Optional[typing.List[str]]:
        # Escrita seguida por uma leitura
        # 1 - Realizar escrita
        self.UART_write(....)
        # 2 - Realizar leitura
        return self.UART_read(....)
        