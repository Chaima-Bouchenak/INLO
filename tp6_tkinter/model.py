# coding: utf-8

class Individu(object):
    """
    Class to creat record cart of individual in the phone book
    """
    def __init__(self, last_name, first_name, phone, address, city):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.city = city

    def __str__(self):
        return self.last_name.lower() + " - " + self.first_name.lower() + " - " + self.phone.lower() + " - " + self.address.lower() + " - " + self.city.lower()

