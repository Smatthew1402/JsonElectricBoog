import json as js
import csv


class JsonGenerator:
    """Generates a Json File from the given csv file. 
        Requires the csv file to be named and formatted specifically
    """
    def __init__(self, filename:str = None):
        """
        Args:
            filename (String, optional):Name of the File to be inported from. 
                                         Should be in format depart+"DeptInfo.csv". Defaults to None.
        """
        self.FileName = filename
        self.employees = []
        self.DeptName = self.FileName[:-12]

    def processcsv(self):
        """Opens the CSV File and loads the employees list

        """
        with open(self.FileName, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = True
            for row in reader:
                if header is False:
                    self.employees.append(self.loademployees(row))
                else:
                    header = False
                
    def loademployees(self, list:list) -> dict:
        """Loads data from the input list into a dict that is returned

        Args:
            list (list): the data list that will be cut into a dict

        Returns:
            dict: A dict with the employee's information
        """
        employeedict = {"Name": list[0]}
        employeedict["Title"] = list[1]
        employeedict["Email"] = list[2]
        employeedict["Phone"] = list[3]
        employeedict["Office"] = list[4]
        employeedict["Bio"] = list[5]
        employeedict["Contact for"] = list[6]
        return employeedict

    def writejson(self):
        """Writes the information in the list of dicts to a json file
        """
        jsonfilename = str(self.DeptName + ".json")
        with open(jsonfilename, 'w') as json:
            js.dump(self.employees, json, indent="    ")
        

        


if __name__ == "__main__":
    t = JsonGenerator("cmeDeptInfo.csv")
    t.processcsv()
    t.writejson()
