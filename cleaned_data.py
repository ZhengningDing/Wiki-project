import json
import csv

# import all json datasets
data_list = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for letter in alphabet:
    with open(f'/Users/tamarspectre/Desktop/ACCMET2J/final_project/Compulsive pipers/People/{letter}_people.json') as file:
        data = json.load(file)
        data_list.extend(data)
# print(len(data_list))

# clean the data - keep only people with a birth date, and filter out fictional characters, species, and dead people
cleaned_data = []
for person in data_list:
    keys = person.keys()
    if not ('ontology/deathDate' in keys or 'ontology/deathYear' in keys or 'fictional character' in keys or 'ontology/creator_label' in keys or 'ontology/creator' in keys or 'ontology/species_label' in keys or 'ontology/species' in keys) and \
        ('ontology/birthYear' in keys or 'ontology/birthDate' in keys):
        cleaned_data.append(person)
# print(len(cleaned_data))

# convert gender dataset from .txt file to dictionary
gender_dictionary = {}
gender_txt = open('/Users/tamarspectre/Desktop/ACCMET2J/final_project/wiki_genders.txt')
for line in gender_txt:
    id, gender, name = line.strip().split('\t')
    gender_dictionary[name] = gender
# print(gender_dictionary)

# intersection between gender dataset and cleaned dataset
title_set1 = set()
for person in cleaned_data:
    title_set1.add(person['title'].replace('_',' '))
# print(title_set1)

title_set2 = set(gender_dictionary.keys())
len(title_set1.intersection(title_set2))
# print(len(title_set1.intersection(title_set2)))

# merge the datasets - add gender to a new cleaned dataset
cleaned_gender = []
for person in cleaned_data:
    name = person['title'].replace('_', ' ')
    if name in gender_dictionary.keys():
        person['gender'] = gender_dictionary[name]
        cleaned_gender.append(person)
# print(len(cleaned_gender))

# with open('cleaned.json', 'w') as file:
#     json.dump(cleaned_gender, file)


# person_data = []
# for person in cleaned_gender:
#     person_datum = [person['title']]

#     # add Year to person_datum  
#     if 'ontology/birthYear' in person:
#        person_datum.append(person['ontology/birthYear'])
#     # We are discarding people with multiple birth dates
#     elif 'ontology/birthDate' in person and type(person['ontology/birthDate'])==str:
#        date_parts = person['ontology/birthDate'].split('-')
#        person_datum.append(date_parts[0])
#     else:
#         person_datum.append('NA')

#     # add a bunch of information to person_datum
#     person_datum.append(person['ontology/birthDate'] if 'ontology/birthDate' in person.keys() else "NA")
#     person_datum.append(person['ontology/birthYear'] if 'ontology/birthYear' in person.keys() else "NA")
#     person_datum.append(person['gender'] if 'gender' in person.keys() else "NA")
#     person_datum.append(person['ontology/height'] if 'ontology/height' in person.keys() else "NA")
#     person_datum.append(person['ontology/weight'] if 'ontology/weight' in person.keys() else "NA")
#     person_datum.append(person['ontology/nationality_label'] if 'ontology/nationality_label' in person.keys() else "NA")
#     person_datum.append(person['ontology/occupation_label'] if 'ontology/occupation_label' in person.keys() else "NA")
#     person_datum.append(person['ontology/almaMater_label'] if 'ontology/almaMater_label' in person.keys() else "NA")
#     person_datum.append(person['ontology/award_label'] if 'ontology/award_label' in person.keys() else "NA")
#     person_datum.append(person['ontology/spouse_label'] if 'ontology/spouse_label' in person.keys() else "NA")
#     person_datum.append(person['ontology/child_label'] if 'ontology/child_label' in person.keys() else "NA")
#     person_data.append(person_datum)
# # print(person_data)

# with open('person_data.csv', 'w') as file:
#     headers = ['Name', 'Birth', 'Birth_date', 'Birth_year', 'Gender', 'Height', 'Weight', 'Nationality', 'Occupation', 'Alma_Mater', 'Award', 'Spouse', 'Child']
#     file.write(f'{"|".join(headers)}\n')
#     for line in person_data:
#         file.write(f'{"|".join(str(item) for item in line)}\n')

person_data = []
for person in cleaned_gender:
    person_datum = [person['title']]

    # add Year to person_datum  
    if 'ontology/birthYear' in person:
       person_datum.append(person['ontology/birthYear'])
    # We are discarding people with multiple birth dates
    elif 'ontology/birthDate' in person and type(person['ontology/birthDate'])==str:
       date_parts = person['ontology/birthDate'].split('-')
       person_datum.append(date_parts[0])
    else:
        person_datum.append('NA')

    # add a bunch of information to person_datum
    person_datum.append(person['gender'] if 'gender' in person.keys() else "NA")
    person_datum.append(person['ontology/height'] if 'ontology/height' in person.keys() else "NA")
    person_datum.append(person['ontology/weight'] if 'ontology/weight' in person.keys() else "NA")
    person_datum.append(person['ontology/nationality_label'] if 'ontology/nationality_label' in person.keys() else "NA")
    person_datum.append(person['ontology/occupation_label'] if 'ontology/occupation_label' in person.keys() else "NA")
    person_datum.append(person['ontology/almaMater_label'] if 'ontology/almaMater_label' in person.keys() else "NA")
    person_datum.append(person['ontology/award_label'] if 'ontology/award_label' in person.keys() else "NA")
    person_datum.append(person['ontology/spouse_label'] if 'ontology/spouse_label' in person.keys() else "NA")
    person_datum.append(person['ontology/child_label'] if 'ontology/child_label' in person.keys() else "NA")
    person_data.append(person_datum)
# print(person_data)

with open('person_data.csv', 'w') as file:
    headers = ['Name', 'Birth', 'Gender', 'Height', 'Weight', 'Nationality', 'Occupation', 'Alma_Mater', 'Award', 'Spouse', 'Child']
    file.write(f'{"|".join(headers)}\n')
    for line in person_data:
        file.write(f'{"|".join(str(item) for item in line)}\n')