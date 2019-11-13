#!/usr/bin/python3
""" console class """
import cmd
import json
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class"""
    
    file_path = "file.json"
    prompt = '(hbnb)'
    def __init__(self):
        """initialization of class"""
        super(HBNBCommand, self).__init__()
        self.ins = []
        self.atr = []


    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Create new instance of class"""
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            b = BaseModel()#change this later
            print('{}'.format(b.id))
            self.ins.append(b)
            self.atr.append(b)
            b.save()
 
    
    def do_show(self, arg):
        """Show Class Instance by ID #"""
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            idn = "({})".format(args[1])
            flag = 0
            for ins in self.ins:
                if idn in ins.__str__():
                    print(ins)
                    flag = 1
            
            if flag == 0:
                print("** no instance found **")

    def emptyline(self):
        """Empty Line does not execute previous command"""
        pass

    def do_destroy(self, arg):
        """destroy instance of class via ID number"""
        args = arg.split(" ")
        flag = 0
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist ** ")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            idn = "({})".format(args[1])
            for ins in self.ins:
                if idn in ins.__str__():
                    self.ins.remove(ins)
                    flag = 1
                
            if flag == 0:
                print("** no instance found *")
            else:
                with open(HBNBCommand.file_path, "r") as f:
                    jobj = json.load(f)
            
                del jobj["BaseModel.{}".format(args[1])]

                with open(HBNBCommand.file_path, "w") as f:
                    json.dump(jobj, f)
 

    def do_all(self, arg):
        """show all instances"""
        args = arg.split(" ")
        if len(args[0]) == 0 or args[0] == 'BaseModel':
            for ins in self.ins:
                print(ins.__str__(), end="")
            print()
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update instance"""
        args = shlex.split(arg)
        if len(args[0]) == 0:
            print("** class name missing **")
        elif not args[0] == "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        #elif not "({})".format(args[1]) in self.ins:
        #    print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            idn = "({})".format(args[1])
            for ins in self.ins:
                if idn in ins.__str__():
                    val = args[3]
                    setattr(ins, args[2], val)
                    ins.save()

    
    
    
        

 

if __name__ == '__main__':
   HBNBCommand().cmdloop()

