from wpilib import run, TimedRobot, Joystick
from subsytems.drivetrain import Drivetrain
from RobotContainer import RobotContainer
import commands2


class Robot(commands2.TimedCommandRobot):

    def __init__(self):
        super().__init__()
        # Instantiate our RobotContainer.
        self.container = RobotContainer()

    def robotInit(self):
        pass

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
