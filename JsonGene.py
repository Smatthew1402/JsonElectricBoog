import json as js
import csv
from socket import setdefaulttimeout
from tkinter import W
from employees import Employee


class JsonGenerator:
    def __init__(self, filename = None):
        self.FileName = filename
        self.employees = []
        self.DeptName = self.FileName[:-12]

    def processcsv(self):
        with open(self.FileName, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = True
            for row in reader:
                if header is False:
                    self.employees.append(self.loademployees(row))
                else:
                    header = False
                
        #Load data from the csv into a list of employees
                
    def loademployees(self, list):
        employeedict = {"Name": list[0]}
        employeedict["Title"] = list[1]
        employeedict["Email"] = list[2]
        employeedict["Phone"] = list[3]
        employeedict["Office"] = list[4]
        employeedict["Bio"] = list[5]
        employeedict["Contact for"] = list[6]
        return employeedict

    def writejson(self):
        jsonfilename = str(self.DeptName + ".json")
        with open(jsonfilename, 'w') as json:
            js.dump(self.employees, json, indent="    ")
        

        


if __name__ == "__main__":
    t = JsonGenerator("cmeDeptInfo.csv")
    t.processcsv()
    t.writejson()
