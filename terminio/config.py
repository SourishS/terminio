class ConfigLoader():
    def load_configuration(self, args):
        host, port, accesskey, secretkey = self.load_config_file(args.file)

        host        = args.host if args.host else host
        port        = int(args.port) if args.port else port
        accesskey   = args.accesskey if args.accesskey else accesskey
        secretkey   = args.secretkey if args.secretkey else secretkey


        host        = host if host else self.read_from_user('Host')
        port        = port if port else self.read_from_user('Port')
        accesskey   = accesskey if accesskey else self.read_from_user('Accesskey')
        secretkey   = secretkey if secretkey else self.read_from_user('Secretkey')

        return host, port, accesskey, secretkey

    def read_from_user(self, prompt):
        return input("Please enter a value for {}:".format(prompt))

    def load_config_file(self, filename):
        if filename:
            import json
            with open(filename, 'r') as f:
                content = f.read()
                config  = json.loads(content)

                get_from_config = lambda k: config[k] if k in config else None
                return get_from_config('host'), get_from_config('port'), get_from_config('accesskey'), get_from_config('secretkey')
        else:
            return None, None, None, None
