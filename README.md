## *Installation:*

### <ins>To clone HBNB with SSH:
```bash
Git clone git@github.com:avid-lei/AirBnB_clone.git
```
### <ins>To clone HBNB with HTTPS:
```bash
Git clone https://github.com/avid-lei/AirBnB_clone.git
```
## *Usage:*

Command
```bash
./console
```
will output the following prompt:
```bash
(hbnb)
```
after which your HBNB app is ready to make your life better!

## *Accepted commands:*
| Command   | Description | Usage example |
| --------- | ----------- | ------- |
| `help`      | lists available commands or details help with a specific command | `help <command>` |
| `all`       | shows all instances of a Class | `all <object>` |
| `create`    | creates a new instance of a Class | `create <object>` |
| `destroy`   | destroys an instance of a Class via ID | `destroy <object> <id>` |
| `show` | shows object's attributes | `show <object> <id>` |
| `update`    | updates instance of a Class | `update <object> <id> <attribute> <value>` |
| `quit`      | command to exit the program | `quit` |
| `EOF`       | command ro exit the program | `EOF` |

### Objects:
BaseModel, City, Place, Amenity, Review, User, State

## *Examples:*
The command
```bash
(hbnb) help create
```
will produce the following output:
```bash
Create new instance of class
```
explaining that the command "create" will create a new instance of a class.
Thus:
```bash
(hbnb) create User
```
will return ID of the newly created instance:
```bash
4e204e6f-a941-4627-b8a1-7727a793b939
```
The command:
```bash
(hbnb) show User 4e204e6f-a941-4627-b8a1-7727a793b939
```
will output all attributes of the object User:
```bash
[User] (a2c8801a-c02c-4289-9397-bef663e5b59e) {'updated_at': datetime.datetime(2019, 11, 14, 10, 52, 53, 299902), 'id': 'a2c8801a-c02c-4289-9397-bef663e5b59e', 'created_at': datetime.datetime(2019, 11, 14, 10, 52, 53, 299860)}
```
To update/add a value of the object's attribute, use the command ```update``` followed by the name of the Class, instance ID, name of the attribute and its new value:
```bash
(hbnb) update User 4e204e6f-a941-4627-b8a1-7727a793b939 first_name "Diva"
```
To delete object User:
```bash
(hbnb) destroy User 4e204e6f-a941-4627-b8a1-7727a793b939
```
The following example shows an attempt to access the deleted object:
```bash
(hbnb) show User 4e204e6f-a941-4627-b8a1-7727a793b939
** no instance found **
```
Exiting the program:
```bash
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~$
```
## *Built with:*

  * Python programming language

## *Authors:*
  * [Diva Lei]
  * [Sasha Mapatelian]

## *Bugs:*
If you have encountered any unexpected behaviour, contact us at:

Diva Lei <810@holbertonschool.com> \
Sasha Mapatelian <526@holbertonschool.com>

\
\
\
© 2019 DivaS Inc.\
All rights reserved.
