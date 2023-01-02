from faker import Faker
import pandas as pd
from tqdm.auto import tqdm


def customer_data(out_file, number_of_records):
    print("Generating customer data...")
    fake = Faker()
    data_list = []
    for i in tqdm(range(number_of_records)):

        columns_list = ['first_name', 'last_name', 'email', 'email-2',
                        'phone_number', 'address', 'city', 'state', 'zipcode', 'country', 'credit_card_1', 'credit_card_2', 'job', 'bank']
        data_list.append([fake.first_name(), fake.last_name(), fake.email(), fake.email(), fake.phone_number(), fake.address(), fake.city(), fake.state(), fake.zipcode(), fake.country(), fake.credit_card_number(), fake.credit_card_number(), fake.job(), fake.iban()])

    print("Writing customer data to csv file...")
    df = pd.DataFrame(data_list, columns=columns_list)
    df.to_csv(out_file, mode='w', index=False)


customer_data(out_file='customer_data_complex.csv', number_of_records=1000000)
