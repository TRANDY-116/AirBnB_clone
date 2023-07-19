#!/usr/bin/python3
"""
   Command interpreter
"""
import cmd


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

    def do_create(self, line):
        """
            Creates a new instance of BaseModel
        """
        if line is None or line == '':
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
            Prints the string representation of an instance
        """
        if line is None or line == '':
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) is not 2:
                print("** instance id missing **")
            else:
                keys = "{}.{}" .format(words[0], words[1])
                if keys not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all[keys])

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id
        """
        if line is None or line == '':
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                keys = "{}.{}".format(words[0], words[1])
                if keys not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[keys]
                    storage.save()

    def do_all(self, line):
        """
            Prints all str rep of all instances based or not on the class name
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
