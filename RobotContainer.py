from wpilib import XboxController
from subsytems.drivetrain import Drivetrain
from commands2 import RunCommand
from commands.drivestraight import DriveStraight
import wpilib
import math


class RobotContainer:
    """
    This class hosts the bulk of the robot's functions. Little robot logic needs to be
    handled here or in the robot periodic methods, as this is a command-based system.
    The structure (commands, subsystems, and button mappings) should be done here.
    """

    def __init__(self):
        # Create the driver's controller.
        self.driverController = XboxController(0)

        # Create an instance of the drivetrain subsystem.
        self.robotDrive = Drivetrain()

        # Autonomous routines

        # A simple auto routine that drives forward a specified distance, and then stops.
        self.simpleAuto = DriveStraight(
            7 * 12 / (4 * math.pi) * 360, self.robotDrive
        )

        # A complex auto routine that drives forward, drops a hatch, and then drives backward.
        # self.complexAuto = ComplexAuto(self.drive, self.hatch)

        # Chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to the autonomous command chooser
        self.chooser.setDefaultOption("Simple Auto", self.simpleAuto)
        # self.chooser.addOption("Complex Auto", self.complexAuto)

        # Put the chooser on the dashboard
        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

        self.robotDrive.setDefaultCommand(
            RunCommand(
                lambda: self.robotDrive.arcadeDrive(
                    -self.driverController.getRawAxis(1) * 0.5,
                    self.driverController.getRawAxis(2) * 0.65,
                ),
                self.robotDrive,
            )
        )
