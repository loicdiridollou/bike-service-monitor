"""Setup script for the src package"""

from setuptools import find_packages, setup

setup(
    name="bike_monitor_service",
    version="0.0.1",
    description="Package source of the different modules",
    author="Loic Diridollou",
    author_email="loic.diridollou@gmail.com",
    packages=find_packages(),
    package_dir={"": "."},
    include_package_data=True,
)
