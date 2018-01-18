import re

commands = {}

def command(match_string):
    def wrapper(func):
        def wrapped(command, matches):
            return func(command, *matches)

        commands[re.compile(match_string)] = wrapped
        return func
    return wrapper


def run_command(command):
    response = None
    for regex, func in commands.items():
        match = regex.match(command)
        if match:
            response = func(command, match.groups())
            break
    return response
