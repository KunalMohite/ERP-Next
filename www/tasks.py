import frappe
import string
import random

def all():
    pass

def cron():
    letters = string.ascii_letters
    note = "".join(random.choice(letters) for i in range(20))
    
    new_note = frappe.get_doc({"doctype":"Note",
    "title": note                 
        })
    new_note.insert()
    frappe.db.commit()