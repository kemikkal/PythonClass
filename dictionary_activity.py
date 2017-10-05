#creates a dictionary that has states and the abbriviation of that states

states = {
            'Oregon':'OR',
            'Florida':'FL',
            'California':'CA',
            'New York':'NY',
            'Michigan':'MI'
        }



#creates a dictionary with states and the cities in the states

cities = {

            'CA':'San Fransico',
            'MI':'Florida',
            }

#adding more entries to the cities dictionary

cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

#prints some contents of the cities dictionary
print('-' * 10)
print("NY state has: ", cities['NY'],"\nOR State has:",cities['OR'])

#Prints some states in the states dictionary

print('-' * 10)
for state, abbrev in list(state.items()):
    print(f"{})
