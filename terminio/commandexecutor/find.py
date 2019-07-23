from terminio.commandexecutor.commandexecutor import CommandExecutor

class find(CommandExecutor):
    """docstring for find"""
    def __init__(self, session):
        super(find, self).__init__(session)

    def execute_command(self, args):
        print(args)
