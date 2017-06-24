#!/usr/bin/python

class Patient():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

if __name__ == '__main__':
    patients = []
    patients.append(Patient('John', 'Doe'))
    patients.append(Patient('Jan', 'Kowalski'))
    
    # latwiej, szybciej
    print([patient.name for patient in patients])

    # standardowo
    result = []
    for patient in patients:
        result.append(patient.name)
    print result
