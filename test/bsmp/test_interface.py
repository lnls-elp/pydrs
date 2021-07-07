"""Test commands module."""

import struct
from unittest import TestCase
from unittest.mock import Mock

from pydrs.bsmp import SerialInterface, PyDrsBasePS, Parameters, EntitiesPS


class TestSerialCommandsx0(TestCase):
    """Test BSMP consulting methods."""

    def setUp(self):
        """Common setup for all tests."""

        self._serial = SerialInterface(path="/serial", baudrate=9600)
        self._entities = EntitiesPS()

        self._pwrsupply = PyDrsBasePS(
            iointerface=self._serial, entities=self._entities, slave_address=1
        )

    def test_query_protocol_version(self):
        """Test"""

    def test_query_variable(self):
        """Test"""
        self._pwrsupply.pread_variable(var_id=0, timeout=500)
