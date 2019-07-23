from terminio.commandexecutor.commandexecutor import CommandExecutor

class put(CommandExecutor):
    """docstring for put"""
    def __init__(self, session):
        super(put, self).__init__(session)


    def execute_command(self, args):
        print(args)
