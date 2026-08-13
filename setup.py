from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="order_tray_app",
    version="0.1.0",
    description="Order Tray - Real-time fulfillment UI for JB Grocers, served from Frappe",
    author="JB Grocers",
    author_email="info@jbgrocers.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
