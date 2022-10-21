import json as js
import csv
from tkinter import W
from employees import Employee


class JsonGenerator:
    def __init__(self, filename = None):
        self.FileName = filename
        self.employees = []

    def processcsv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = True
            for row in reader:
                if header is False:
                    #self.employees.append(self.loademployees(row))
                    self.employees.append(row)
                else:
                    header = False
                
        #Load data from the csv into a list of employees
                
    def loademployees(self, list):
        N = list[0]
        T = list[1]
        E = list[2]
        P = list[3]
        O = list[4]
        B = list[5]
        C = list[6]
        return Employee(N,T,E,P,O,B,C)

    def writejson(self):
        pass

        


if __name__ == "__main__":
    t = JsonGenerator()
    t.processcsv("cmeDeptInfo.csv")

    with open('test.json', 'w') as json:
        js.dump(t.employees, json)
