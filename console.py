#!/usr/bin/python3
'''Contains the entry point of the command interpreter'''
import cmd
import re
import shlex

from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place


from models.base_model import BaseModel


def parse(arg):
    """
    Method to parse and process input
    """

    # Search for curly braces and square brackets in the input
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    brackets_match = re.search(r"\[(.*?)\]", arg)

    # Split the input string into tokens using shlex
    tokens = shlex.split(arg)

    # Case 1: Neither curly braces nor brackets are found
    if curly_braces_match is None and brackets_match is None:
        return tokens

    # Case 2: Only square brackets are found
    if brackets_match:
        before_brackets = tokens[:brackets_match.start()]
        result = [item.strip() for item in before_brackets]
        result.append(brackets_match.group())
        return result

    # Case 3: Only curly braces are found
    before_curly_braces = tokens[:curly_braces_match.start()]
    result = [item.strip() for item in before_curly_braces]
    result.append(curly_braces_match.group())
    return result



class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - A command-line interface for interacting with HBNB data.

    This class provides a command-line interface for creating and managing instances
    of different classes in the HBNB data storage system. It supports commands for
    creating, showing, exiting, and handling end-of-file events.

    Attributes:
        prompt (str): The command prompt for the shell.
        __classes (set): A set containing the names of available classes.

    Public Methods:
        emptyline(self): Override of the default method to do nothing when the user
        presses Enter with an empty input.

        do_quit(self, arg): Command to exit the shell. Returns True to exit.

        do_exit(self, arg): Command to exit the shell. Returns True to exit.

        do_EOF(self, arg): Handles the End of File (EOF) event. Prints a newline and calls
        the `do_exit` method to exit the shell.

        do_create(self, arg): Creates an instance of a class based on the provided class name.

        do_show(self, arg): Displays the string representation of a class instance.

    Example:
        To create an instance of the 'BaseModel' class, you can enter: `create BaseModel`
    """
    
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """ Called when an empty line is entered."""
        pass
    
    
    def do_quit(self, arg):
        """ Exit the shell."""
        return True
    
    
    def do_exit(self, arg):
        """ Exit the shell """
        return True
    
    def do_EOF(self, arg):
        """
        End of File event [EOF]

        Args:
            arg (string): Ignored. This method does not expect any arguments.
        """
        print = ""
        self.do_exit()

    
    def do_create(self, arg):
        """
        Create an instance of a class

        args:
            arg (str): A string containing the class name
            for which an instance should be created.
        """
        args = parse(arg)

        if len(args) == 0:
            print("** Class name is missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** Class doesn't exist **")
        else:
            # If Valid class name, create an instance and print its ID
            class_name = args[0]
            instance = eval(class_name)()
            print(instance.id)
            storage.save()



    def do_show(self, arg):
        """
         show <class> <id>
            Display string representation of the class instance
        Args:
            arg (str): A string containing the class name and instance ID.

        """
        args = parse(arg)
        objdict = storage.all()

 
        command_cases = {
            "class_name_missing": lambda: print("** class name missing **"),
            "class_not_exist": lambda: print("** class doesn't exist **"),
            "instance_id_missing": lambda: print("** instance id is missing **"),
            "instance_not_found": lambda: print("** no instance found **"),
            "valid_arg": lambda: print(objdict["{}.{}".format(args[0], args[1])])
        }


        if len(args) == 0:
            command_case = "class_name_missing"
        elif args[0] not in HBNBCommand.__classes:
            command_case = "class_not_exist"
        elif len(args) == 1:
            command_case = "instance_id_missing"
        elif f"{args[0]}.{args[1]}" not in objdict:
            command_case = "instance_not_found"
        else:
            command_case = "valid_arg"

        command_cases[command_case]()

def do_destroy(self, arg):
        args = parse(arg)
        objdict = storage.all()

 
        command_cases = {
            "class_name_missing": lambda: print("** class name missing **"),
            "class_not_exist": lambda: print("** class doesn't exist **"),
            "instance_id_missing": lambda: print("** instance id is missing **"),
            "instance_not_found": lambda: print("** no instance found **"),
            "delete_and_save": lambda: self.delete_and_save(objdict, args[0], args[1])
        }


        if len(args) == 0:
            command_case = "class_name_missing"
        elif args[0] not in HBNBCommand.__classes:
            command_case = "class_not_exist"
        elif len(args) == 1:
            command_case = "instance_id_missing"
        elif f"{args[0]}.{args[1]}" not in objdict:
            command_case = "instance_not_found"
        else:
            command_case = "delete_and_save"

        command_cases[command_case]()

def delete_and_save(self, objdict, class_name, instance_id):
    """Delete the instance from the storage and save the changes."""
    del objdict["{}.{}".format(class_name, instance_id)]
    storage.save()


def do_all(self, arg):










 if __name__ == '__main__':
    HBNBCommand().cmdloop()