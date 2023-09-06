class User:
    def __init__(self, id, fname, lname, email) -> None:
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
    
    def __str__(self) -> str:
        return f"{self.fname} {self.lname} | {self.email} | {self.id}"