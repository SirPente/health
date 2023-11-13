# Copyright (c) 2023, earthians Health Informatics Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class CustomerReminder(Document):

	

	def before_insert(self):
		
		if self.message_template:
			# Fetch the selected SMS template content
			template = frappe.get_doc("Customer Text Template", self.message_template)
			template_content = template.message_body

			# Replace placeholders with actual values
			customer_name = self.customer
			reminder_items = ", ".join([item.customer_reminder_schedule for item in self.reminder_item])

			# Populate the SMS content
			self.text_content = template_content.format(customer=customer_name, items=reminder_items)

		pass
