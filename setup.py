from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hm1/__init__.py
from hm1 import __version__ as version

setup(
	name="hm1",
	version=version,
	description="hotel",
	author="naveen",
	author_email="n@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
