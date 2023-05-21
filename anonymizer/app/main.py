#!/usr/bin/python
# -*- coding: utf-8 -*-
from faker import Faker
import csv
import os
from helpers import deletefiles, hash

fake_up = Faker()
headers = [
    "Firstname",
    "Lastname",
    "DOB",
    "Phone",
    "Address",
    "Email",
]
anonymzed_columns = ["Firstname", "Lastname", "Address"]
row_count = 100


cust_data_csv = os.path.join(os.getcwd(), "data", "raw", "customer_data.csv")
cust_data_anonymized_csv = os.path.join(
    os.getcwd(), "data", "processed", "customer_data_anonymized.csv"
)

# Clear out raw & processed sub-directories of "customer_data.csv" &
# "customer_data_anonymized.csv"

deletefiles(cust_data_csv, cust_data_anonymized_csv)

# Create data for "customer_data.csv"

with open(cust_data_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the headers

    writer.writerow(headers)

    # Write the rows

    for _ in range(row_count):
        row = [
            fake_up.first_name(),
            fake_up.last_name(),
            fake_up.date_of_birth(),
            fake_up.phone_number(),
            ", ".join(fake_up.address().splitlines()),
            fake_up.email(),
        ]
        writer.writerow(row)

# Anonymize columns defined in anonymzed_columns

with open(cust_data_csv, "r", newline="") as sourcecsvfile:
    reader = csv.DictReader(sourcecsvfile)

    with open(cust_data_anonymized_csv, "+a", newline="") as targetfile:
        writer = csv.DictWriter(targetfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            for key, value in row.items():
                if key in anonymzed_columns:
                    row[key] = hash(value)
                else:
                    row[key] = value

            writer.writerow(row)
