from terminio.commandexecutor.commandexecutor import CommandExecutor

class ls(CommandExecutor):
    def __init__(self, session):
        super(ls, self).__init__(session)
        self.grammer = {
            '-l' : { 
                    'description' : 'use a long listing format',
                    'type' : 'boolean'
            },
            '-r' : { 
                    'description' : 'reverse order while sorting',
                    'type' : 'boolean'
            },
            '-R' : { 
                    'description' : 'recurse into buckets and objects',
                    'type' : 'boolean'
            },
            '-t' : { 
                    'description' : 'sort by modification time, newest first',
                    'type' : 'boolean'
            },
            'directory' : { 
                    'description' : 'Directory to list',
                    'type' : 'string'
            }
        }

    def execute_command(self, cwd, args):
        # if args.directory:
        directory = args.directory or ''
        # else:
        #     directory = cwd

        if directory.startswith('/'):
            completepath = directory
        else:
            completepath = cwd + directory
        parts = completepath.split('/', 2)
        bucket = parts[1]

        dirprefix = parts[2] if len(parts) > 2 else ''

        self.list(bucket, dirprefix, completepath, args)

    def list(self, bucket_name, dirprefix, completepath, args):
        self.print('Directory listing for {}:'.format(completepath), end='\n')

        notnull = lambda v : v if v else '-'

        objectname = lambda n : obj.object_name.split('/')[-2] if obj.object_name.endswith('/') else obj.object_name.split('/')[-1]

        end = '\n' if args.l else '\t'

        if not bucket_name:
            items = self.session.client.list_buckets()
            for b in items:
                if args.l:
                    info = '{:20} {:40} {:30} {:20}'.format('Bucket', b.creation_date.strftime("%c"), '-', b.name)
                else:
                    info = b.name
                self.print(info, end=end)
            self.print('\nTotal {}'.format(len(items)), end='\n\n\n')

            if args.R:
                for b in items:
                    self.list(b.name, '', completepath + b.name, args)            
        else:
            objs = list()
            if dirprefix and not dirprefix.endswith('/'):
                dirprefix = dirprefix + '/'
            items = self.session.client.list_objects(bucket_name, prefix=dirprefix)
            cnt = 0
            for obj in items:
                objs.append(obj)
                cnt += 1
                if args.l:
                    info = '{:20} {} {:30} {:20}'.format(
                        'Directory' if obj.object_name.endswith('/') else 'File',
                        notnull(obj.last_modified), notnull(obj.size), objectname(obj.object_name))
                else:
                    info = obj.object_name
                self.print(info, end=end)

            self.print('\nTotal {}'.format(cnt), end='\n\n\n')

            if args.R:
                for obj in objs:
                    if obj.object_name.endswith('/'):
                        self.list(bucket_name, obj.object_name, completepath + '/' + obj.object_name, args)