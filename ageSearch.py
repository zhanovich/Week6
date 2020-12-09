#!/usr/bin/env python3

import os
from connection import executeSelect

def ageSearch():
  minAge = input("\n  Enter Minimum Age: ")
  maxAge = input("  Enter Maximum Age: ")

  # SQL to search by age range
  sql = '''
    SELECT
      person_name,
      street_address,
      city,
      state,
      zip_code,
      active_phone_number
    FROM AddressBook.people_address
    JOIN Addressbook.people_master
      ON people_address.person_id = people_master.person_id
    JOIN AddressBook.addresses
      ON people_address.address_id = addresses.address_id
    WHERE end_date IS NULL
      AND TIMESTAMPDIFF(YEAR, person_DOB, CURDATE()) BETWEEN {} AND {};
  '''.format(minAge, maxAge)

  # Execute the query
  executeSelect(sql)
