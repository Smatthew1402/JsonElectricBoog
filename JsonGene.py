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
                
    def loademployees(self, list:list) -> list:
        """Loads data from the input list into a dict that is returned

        Args:
            list (list): the data list that will be cut into a dict

        Returns:
            list: A list containing the employee's name, and a dict of their information
        """
        employeelist = [str(list[0])]
        employeedict = {"Title": list[1]}
        if list[2] != "None Listed":
            employeedict["Email"] = list[2]
        if list[3] != "None Listed":
            employeedict["Phone"] = list[3]
        if list[4] != "None Listed":
            employeedict["Office"] = list[4]
        if list[5] != "None Listed":
            employeedict["Bio"] = list[5]
        if list[6] != "None Listed":
            employeedict["Contact for"] = list[6]
        employeelist.append(employeedict)
        return employeelist

    def writejson(self):
        """Writes the information in the list of dicts to a json file
        """
        jsonfilename = str(self.DeptName + ".json")
        with open(jsonfilename, 'w') as json:
            js.dump(self.employees, json, indent = 0, ensure_ascii=False)
        

        


if __name__ == "__main__":
    t = JsonGenerator("cmeDeptInfo.csv")
    t.processcsv()
    t.writejson()
