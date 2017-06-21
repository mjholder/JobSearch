from setuptools import setup

setup(
    name='JobSearch',
    version='1.0',
    packages=['jobsearch'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
