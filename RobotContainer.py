from wpilib import XboxController
from subsytems.drivetrain import Drivetrain
from commands2 import RunCommand


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

        self.robotDrive.setDefaultCommand(
            RunCommand(
                lambda: self.robotDrive.arcadeDrive(
                    -self.driverController.getRawAxis(1) * 0.5,
                    self.driverController.getRawAxis(2) * 0.65,
                ),
                self.robotDrive,
            )
        )
