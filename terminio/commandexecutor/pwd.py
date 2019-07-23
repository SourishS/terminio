from terminio.commandexecutor.commandexecutor import CommandExecutor

class pwd(CommandExecutor):
    """docstring for put"""
    def __init__(self, session):
        super(pwd, self).__init__(session)


    def execute_command(self, cwd, args):
        self.print(cwd, end='\n')
