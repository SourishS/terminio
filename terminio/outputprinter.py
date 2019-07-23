import sys

class OutputPrinter():
    def print(self, message, end):
        sys.stdout.write(message + end)
        sys.stdout.flush()