import importlib

class MShell():
    def __init__(self, session):
        self.session = session
        self.prompt  = session.get_prompt()
        self.cwd     = '/'
        
    def open(self):
        while True:
            command = self.show_shell_prompt_for_input()
            self.execute_command(command)


    def show_shell_prompt_for_input(self):
        return input('[minio@{}:{}]> '.format(self.prompt, self.cwd))

    def execute_command(self, command):
        if not command.strip():
            return
        parts = command.split(" ")

        command = parts[0]
        try:
            executor = getattr(importlib.import_module("terminio.commandexecutor."+command),
                               command)
            cmd_exec = executor(self.session)
            _args = self.process_args(command, cmd_exec, parts[1:] if len(parts) > 1 else [])
            outputdir = cmd_exec.execute_command(self.cwd, _args)
            if outputdir:
                if outputdir.startswith('/'):
                    self.cwd = outputdir
                else:
                    if self.cwd == '/':
                        self.cwd = '/' + outputdir
                    else:
                        self.cwd = self.cwd + '/' + outputdir
        except ModuleNotFoundError as e:
            print('Unknown command: ' + command)
        # ModuleNotFoundError

    def process_args(self, command, cmd_exec, args):
        argdfn = cmd_exec.grammer

        import argparse
        argparser  = argparse.ArgumentParser(prog=command)

        for argname, value in argdfn.items():
            description = value['description']
            action = 'store_true' if 'boolean' in value['type'] else 'store'

            if argname.startswith('-'):
                argparser.add_argument(argname,
                                    help=value['description'],
                                    action=action)
            else:
                argparser.add_argument(argname,
                                    help=value['description'],
                                    default=value['default'] if 'default' in value else None,
                                    nargs='?',
                                    action=action)
        _args = argparser.parse_args(args)

        return _args