#!/usr/bin/python3
""" console class """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    
    prompt = '(hbnb)'
    
    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            self.b = BaseModel()#change this later
            print('{}'.format(self.b.id))
            self.b.save()
    
    def do_show(self, arg):
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif self.b.id != args[1]: #change later
            print("** no instance found **")
        else:
            print(self.b) #change later 
        
    def do_destroy(self, arg):
        args = arg.split(" ")
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] != 'BaseModel':
            print("** class doesn't exist ** ")
        elif len(args) == 1:
            print("** instance id missing **")
        elif self.b.id != args[1]: #change later
            print("** no instance found **")  
        else:
            del self.b 
    
    
        
        

 

if __name__ == '__main__':
   HBNBCommand().cmdloop()

