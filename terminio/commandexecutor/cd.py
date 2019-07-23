from terminio.commandexecutor.commandexecutor import CommandExecutor

class cd(CommandExecutor):
    def __init__(self, session):
        super(cd, self).__init__(session)
        self.grammer = {
            'directory' : { 
                    'description' : 'Directory to list',
                    'type' : 'string'
            }
        }


    def execute_command(self, cwd, args):
        if args.directory is None:
        	return cwd
        elif args.directory == '.':
            return cwd
        elif args.directory == '..':
            return '/'.join(cwd.split('/')[0:-1])
        else:
        	return args.directory