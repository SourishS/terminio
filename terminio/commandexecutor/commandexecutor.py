class CommandExecutor():
    def __init__(self, session):
        self.session = session
        self.grammer = dict()

    def execute_command(self, cwd, args):
        pass

    def print(self, message, end=' '):
        self.session.printer.print(message, end)