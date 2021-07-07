import typing as _typing

from siriuspy.bsmp import (
    Curve as _Curve,
    Entities as _Entities,
    Function as _Function,
    Variable as _Variable,
)
from siriuspy.bsmp import Types as _Types
from siriuspy.pwrsupply.bsmp.constants import ConstPSBSMP as _ConstPSBSMP

from .parameters import Parameters as _Parameters


class EntitiesPS(_Entities):
    """PS Entities."""

    _ps_variables: _typing.Tuple[_Variable] = (
        # --- common variables
        _Variable(eid=0, waccess=False, count=1, var_type=_Types.T_UINT16),
        _Variable(eid=1, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=2, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=3, waccess=False, count=128, var_type=_Types.T_CHAR),
        _Variable(eid=4, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=5, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=6, waccess=False, count=1, var_type=_Types.T_UINT16),
        _Variable(eid=7, waccess=False, count=1, var_type=_Types.T_UINT16),
        _Variable(eid=8, waccess=False, count=1, var_type=_Types.T_UINT16),
        _Variable(eid=9, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=10, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=11, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=12, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=13, waccess=False, count=4, var_type=_Types.T_FLOAT),
        _Variable(eid=14, waccess=False, count=1, var_type=_Types.T_UINT16),
        _Variable(eid=15, waccess=False, count=1, var_type=_Types.T_UINT16),
        _Variable(eid=16, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=17, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=18, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=19, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=20, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=21, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=22, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=23, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=24, waccess=False, count=1, var_type=_Types.T_UINT32),
        _Variable(eid=25, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=26, waccess=False, count=1, var_type=_Types.T_FLOAT),
        _Variable(eid=27, waccess=False, count=1, var_type=_Types.T_UINT32),
        # --- undefined variables
        _Variable(eid=28, waccess=False, count=1, var_type=_Types.T_UINT8),
        _Variable(eid=29, waccess=False, count=1, var_type=_Types.T_UINT8),
        _Variable(eid=30, waccess=False, count=1, var_type=_Types.T_UINT8),
    )

    _ps_functions: _typing.Tuple[_Function] = (
        _Function(eid=_ConstPSBSMP.F_TURN_ON, i_type=(), o_type=(_Types.T_UINT8,)),
        _Function(eid=_ConstPSBSMP.F_TURN_OFF, i_type=(), o_type=(_Types.T_UINT8,)),
        _Function(eid=_ConstPSBSMP.F_OPEN_LOOP, i_type=(), o_type=(_Types.T_UINT8,)),
        _Function(eid=_ConstPSBSMP.F_CLOSE_LOOP, i_type=(), o_type=(_Types.T_UINT8,)),
        _Function(
            eid=_ConstPSBSMP.F_SELECT_OP_MODE,
            i_type=(_Types.T_ENUM,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_RESET_INTERLOCKS,
            i_type=(),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_COMMAND_INTERFACE,
            i_type=(_Types.T_ENUM,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SERIAL_TERMINATION,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_UNLOCK_UDC,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_LOCK_UDC,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_CFG_SOURCE_SCOPE,
            i_type=(_Types.T_UINT32,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_CFG_FREQ_SCOPE,
            i_type=(_Types.T_FLOAT,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_CFG_DURATION_SCOPE,
            i_type=(_Types.T_FLOAT,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(eid=_ConstPSBSMP.F_ENABLE_SCOPE, i_type=(), o_type=(_Types.T_UINT8,)),
        _Function(
            eid=_ConstPSBSMP.F_DISABLE_SCOPE,
            i_type=(),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(eid=_ConstPSBSMP.F_SYNC_PULSE, i_type=(), o_type=()),
        _Function(
            eid=_ConstPSBSMP.F_SET_SLOWREF,
            i_type=(_Types.T_FLOAT,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SLOWREF_FBP,
            i_type=(_Types.T_FLOAT, _Types.T_FLOAT, _Types.T_FLOAT, _Types.T_FLOAT),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SLOWREF_READBACK_MON,
            i_type=(_Types.T_FLOAT,),
            o_type=(
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SLOWREF_FBP_READBACK_MON,
            i_type=(
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
            o_type=(
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SLOWREF_READBACK_REF,
            i_type=(_Types.T_FLOAT,),
            o_type=(
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SLOWREF_FBP_READBACK_REF,
            i_type=(
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
            o_type=(
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
        ),
        _Function(
            eid=_ConstPSBSMP.F_RESET_COUNTERS,
            i_type=(),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_CFG_WFMREF,
            i_type=(
                _Types.T_UINT16,
                _Types.T_UINT16,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SELECT_WFMREF,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_GET_WFMREF_SIZE,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT16,),
        ),
        _Function(eid=_ConstPSBSMP.F_RESET_WFMREF, i_type=(), o_type=(_Types.T_UINT8,)),
        _Function(
            eid=_ConstPSBSMP.F_CFG_SIGGEN,
            i_type=(
                _Types.T_ENUM,
                _Types.T_UINT16,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_SIGGEN,
            i_type=(_Types.T_FLOAT, _Types.T_FLOAT, _Types.T_FLOAT),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_ENABLE_SIGGEN,
            i_type=(),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_DISABLE_SIGGEN,
            i_type=(),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_PARAM,
            i_type=(
                _Types.T_PARAM,
                _Types.T_UINT16,
                _Types.T_FLOAT,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_GET_PARAM,
            i_type=(
                _Types.T_PARAM,
                _Types.T_UINT16,
            ),
            o_type=(_Types.T_FLOAT,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SAVE_PARAM_EEPROM,
            i_type=(
                _Types.T_PARAM,
                _Types.T_UINT16,
                _Types.T_UINT16,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_LOAD_PARAM_EEPROM,
            i_type=(
                _Types.T_PARAM,
                _Types.T_UINT16,
                _Types.T_UINT16,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SAVE_PARAM_BANK,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_LOAD_PARAM_BANK,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SET_DSP_COEFFS,
            i_type=(
                _Types.T_DSP_CLASS,
                _Types.T_UINT16,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
                _Types.T_FLOAT,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_GET_DSP_COEFF,
            i_type=(
                _Types.T_DSP_CLASS,
                _Types.T_UINT16,
                _Types.T_UINT16,
            ),
            o_type=(_Types.T_FLOAT,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SAVE_DSP_COEFFS_EEPROM,
            i_type=(
                _Types.T_DSP_CLASS,
                _Types.T_UINT16,
                _Types.T_UINT16,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_LOAD_DSP_COEFFS_EEPROM,
            i_type=(
                _Types.T_DSP_CLASS,
                _Types.T_UINT16,
                _Types.T_UINT16,
            ),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_SAVE_DSP_MODULES_EEPROM,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(
            eid=_ConstPSBSMP.F_LOAD_DSP_MODULES_EEPROM,
            i_type=(_Types.T_UINT16,),
            o_type=(_Types.T_UINT8,),
        ),
        _Function(eid=_ConstPSBSMP.F_RESET_UDC, i_type=(), o_type=()),
    )

    _ps_curves: _typing.Tuple[_Curve] = (
        _Curve(
            eid=0,
            waccess=True,
            count=256,
            nblocks=16,
            var_type=_Types.T_FLOAT,
        ),
        _Curve(
            eid=1,
            waccess=True,
            count=256,
            nblocks=16,
            var_type=_Types.T_FLOAT,
        ),
        _Curve(
            eid=2,
            waccess=False,
            count=256,
            nblocks=16,
            var_type=_Types.T_FLOAT,
        ),
    )

    _ps_parameters = _Parameters()

    def __init__(self):
        """Call super."""
        super().__init__(self._ps_variables, self._ps_curves, self._ps_functions)

    @property
    def parameters(self):
        """Return pwrsupply parameters."""
        return EntitiesPS._ps_parameters
