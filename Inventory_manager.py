#MiniProject--Hostel Inventory Manager 
'''Inventory is connected with MySQL Database
   It includes 6 tables-- 1)Guests_details,2)Workers_details 3)Charges 4)Menu 5)Facilities 6)Fee'''
#To add text colors in IDLE
import sys
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")
color.write('          **********Hostel Inventory Manager**********          ',"COMMENT")
print()
#print("___________________________________________")
entry = "- - - - - "
space = '                '
try:
    import mysql.connector
    db_connection = mysql.connector.connect(host = "localhost",user = "root",password = "Krsna@538",database = "inventory_manager")
    cursor = db_connection.cursor()
#CRUD operations
    color.write('            ***** Guests Data *****',"STRING")
    print()
    color.write("   Name      Qualification          Joining_date       Room_no,Share_type, Work_address,  Permanent_Address,  Vacate_date,   guest_no",  "KEYWORD")
    print()
    #Create(Insert)
    #To insert data into the table
    cursor.execute("Insert into Guest_details values('Madhu','B.sc(Computers)','2023-08-28',306,2,'EDRED','Rayachoty','2024-02-03',2)")
    cursor.execute("Insert into Guest_details values('Prabha','M.sc(Mathematics)','2023-08-28',305,5,'SVU','Tirupati','2024-02-03',3)")
    #Read
    #To fetch data from the table
    cursor.execute("select * from Guest_details")
    data = cursor.fetchall()
    for record in data:
      print(record)
    #Update
    #To update the existing data
    cursor.execute("update Guest_details set Sharing_type=%s where Name=%s",(3,'Madhu'))
    #Delete
    #To delete data from the table
    cursor.execute("Delete from Guest_details where Name=%s",('Madhu',))
    #We can also perform CRUD operations for this entities
    #Printing workers_details
    print(entry)
    color.write('            ***** Workers Data *****',"STRING")
    print()
    color.write("  Name       Work_type     Salary    Address ","KEYWORD")
    print()
    cursor.execute("select * from Worker_details")
    data = cursor.fetchall()
    for record in data:
        print(record)
    #printing monthly_charges
    print(entry)
    color.write('            ***** Monthly Charges *****',"STRING")
    print()
    color.write("       Day         Groceries Power Maintanence  Gas Salaries","KEYWORD")
    print()
    cursor.execute("select * from Charges")
    data = cursor.fetchall()
    for record in data:
       print(record)
    #printing Food Menu
    print(entry)
    color.write('            ***** Food Menu *****',"STRING")
    print()
    color.write("    Day        Morning             Afternoon               Night","KEYWORD")
    print()
    cursor.execute("select * from Menu")
    data = cursor.fetchall()
    for record in data:
        print(record)
    #Printing facilities available in the hostel
    print(entry)
    color.write('            ***** Facilities Available *****',"STRING")
    print()
    color.write("Product Quantity","KEYWORD")
    print()
    cursor.execute("select * from facilities")
    data = cursor.fetchall()
    for record in data:
        print(record)
    #print fee details
    print(entry)
    color.write('            ***** Fee details *****',"STRING")
    print()
    color.write("id  Amount Payment_status","KEYWORD")
    print()
    cursor.execute("select * from fee")
    data = cursor.fetchall()
    for record in data:
         print(record)
    print()
except mysql.connector.Error as err:
    print(f"Error:{err}")
finally:
    cursor.close()
    db_connection.close()
