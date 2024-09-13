import random
from datetime import datetime, timedelta

def generate_random_sales_data (start_date,end_date):

    """"
    Generate random sales data for the specified number of rows. 

    Parameters:
    start_date(str) : start date in the format 'YYYY-MM-DD'
    end_date(str): End date in the format 'YYYY-MM-DD'

    Returs: 
    list: List of dictonaries containing sales data for each row. 
    Each dictionary has keys'Date', 'Branch' 'Quantity', 'Price', 'Total'

    """
    
    branches = ['Mumbai', 'Hyderabad', 'Delhi', 'Bangalores']
    sales_data = []

    start_date = datetime.strptime(str(start_date),'%Y-%m-%d')
    end_date = datetime.strptime(str(end_date), '%Y-%m-%d')

    while start_date <= end_date:
     for Branch in branches: 
        Quantity = random.randint(1,100)
        price= round(random.uniform(1.0, 100.0),2)
        total= round(Quantity*price,2)

        sales_data.append({
            'Date': start_date.strftime('%Y-%m-%d'),
            'Branch': branches,
            'Quantity': Quantity,
            'Price': price,
            'Total': total
        })

        start_date +=timedelta(days=1)

    return sales_data

#Example usage: 
start_date = "2024-01-20"
end_date = "2024-01-30"
sales_data = generate_random_sales_data(start_date, end_date)

for sale in sales_data: 
    print(sale)