# Copyright (c) 2021, Kunal Mohite and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class State(Document):
    pass
@frappe.whitelist(allow_guest=True)   
def stateapi():
    doc = frappe.new_doc('States')
    doc.state_name = 'Tamilnadu'
    doc.city = 'Chennai'
    doc.famous_dish = 'Idli Sambhar'
    doc.save(ignore_permissions=True)
    frappe.db.commit()
    return "New Data Has Been Created successfully"
    
    