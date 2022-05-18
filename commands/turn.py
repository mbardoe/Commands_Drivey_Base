import commands2
from wpimath.controller import PIDController
from constants import turn_K_p, turn_K_I, turn_K_D
from subsytems.drivetrain import Drivetrain


class Turn(commands2.PIDCommand):

    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, turn_set_point: float, drivetrain: Drivetrain):
        super().__init__(
            PIDController(turn_K_p, turn_K_I,
                          turn_K_D),

            drivetrain.gyro.getYaw,

            turn_set_point,

            drivetrain.turn,
            [drivetrain])
        self.getController().setTolerance(2)
        self.getController().enableContinuousInput(0, 360)

    def isFinished(self):
        return self.getController().atSetpoint()
