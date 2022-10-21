import json as js
import csv
from employees import Employee


class JsonGenerator:
    def __init__(self, filename = None):
        self.FileName = filename

    def processcsv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            employees = []
            header = True
            for row in reader:
                if header is False:
                    employees.append(self.loademployees(row))
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


        


if __name__ == "__main__":
    t = JsonGenerator()
    t.processcsv("cmeDeptInfo.csv")