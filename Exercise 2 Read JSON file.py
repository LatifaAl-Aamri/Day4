# Exercise 2
"""
1/Download JSON file or create (countryName, population)
2/Read JSON file in python
3/Ask user to input countryName and population
4/Add inserted input to JSON file
5/search country name that user input and deleted in JSON file
6/send error message if it is empty or nothing
"""

import json
# The save_countries function is defined to save the updated data to the JSON file
def save_countries(data):
    with open('countries.json', 'w') as file:
        json.dump(data, file, indent=4)
# The main function contains the menu loop where the user can choose between adding a country,
# deleting a country, or quitting.
def main():
    with open('countries.json', 'r') as file:
        countries_data = json.load(file)
#     to see the data in json file
    print(countries_data)   
    
    while True:
        print("\nMenu of countries:")
        print("1. Add a country")
        print("2. Delete a country")
        print("3. Quit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            new_country_name = input("Enter the country name: ")
            new_population = int(input("Enter the population: "))
            new_country = {"countryName": new_country_name, "population": new_population}
            countries_data.append(new_country)
            save_countries(countries_data)
            print(f"{new_country_name} added to the JSON file.")
#             print(countries_data)
        elif choice == '2':
            search_country_name = input("Enter the country name to delete: ")
            found_country = None
            for country in countries_data:
                if country['countryName'] == search_country_name:
                    found_country = country
                    break
                    
            if found_country:
                countries_data.remove(found_country)
                save_countries(countries_data)
                print(f"{search_country_name} deleted from the JSON file.")
#                 print(countries_data)
            else:
                print(f"{search_country_name} not found in the JSON file.")
        #The program continues to display the menu until the user chooses to quit.
        elif choice == '3':
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

