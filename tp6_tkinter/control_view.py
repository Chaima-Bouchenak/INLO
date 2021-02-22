# coding: utf-8
import tkinter as tk
from tkinter import Entry, Label, StringVar, Tk, Button, messagebox , filedialog
import subprocess, sys
from model import Individu

# Open GUI window
root = Tk()
root.title("Annuaire d'adresse")
root.geometry("330x200")

# Set up different Entry and Button texts
ids = ["last_name", "first_name", "phone", "address", "city"]
bouton = ["chercher", "inserer", "effacer"]

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

i, j = 0, 0
# Build Entries widgets
for idi in ids:
    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.grid(row=i, column=0, sticky=tk.W+tk.E)

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.grid(row=i, column=1, sticky=tk.W+tk.E)

    i += 1


# Build Buttons widgets
for idi in bouton:
    button = Button(root, text=idi)
    widgets_button[idi] = button
    button.grid(row=i + 1, column=j)

    consulter = tk.Button(root, text="Consulter l'annulaire")
    consulter.grid(row=7, column=1)

    j += 1
# Set defaut dictionnary to store contacts
# Key : User last name
# Value : Complementary informations using Individu Class
dict_annuaire = {}


def user_entry_validation():
    """check that all fields of user input are not empty"""
    if widgets_entry["first_name"].get() != "" \
    and widgets_entry["last_name"].get() != "" \
    and widgets_entry["phone"].get() != ""  \
    and widgets_entry["address"].get() != "" \
    and widgets_entry["city"].get() != "":
        return True
    else:
        return False


def insert_contact():
    """Add a new user contact to the addres book"""
    contact_to_insert = widgets_entry["last_name"].get()
    contact_to_insert = contact_to_insert.lower()
    if user_entry_validation():
        if contact_to_insert not in dict_annuaire.keys():
            contact_new = Individu(widgets_entry["last_name"].get(),
                                   widgets_entry["first_name"].get(),
                                   widgets_entry["phone"].get(),
                                   widgets_entry["address"].get(),
                                   widgets_entry["city"].get()
                                   )
            dict_annuaire[contact_to_insert] = list()
            dict_annuaire[contact_to_insert] = contact_new
            messagebox.showinfo(title="Inseertion nouveau contact",
                                message="Contact entegistré avec succès !")
            save_dict_annuaire_in_file(dict_annuaire)
        else:
            messagebox.showinfo(title="Inseertion nouveau contact",
                                message="Le nom que vous saisissez existe déja dans l'annuaire")
        return dict_annuaire
    else:
        messagebox.showwarning(title="Insertion nouveau contact",
                               message="Erreur! vous devez remplir tout les champs")


def delete_contact():
    """Delete existing contact from the address book"""
    contact_to_delete = widgets_entry["last_name"].get()
    contact_to_delete = contact_to_delete.lower()
    for key in list(dict_annuaire.keys()):
        if contact_to_delete == key:
            del dict_annuaire[key]
            messagebox.showinfo(title="Suppression contact existant",
                                message="Contact supprimé avec succès !")
        else:
            messagebox.showwarning(title="Suppression contact existant",
                                   message="Erreur! le contact n'existe pas dans notre annuaire")

    save_dict_annuaire_in_file(dict_annuaire)


def search_contact():
    """Search for complementary information of the contact in the address book
    input : last_name"""
    contact_target = widgets_entry["last_name"].get()
    contact_target = contact_target.lower()
    for key in dict_annuaire:
        if contact_target == key:
            contact_target_info = dict_annuaire[key]
            messagebox.showinfo(title="Resultat de votre echerche", message=contact_target_info)
        else:
            messagebox.showwarning(title="Recherche contact",
                                   message="Erreur! le contact n'existe pas dans notre annuaire")


def save_dict_annuaire_in_file(data):
    """Save the address book in CSV file"""
    with open("Votre Annuaire d'adresse.csv", 'w') as file:
        file.write("###### ANNUAIRE D'ADRESSES 2021 APP ######\n\n")
        contact = "Contacte(s)"
        informations = "Nom - Prenom - Telephone - Adresse - Ville"
        file.write("%s, %s\n" % (contact, informations))
        for key in data.keys():
            file.write("%s, %s\n" % (key, data[key]))


def browse_annuaire():
    "Browse and open the address book in CSV file by user"
    file_output = filedialog.askopenfilename(parent=root,
                                          initialdir="/home",
                                          initialfile="Votre Annuaire d'adresse.csv",
                                          title="Select a File",
                                          filetypes=(("CSV file",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    print(file_output)
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, file_output])

# Link each fuction to its suitable button


widgets_button[bouton[1]].config(command=insert_contact)
widgets_button[bouton[2]].config(command=delete_contact)
widgets_button[bouton[0]].config(command=search_contact)
consulter.config(command=browse_annuaire)


root.mainloop()
