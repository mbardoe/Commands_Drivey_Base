import commands2
import ctre
from wpilib.drive import DifferentialDrive
from wpilib import SpeedControllerGroup


class Drivetrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.gyro = ctre.PigeonIMU(10)
        self.gyro.setYaw(0, 0)

        self.leftMotors = SpeedControllerGroup(ctre.TalonSRX(0).ctre.VictorSPX(1), ctre.VictorSPX(2))
        self.rightMotors = SpeedControllerGroup(ctre.TalonSRX(3), ctre.VictorSPX(4), ctre.VictorSPX(5))

        self.m_right_encoder = ctre.CANCoder(9)
        self.m_left_encoder = ctre.CANCoder(11)

        self.drive = DifferentialDrive(self.leftMotors, self.rightMotors)

    def set(self, left: float, right: float):
        """ a tank drive for the robot."""
        self.drive.tankDrive(left, -right)
        # self.m_left.set(ctre.ControlMode.PercentOutput, left)
        # self.m_right.set(ctre.ControlMode.PercentOutput, -right)

    def arcadeDrive(self, fwd, rot):
        """Drive the robot with standard arcade controls."""
        self.drive.arcadeDrive(fwd, rot)

    def periodic(self):
        pass
