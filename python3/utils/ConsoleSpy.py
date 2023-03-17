import sys


class ConsoleSpy:
    def __init__(self, log_file):
        self.console = sys.stdout
        self.log_file = log_file

    def start(self):
        sys.stdout = self

    def stop(self):
        sys.stdout = self.console

    def write(self, message):
        self.console.write(message)
        self.log_file.write(message)
        self.log_file.flush()
