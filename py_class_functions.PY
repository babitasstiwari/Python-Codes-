import pandas as pd

class YearError(Exception):
    pass

class EnergyConsumptionData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

def load_data(self):
    return pd.read_excel(self.file_path)

def handle_year_error(self, year_value):
    try:
        year: int(year_value)
        if year < 2000 or year >2030:
            raise YearError("Year is out of range")
        else:
            return year 
    except ValueError:
        return None
    
def clean_data(self):
    self.data['Year'] = self.data['Year'].apply(self.handle_year_error)

def print_data(self):
    print(self.data)

# creating an instance for EnergyConsumptionData class: 
    energy_data = EnergyConsumptionData(r'C:\Users\BabitaTiwari\Desktop\Phython Practice\Energy_Comsumption.xlsx')

# cleaning and printing the data. 
    energy_data.clean_data()
    energy_data.print_data()
    
