import rev
import wpilib
import phoenix5

class RoboMateus(wpilib.TimedRobot):
    def robotInit(self):
        # Configuração dos motores 
        self.motor_esquerdo_frente = phoenix5.WPI_talonSRX(1)
        self.motor_direito_traseira = phoenix5.WPI_talonSRX(2)
        self.motor_esquerdo_traseira = rev.CANSparkMax (3)
        self.motor_direito_frente = rev.CANSparkMax (4)

        # Motor para escalada
        self.victor_escalada = WPI_VictorSPX(5)

        #Importando joystick
        self.joiystick = wpilib(0)

        def teleopPeriodic(self):
            # Controle do arcade drive
            stick_esquerdo = self.wpilib.getRawAxis()
            stick_direito = self.wpilib.getRawAxis()
            
        # Controle de Escalada 
        if self.stick.getRawButton(1):
            self.victor_escalada.set(1.0) # Ligar o motor de escalada 
        else :
            self.victor_escalada.set(0.0) # Desligar o motor de escalada saf

# ENUNCIADO :Usando seus conhecimentos em RobotPy e o código base do Listing 1, crie um repositório
#local com Git para preparar o código do robô. Adapte o código com dois TalonSRX (classe
#phoenix5.WPI_TalonSRX) e dois SparkMAX (classe rev.CANSparkMax) para a tração.
#Coloque também um VictorSPX (classe phoenix5.WPI_VictorSPX) para simular um mecan-
#ismo simples de escalada (ativar e desativar). Você pode escolher qual método de controle de
#tração (Arcade, Cheesy ou Tank) queira usar. Crie duas branches em seu repositório local (uma
#principal e outra de desenvolvimento) e faça dois ou mais commits. Envie as duas branches
#em um repositório remoto e anexe o link na atividade do Classroom.
