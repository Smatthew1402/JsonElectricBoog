class Employee:
    #Name,Title,Email,Phone,Office,Bio,Contact For
    def __init__(self, Name='', Title='', Email='', Phone='', Office='', Bio='', Contact4=''):
        self.Name = Name
        self.Title = Title
        self.Email = Email
        self.Phone = Phone
        self.Office = Office
        self.Bio = Bio
        self.ContactFor = Contact4
    
    def __repr__(self):
        c = ' | '
        return(str((self.Name, c, self.Title, c, self.Email, c, self.Phone, c, self.Office, c, self.Bio, c, self.ContactFor)))
