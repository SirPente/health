# Copyright (c) 2023, earthians Health Informatics Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import getdate,add_to_date


class ProcedureServiceRequest(Document):
	
	def on_submit(self):
		self.create_customer_reminder_schedule()

	def create_customer_reminder_schedule(self):
		# Get the Customer Reminder Schedule Template
		template = frappe.get_doc("Customer Reminder Schedule Template", self.customer_reminder_schedule)
		due_date = getdate(self.due_date)

		# For each item in the template, create a Customer Reminder Schedule
		for item in template.customer_reminder_item:
			trigger_time = item.trigger_time
			
			reminder_date = add_to_date(due_date, seconds = trigger_time)

			# Create the Customer Reminder Schedule
			customer_reminder_schedule = frappe.get_doc({
				"doctype": "Customer Reminder Schedule",
				"service_type" : self.service_type,
				#"service_request": self.name,
				"reminder_date": reminder_date
			})

			customer_reminder_schedule.insert(ignore_permissions=True,ignore_mandatory=True)

			customer_reminder_schedule.service_request = self.name

			customer_reminder_schedule.insert(ignore_permissions=True,ignore_mandatory=True)

	pass



