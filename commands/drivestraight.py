import commands2
from commands2 import PIDCommand
from wpimath.controller import PIDController
from subsytems.drivetrain import Drivetrain
from RobotContainer import RobotContainer
from constants import movement_K_p, movement_K_I, movement_K_D
from subsytems.drivetrain import Drivetrain


# // NOTE:  Consider using this command inline, rather than writing a subclass.  For more
# // information, see:
# // https://docs.wpilib.org/en/latest/docs/software/commandbased/convenience-features.html
class DriveStraight(PIDCommand):
    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, distSetPt: float, drivetrain: Drivetrain):
        super().__init__(
            PIDController(movement_K_p, movement_K_I,
                          movement_K_D),

            drivetrain.m_left_encoder.getPosition,

            distSetPt,

            drivetrain.driveStraight,
            [drivetrain])

    def isFinished(self):
        return self.getController().atSetpoint();
