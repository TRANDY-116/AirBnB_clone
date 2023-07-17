#!/usr/bin/python3
"""
   Command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
        command processors
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
            Exit the program
        """
        return True

    def do_EOF(self, line):
        """
            Exit the program
        """
        return True

    def emptyline(self):
        """
            Do nothing when an empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
