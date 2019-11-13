#!/usr/bin/python3


class User(BaseModel):
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init___(self):
        super().__init__(BaseModel)
