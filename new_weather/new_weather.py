# Copyright (c) 2021, Kunal Mohite and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class NewWeather(Document):
    pass
@frappe.whitelist(allow_guest=True)   
def wthapi():   
    doc = frappe.get_doc({
         "doctype": "States",
         "state_name": "Maharashtra",
         "child_table":[
             {
               "date": "22-06-2021",
               "temprature": "32",
               "season": "Summer",
             }
        ]
    })
    doc.insert(ignor_permissions=True)