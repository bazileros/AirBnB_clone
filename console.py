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


# def parse(arg):
#     """
#     Method written to take and parse input before use 
#     """
#     curly_braces = re.search(r"\{(.*?)\}", arg)
#     brackets = re.search(r"\[(.*?)\]", arg)
#     if curly_braces is None:
#         if brackets is None:
#             return [i.strip(",") for i in split(arg)]
#         else:
#             lexer = split(arg[:curly_braces.span()[0]])
#             rlt = [i.strip() for i in lexer]
#             rlt.append(brackets.group())
#             return rlt
#     else:
#         lexer = split(arg[:curly_braces.span()[0]])
#         rlt = [i.strip() for i in lexer]
#         rlt.append(curly_braces.group())
#         return rlt



def parse(arg):
    """
    Method to parse and process input
    """
    curly_braces_match = re.search(r"\{(.*?)\}", arg)
    brackets_match = re.search(r"\[(.*?)\]", arg)
    
    # Use shlex.split to split the input string into tokens
    tokens = shlex.split(arg)
    
    if curly_braces_match is None:
        if brackets_match is None:
            # If neither curly braces nor brackets are found,
            #  return the tokens
            return tokens
        else:
            # Split the tokens before the curly braces,
            # strip extra whitespace, and add the brackets
            # to the result
            before_curly_braces = tokens[:brackets_match.start()]
            result = [item.strip() for item in before_curly_braces]
            result.append(brackets_match.group())
            return result
    else:
        # Split the tokens before the curly braces,
        #  strip extra whitespace,
        #  and add the curly braces to the result
        before_curly_braces = tokens[:curly_braces_match.start()]
        result = [item.strip() for item in before_curly_braces]
        result.append(curly_braces_match.group())
        return result


class HBNBCommand(cmd.Cmd):
    
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
        pass
    
    
    def do_quit(self, arg):
        """Exit the shell."""
        return True
    
    
    def do_exit(self, arg):
        return True
    
    def do_EOF(self, arg):
        print = ""
        self.do_exit()

    def do_create(self, arg):
        """
        create instance of a class
        """
        args = parse(arg)
        if len(args) == 0:
            print("** Class name is missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()


    def do_show(self, arg):
        """
         show <class> <id>
            Display string representation of the class instance
        """
        args = parse(arg)
        objdict = storage.all()

 
        command_cases = {
            "class_name_missing": lambda: print("** class name missing **"),
            "class_not_exist": lambda: print("** class doesn't exist **"),
            "instance_id_missing": lambda: print("** instance id is missing **"),
            "instance_not_found": lambda: print("** no instance found **"),
            "valid_show": lambda: print(objdict["{}.{}".format(args[0], args[1])])
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
            command_case = "valid_show"

        command_cases[command_case]()









if __name__ == '__main__':
    HBNBCommand().cmdloop()