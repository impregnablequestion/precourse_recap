flatmate_1 = "niall"
flatmate_2 = "seamus"
flatmate_3 = "martini"

rent = 650
ctax = 150
internet = 20
heating = 90

total_bills = rent + ctax + internet + heating
total_bills_per_person = (rent + ctax + internet + heating)/3

flatmate_1.capitalize()

list_of_flatmates = f"{flatmate_1} {flatmate_2} {flatmate_3}"
list_of_human_flatmates = f"{flatmate_1} {flatmate_2}"
list_of_feline_flatmates = f"{flatmate_3}"
total_utilities = ctax + internet + heating

print(list_of_flatmates)
print(total_bills)
print(total_utilities)
print(total_bills_per_person)
print(list_of_human_flatmates)
print(list_of_feline_flatmates)