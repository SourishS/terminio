from terminio.commandexecutor.commandexecutor import CommandExecutor

class cat(CommandExecutor):
    def __init__(self, session):
        super(cat, self).__init__(session)

    def execute_command(self, args):
        print(args)
