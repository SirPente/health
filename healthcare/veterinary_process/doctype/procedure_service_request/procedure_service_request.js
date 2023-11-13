// Copyright (c) 2023, earthians Health Informatics Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Procedure Service Request", {
   refresh: function(frm) {
      frm.set_query('service_type', function() {
         let request_doctypes = [
            "Clinical Procedure Template",
            "Therapy Type",
            "Lab Test Template",
            "Appointment Type",
            "Observation Template",
            "Healthcare Activity"];
         return {
            filters: {
               name: ['in', request_doctypes]
            }
         };
      });
   }
  });
