app_name = "order_tray_app"
app_title = "Order Tray"
app_publisher = "JB Grocers"
app_description = "Order Tray - Real-time fulfillment UI for JB Grocers, served from Frappe"
app_email = "info@jbgrocers.com"
app_license = "MIT"

# This app has no doctypes, patches, or fixtures.
# It exists solely to serve the built Order Tray React app
# as a static website page from within the jbgrocers Frappe site.
#
# The React app itself talks to Frappe's existing REST API
# and Socket.io real-time updates -- this app does NOT add any
# new backend logic, only a webpage that serves the frontend files.

# No website_context, no scheduler events, no doc events needed.
