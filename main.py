import logging
import logging.config
import os
import argparse
import sys


def main():
    argparser  = argparse.ArgumentParser(prog='terminio')

    argparser.add_argument("--file",
                                help="Connection definition file",
                                action='store')

    argparser.add_argument("--host",
                                help="Host ip where minio is running",
                                action='store')

    argparser.add_argument("--port",
                                help="Host port where minio is running",
                                action='store')

    argparser.add_argument("--accesskey",
                                help="Accesskey for the minio",
                                action='store')

    argparser.add_argument("--secretkey", "-k",
                                help="Secreckey for the minio",
                                action='store')

    argparser.add_argument("--script", 
                                help="Execute a script and exit", 
                                action='store')

    args = argparser.parse_args()

    from terminio.config import ConfigLoader
    host, port, accesskey, secretkey = ConfigLoader().load_configuration(args)

    from terminio.minioutils import MinioClient, LoginError
    try:
        session = MinioClient().login(host, port, accesskey, secretkey)

        from terminio.mshell import MShell
        shell = MShell(session)
        if args.script:
            shell.execute_command(args.script)
        else:
            shell.open()
    except LoginError as e:
        print(e.message)

if __name__ == '__main__':
    sys.exit(main())