import AssignRunner
import Emails
import Logging

Logging.initialised("RunMorning.py")

AssignRunner.assignRunner(9)
AssignRunner.assignRunner(10)
AssignRunner.assignRunner(11)
AssignRunner.assignRunner(12)

Emails.EmailRunners(9)
Emails.EmailRunners(10)
Emails.EmailRunners(11)
Emails.EmailRunners(12)
