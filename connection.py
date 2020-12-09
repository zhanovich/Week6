#!/usr/bin/env python3

import pymysql

#DB connection information
HOST = 'localhost'
USER = 'root'
PASSWORD = 'password'
DB = 'AddressBook'

# Print sql result

def printRecord(row):
  # Print record for user.
  print("---------------------------------------")
  print("\n\tName: ", row['person_name'])
  print("\tAddress: ", row['street_address'])
  print("\t{}, {} {}".format(row['city'], row['state'], row['zip_code']))
  print("\tPhone: ", row['active_phone_number'])
  print("\n---------------------------------------\n")


# connect and execute select sql statement
def executeSelect(statement):
  connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )
  
  try:
      with connection.cursor() as cursor:
        cursor.execute(statement)
        records = cursor.fetchall()
        if cursor.rowcount > 0:
          for row in records:
            printRecord(row)
        else:
          print("\n")
          print("\n  No records found.")
          print("\n\n")
  finally:
    connection.close()
