#!/usr/bin/env python3

import os
from connection import executeSelect

def exactNameSearch():
  name = input("\n  Enter Exact Name: ")

  # SQL to search by exact name
  sql = '''
    SELECT
      person_name,
      street_address,
      city,
      state,
      zip_code,
      active_phone_number
    FROM AddressBook.people_address PA
    JOIN Addressbook.people_master M
      ON PA.person_id = M.person_id
    JOIN AddressBook.addresses A
      ON PA.address_id = A.address_id
    WHERE end_date IS NULL
      AND LOWER(person_name) = LOWER('{}');
  '''.format(name)

  # Execute the query
  executeSelect(sql)

def partialNameSearch():
  name = input("\n  Enter Partial Name: ")

  # SQL to search by partial name
  sql = '''
    SELECT
      person_name,
      street_address,
      city,
      state,
      zip_code,
      active_phone_number
    FROM AddressBook.people_address PA
    JOIN Addressbook.people_master M
      ON PA.person_id = M.person_id
    JOIN AddressBook.addresses A
      ON PA.address_id = A.address_id
    WHERE end_date IS NULL
      AND LOWER(person_name) LIKE LOWER('%{}%');
  '''.format(name)

  # Execute the query
  executeSelect(sql)
