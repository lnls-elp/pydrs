# Para importar o pydrs, o python/ipython deve ter sido iniciado na pasta onde 
# está o arquivo pydrs.py. Outra alternativa é adicionar o pydrs ao PYTHONPATH
# (Stack Overflow na veia)
import pydrs

# Inicializa uma instância do objeto SerialDRS, que contém argumentos e métodos 
# para comunicação serial com DRS via protocolo BSMP
drs = pydrs.SerialDRS()

# Abre porta serial. Verificar a porta no Gerenciador de Dispositivos
drs.connect('COM6',3000000)

# Lê modelo da fonte (ps_module). Retorna uma lista de 5 valores, sendo o quarto
# número o modelo da fonte (FBP_FAC_UFJF = 15)
drs.Read_ps_Model()

# Lê corrente do módulo de potência 1 (correspondente à primeira placa HRADC)
drs.Read_iMod1()

# Lê corrente do módulo de potência 2 (correspondente à segunda placa HRADC)
drs.Read_iMod2()

# Lê corrente na carga (correspondente à terceira placa HRADC)
drs.Read_iLoad1()
 
# Lê tensão de saída de cada módulo de potência
drs.Read_vOutMod1()
drs.Read_vOutMod2()
drs.Read_vOutMod3()
drs.Read_vOutMod4()

# Lê interlocks. Se estiver com algum interlock, ele deve ser resetado para 
# que a fonte ligue
drs.read_HardInterlock(drs.Read_ps_HardInterlocks())

# Reseta interlocks. Caso a condição que causou o interlock ainda esteja 
# presente, o interlock permanece ativo
drs.ResetInterlocks()

# Liga a fonte. Esta ação fecha o relé de entrada do DC-Link, habilita os sinais
# PWM (inicialmente em 50%, para iLoad = 0A) e inicia a operação em malha
# aberta, com referência em 0%
drs.TurnOn()

# Desliga a fonte. Desliga os PWMs e abre o relé do DC-Link
drs.TurnOff()

# Abre a malha. Referências passam a ser expressas em porcentagem do ciclo de 
# trabalho aplicado aos PWM
drs.OpenLoop()

# Fecha a malha. Referências passam a ser expressas em corrente na carga
drs.ClosedLoop()

# Define novo setpoint na fonte. Esta ação dispara o SamplesBuffer
drs.SetISlowRef(setpoint)

# Desabilita SamplesBuffer. Esta ação mantém o SamplesBuffer ativo até completar
# de preenchê-lo. A partir desse ponto, pode-se ler suas amostras
drs.DisableSamplesBuffer()

# Caso você esteja no cmd/powershell/terminal executando manualmente os
# comandos, para garantir que o SamplesBuffer seja desabilitado rapidamente após
# ter sido habilitado no SetISlowRef(), digitar os comandos da seguinte forma 
# (método alternativo melhor do que aquele do for loop):
#
# 	Obs.: após digitar o "; \" e dar Enter na primera linha, o terminal pula de
# 	      linha e aguarda um novo comando.
#
drs.SetISlowRef(setpoint); \
drs.DisableSamplesBuffer()

# Lê SamplesBuffer. São 4096 amostras, definidas pela função 
# 'WriteBuffer(&IPC_CtoM_Msg.SamplesBuffer, xxxxxx)' presente na rotina do 
# controlador no firmware
buff = drs.Recv_samplesBuffer_allblocks()