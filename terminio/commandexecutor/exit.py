from terminio.commandexecutor.commandexecutor import CommandExecutor
import sys

class exit(CommandExecutor):
    def __init__(self, session):
        super(exit, self).__init__(session)

    def execute_command(self, cwd, args):
    	sys.exit(0)