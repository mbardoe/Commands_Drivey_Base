import commands2
from commands2 import PIDCommand
from wpimath.controller import PIDController
from subsytems.drivetrain import Drivetrain
from RobotContainer import RobotContainer


# // NOTE:  Consider using this command inline, rather than writing a subclass.  For more
# // information, see:
# // https://docs.wpilib.org/en/latest/docs/software/commandbased/convenience-features.html
class DriveStraight(PIDCommand):
    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, distSetPt: float):
        super(
            # // The controller that the command will use
            PIDController(Constants.PIDConstants.drivekP, Constants.PIDConstants.driveKI,
                          Constants.PIDConstants.driveKD),
        // This
        should
        return the
        measurement
        () -> (drive.getLeftEncoderDistance() + drive.getRightEncoderDistance()) / 2,
        // This
        should
        return the
        setpoint(can
        also
        be
        a
        constant)
        () -> distSetPt,
        // This
        uses
        the
        output
        output -> {
            drive.driveStraight(output, Constants.PIDConstants.ksetPoint);
        }
        );
        addRequirements(drive);
        drive.resetGryo();
        drive.resetDrivetrainEncoders();
        // Use
        addRequirements()
        here
        to
        declare
        subsystem
        dependencies.
        // Configure
        additional
        PID
        options
        by
        calling
        `getController`
        here.
        }

        // Returns
        true
        when
        the
        command
        should
        end.
        @ Override
        public
        boolean
        isFinished()
        {

    return getController().atSetpoint();

}
}
