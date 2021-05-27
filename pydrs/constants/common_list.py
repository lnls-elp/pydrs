"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """''
======================================================================
                    Listas de Entidades BSMP
        A posição da entidade na lista corresponde ao seu ID BSMP
======================================================================
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" ""

ListVar = [
    "iLoad1",
    "iLoad2",
    "iMod1",
    "iMod2",
    "iMod3",
    "iMod4",
    "vLoad",
    "vDCMod1",
    "vDCMod2",
    "vDCMod3",
    "vDCMod4",
    "vOutMod1",
    "vOutMod2",
    "vOutMod3",
    "vOutMod4",
    "temp1",
    "temp2",
    "temp3",
    "temp4",
    "ps_OnOff",
    "ps_OpMode",
    "ps_Remote",
    "ps_OpenLoop",
    "ps_SoftInterlocks",
    "ps_HardInterlocks",
    "iRef",
    "wfmRef_Gain",
    "wfmRef_Offset",
    "sigGen_Enable",
    "sigGen_Type",
    "sigGen_Ncycles",
    "sigGenPhaseStart",
    "sigGen_PhaseEnd",
    "sigGen_Freq",
    "sigGen_Amplitude",
    "sigGen_Offset",
    "sigGen_Aux",
    "dp_ID",
    "dp_Class",
    "dp_Coeffs",
    "ps_Model",
    "wfmRef_PtrBufferStart",
    "wfmRef_PtrBufferEnd",
    "wfmRef_PtrBufferK",
    "wfmRef_SyncMode",
]

ListCurv = [
    "wfmRef_Curve",
    "sigGen_SweepAmp",
    "samplesBuffer",
    "fullwfmRef_Curve",
    "wfmRef_Blocks",
    "samplesBuffer_blocks",
]

ListFunc = [
    "TurnOn",
    "TurnOff",
    "OpenLoop",
    "ClosedLoop",
    "OpMode",
    "RemoteInterface",
    "SetISlowRef",
    "ConfigWfmRef",
    "ConfigSigGen",
    "EnableSigGen",
    "DisableSigGen",
    "ConfigDPModule",
    "WfmRefUpdate",
    "ResetInterlocks",
    "ConfigPSModel",
    "ConfigHRADC",
    "ConfigHRADCOpMode",
    "EnableHRADCSampling",
    "DisableHRADCSampling",
    "ResetWfmRef",
    "SetRSAddress",
    "EnableSamplesBuffer",
    "DisableSamplesBuffer",
    "SetISlowRefx4",
    "SelectHRADCBoard",
    "SelectTestSource",
    "ResetHRADCBoards",
    "Config_nHRADC",
    "ReadHRADC_UFM",
    "WriteHRADC_UFM",
    "EraseHRADC_UFM",
    "ReadHRADC_BoardData",
]

ListTestFunc = [
    "UdcIoExpanderTest",
    "UdcLedTest",
    "UdcBuzzerTest",
    "UdcEepromTest",
    "UdcFlashTest",
    "UdcRamTest",
    "UdcRtcTest",
    "UdcSensorTempTest",
    "UdcIsoPlaneTest",
    "UdcAdcTest",
    "UdcUartTest",
    "UdcLoopBackTest",
    "UdcComTest",
    "UdcI2cIsoTest",
]

ListHRADCInputType = [
    "Vin_bipolar",
    "Vin_unipolar_p",
    "Vin_unipolar_n",
    "Iin_bipolar",
    "Iin_unipolar_p",
    "Iin_unipolar_n",
    "Vref_bipolar_p",
    "Vref_bipolar_n",
    "GND",
    "Vref_unipolar_p",
    "Vref_unipolar_n",
    "GND_unipolar",
    "Temp",
    "Reserved0",
    "Reserved1",
    "Reserved2",
]

ListPSModels = [
    "FBP_100kHz",
    "FBP_Parallel_100kHz",
    "FAC_ACDC_10kHz",
    "FAC_DCDC_20kHz",
    "FAC_Full_ACDC_10kHz",
    "FAC_Full_DCDC_20kHz",
    "FAP_ACDC",
    "FAP_DCDC_20kHz",
    "TEST_HRPWM",
    "TEST_HRADC",
    "JIGA_HRADC",
    "FAP_DCDC_15kHz_225A",
    "FBPx4_100kHz",
    "FAP_6U_DCDC_20kHz",
    "JIGA_BASTIDOR",
]

ListParameters = [
    "PS_Name",
    "PS_Model",
    "Num_PS_Modules",
    "Command_Interface",
    "RS485_Baudrate",
    "RS485_Address",
    "RS485_Termination",
    "UDCNet_Address",
    "Ethernet_IP",
    "Ethernet_Subnet_Mask",
    "Buzzer_Volume",
    "Freq_ISR_Controller",
    "Freq_TimeSlicer",
    "Control_Loop_State",
    "Max_Ref",
    "Min_Ref",
    "Max_Ref_OpenLoop",
    "Min_Ref_OpenLoop",
    "PWM_Freq",
    "PWM_DeadTime",
    "PWM_Max_Duty",
    "PWM_Min_Duty",
    "PWM_Max_Duty_OpenLoop",
    "PWM_Min_Duty_OpenLoop",
    "PWM_Lim_Duty_Share",
    "HRADC_Num_Boards",
    "HRADC_Freq_SPICLK",
    "HRADC_Freq_Sampling",
    "HRADC_Enable_Heater",
    "HRADC_Enable_Monitor",
    "HRADC_Type_Transducer",
    "HRADC_Gain_Transducer",
    "HRADC_Offset_Transducer",
    "SigGen_Type",
    "SigGen_Num_Cycles",
    "SigGen_Freq",
    "SigGen_Amplitude",
    "SigGen_Offset",
    "SigGen_Aux_Param",
    "WfmRef_ID_WfmRef",
    "WfmRef_SyncMode",
    "WfmRef_Frequency",
    "WfmRef_Gain",
    "WfmRef_Offset",
    "Analog_Var_Max",
    "Analog_Var_Min",
    "Hard_Interlocks_Debounce_Time",
    "Hard_Interlocks_Reset_Time",
    "Soft_Interlocks_Debounce_Time",
    "Soft_Interlocks_Reset_Time",
    "Scope_Sampling_Frequency",
    "Scope_Source",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Password",
    "Enable_Onboard_EEPROM",
]

ListBCBFunc = [
    "ClearPof",
    "SetPof",
    "ReadPof",
    "EnableBuzzer",
    "DisableBuzzer",
    "SendUartData",
    "GetUartData",
    "SendCanData",
    "GetCanData",
    "GetI2cData",
]