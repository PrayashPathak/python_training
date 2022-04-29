import csv
sales_file = open('./sales-demo.csv')

sales_dict = csv.DictReader(sales_file)  # Creates a list of dictionaries.

cancelledOrders = []

total_of_cancelled_orders = 0.0

# for line in sales_dict:
#     # lines = line.split(",")
#     print(line)

# for line in sales_dict:
#     # lines = line.split(",")
#     # print(lines)

#     if line['Status'].upper() == 'CANCELLED':
#         cancelledOrders.append(line)

# print(cancelledOrders)


# Computing the total of cancelled orders

# for line in cancelledOrders:
#     print(type(line))
#     total_of_cancelled_orders += float(line['Total'])

# print("Total = ", total_of_cancelled_orders)


# Filtering the data values based on the name of the customer .(name must be 'mohammed' or 'Ramesh')

filtered_list = []

# for names in sales_dict:
#     if names['Customer_Name'].title() == 'Mohammed' or names['Customer_Name'].title() == 'Ramesh':
#         filtered_list.append(names)
# print(filtered_list)


# Version 2 of the method.

for line in sales_dict:
    if line['Customer_Name'].title() in ['Mohammed', 'Ramesh']:
        filtered_list.append(line)

print(filtered_list)

# Filtered Customer file

customer_file = open('custom.csv', 'w')

# fields = ['Invoice_ID', 'Customer_Name',
#   'Product Name', 'Qty', 'Rate', 'Status', 'Total']

# Field names are for filtering the data
fields = ['Customer_Name', 'Total']
writer = csv.DictWriter(customer_file, fieldnames=fields)

# For Writing the headers
# writer.writeheader()

# writer.writerows(filtered_list)

# File Modes
# 'x' -> For creating file for logrotate purpose.


# For writing the selected filednames in the file.


for line in filtered_list:
    value = {
        'Customer_Name': line['Customer_Name'],
        'Total': line['Total']
    }
    writer.writerow(value)

customer_file.close()

# Make a list of Top Customers
# Make a list of Top Selling Customers.
# Convert the previous score file into csv file.
