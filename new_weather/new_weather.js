// Copyright (c) 2021, Kunal Mohite and contributors
// For license information, please see license.txt

frappe.ui.form.on('New Weather', {
	 refresh: function(frm) {
		frm.add_custom_button('Accepted', () => {
			//frm.doc.docstatus = 'Accepted'
			//frm.set_df_property('status', 'options', 'accepted')
			frm.set_value("status","accepted")
			frm.save()
		},'Action For BA')
		frm.add_custom_button('Rejected', () => {
			//frm.doc.docstatus = 'Rejected'
			//frm.set_df_property('status', 'options', 'rejected')
			frm.set_value("status","rejected")	
			frm.save()
		},'Action For BA')		
		frm.add_custom_button('Cancel', () => {
			//frm.doc.docstatus = 'Cancel'
			//frm.set_df_propertys('status', 'options', 'cancel')
			frm.set_value("status","cancel")
			frm.save()
		},'Action For BA')
	 }
});
