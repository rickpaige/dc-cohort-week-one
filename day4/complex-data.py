phone_book = {
    'title': "Yellow Pages",
    'published_date': 1980,
    'contacts': [
        {
        'first_name': 'Ricky',
        'last_name': 'Paige',
        'phone': 8765309,
        },
        {
            'first_name': 'Bob',
            'last_name': 'The Builder',
            'phone': 1234567,
        },
        {
            'first_name': 'Joe',
        }
    ],
}
    
print(phone_book['contacts'][0]['first_name'])

ricky = phone_book['contacts'][0]
print(f'{ricky["first_name"]}')


for contact in phone_book['contacts']:
    print(contacts['first_name'])

def find_by_first_name(first_name):
    for contacts in phone_book['contacts']: 
        if contacts['first_name'] == first_name:
            return (f'{contacts["first_name"]}: {contacts["phone"]}')
    return f"There is no one with the name {first_name}'"


first_name_query = input('Who do you want to search for ')
print(find_by_first_name(first_name_query))
    
def find_contacts_by_first_name(contacts, first_name_query):
    #create empty list to put items into when found
    results = []
    #find all contacts with matching first name
    #put found items in the 'results' list
    for contact in contacts:
        if contact('contacts')