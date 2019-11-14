# *Welcome to the world of satisfaction and adventure, my Dear ~~Stranger~~ Friend!*

***
  * Your Uber driver is not coming and you are already 1 minute late to work?
  * Cat peed in your shoe?
  * Did they again lose your credit card at the bar?
  * Maybe you forgot your takeaway in the backpack and now all your stuff is greasy?
  * Or maybe you just saw a story on Instagram where your friends are out at the hottest rooftop bar in the city, but without you?

## *We’ve got your back, comrade!*

The struggle is real, but help is on the way!

While studying here at [Holberton School SF](https://www.holbertonschool.com/), your lifetime defenders and aspiring software engineers (and two humans just like you), The Diva [Diva Lei](https://twitter.com/DivaLei1) and [Sasha with a long last name](https://twitter.com/mapatelian), who know what it’s like to have to deal with a stress, have managed to find an astonishing solution for You!

> ### *May you problems fix themselves, they always do somehow. Live your best life and TRAVEL!*

### "With our <ins>flawlessly</ins> coded and <ins>totally innovative</ins> application you will be able to book a place anywhere you want, whenever you feel the need", reveals one of the founders of brutally successful DivaS Inc. Ms. Lei.

Did you ever want to spend a weekend somewhere in Ghana or Morocco and didn’t want to spend all the money in the world for the hotel rooms? Bingo! Our application will connect you with thousands of real people who are ready to provide you with a place to stay, a place you can truly call a “home away from home”, so you can finally take a deep breath and calm down. Explore the world, be adventurous, INSTALL HBNB RIGHT NOW AND GET THE VPN TO HIDE YOUR IP WHILE TRAVELLING FOR FREE! ONLY NOW!

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
  * Love

## *Authors:*
  * [Diva Lei](https://twitter.com/mapatelian)
  * [Sasha Mapatelian](https://twitter.com/mapatelian)

## *Bugs:*
If you have encountered any unexpected behaviour, contact us at:

Diva Lei <810@holbertonschool.com> \
Sasha Mapatelian <526@holbertonschool.com>

\
\
\
© 2019 DivaS Inc.\
All rights reserved.
