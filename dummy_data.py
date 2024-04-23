from faker import Faker

fake = Faker()
print(fake.name())
print(fake.address())
print(fake.date())
print(fake.date_time())
print(fake.date_time_this_century())
print(fake.date_time_this_decade())
print(fake.date_time_this_year())
print(fake.date_time_this_month())
print(fake.date_time_this_week())
print(fake.text())
print(fake.email())