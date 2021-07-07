// Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Transfer Certificate', {
    setup: function(frm){
        
    
    },
 	refresh(frm)  {
	
    //onload: function(frm){
	//frappe.msgprint("Hello Kunal Mohite form 'onload' event")
		
    //validate: function(frm){
    //frappe.throw("Hello Kunal Mohite from 'validate' event")

    //before_save: function(frm){
	// frappe.throw("Hello Kunal Mohite from 'before_save' event")
	
    //after_save: function(frm){
    //frappe.throw("Hello Kunal Mohite from 'after_save' event")
    
    //before_cancel: function(frm){
    //frappe.throw("Hello Kunal Mohite from 'before_cancel' event")
    
    //after_cancel: function(frm){
    //frappe.throw("Hello Kunal Mohite from 'after_cancel' event")
		
    //before_submit: function(frm){
    //frappe.throw("Hello Kunal Mohite from 'before_submit' event")
	
    //on_submit: function(frm){
    //frappe.throw("Hello Kunal Mohite from 'on_submit' event")
    
 //-----------------------------------------------------------------------------
 
           // Message Print event
    // after_save: function(frm){
    //     frappe.msgprint({
    //         title:__("Notification"),
    //         indicator:  'blue',
    //         message:__('Hello World form MsgPrint event')
    //     });
    
//------------------------------------------------------------------------------    
    //Methods to enable / disable the Save button in the form.

// if (frappe.user_roles.includes('Custom Role')) {
//     frm.enable_save();
// } else {
//     frm.disable_save();
// }

// if (frappe.user_roles.includes('Custom Role')) {
//  be   frm.enable_save();
// }

    
		//save form
		//frm.save();
		
		// submit form
        //frm.save('Submit');
		
		//frm.reload_doc();
		
		//frm.refresh_field('contact');
		
       //Set intro text on the top of the form.
       //if (!frm.doc.student_transfer_certificate) {
       //frm.set_intro('Please set the value of Student Information');
       //}
     

       //Change the docfield property of a field and refresh the field
       //frm.set_df_property('reason_for_transfer', 'fieldtype', 'Text');


        //Open Email dialog for this form.
		//frm.email_doc(`Hello ${frm.doc.customer_name}`);
		
		// set the options of the status field to only be [Open, Closed]
        //frm.set_df_property('status', 'options', ['Open', 'Closed'])
        
        // set a field as mandatory
        //frm.set_df_property('contact', 'reqd', 1)
        
        // set a field as read only
        //frm.set_df_property('status', 'read_only', 1)
        
        
        // set priority as mandatory if status is Open
        //frm.toggle_reqd('priority', frm.doc.status === 'Open');
        //frm.set_df_property("age", "read_only", frm.doc.__islocal ? 0 : 1);

// --------------------------------------------------------------------------------

// remove custom button
//frm.remove_custom_button('Click Me');

// frm.add_custom_button('Click Me 1', () => {
//     frappe.msgprint(__('You Clicked Me 1'));
// },'click me')
// frm.add_custom_button('Click Me 2', () => {
//     frappe.msgprint(__('You Clicked Me 2'));
// },'click me')


        //Add Custom Button
		frm.add_custom_button('Hello Kunal', () => {
		    
		    //Prompt message
		  frappe.prompt('Contact', ({ value } ) => {
		      if(value){
		          frm.set_value('contact', value);
		          frm.refresh_field('contact')
		          
		          //Print the message in Dialogue box
 	              frappe.msgprint(__('Contact field updated successfully'));
 	              }
		     })    
		   
	  	});
	},
});
