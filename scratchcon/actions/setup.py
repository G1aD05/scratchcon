from setuptools import setup, find_packages

setup(
    name='scratchcon',
    version='1.1.1-beta',
    packages=find_packages(),
    install_requires=[
        'requests',
        'scratchattach',
    ],
    author='G1ad0s',
    author_email="on67703@gmail.com",
    description='A Python library for interacting with the scratch.mit.edu API',
    long_description=open('README.rst').read(),
    url='https://github.com/G1ad0s/scratchcon',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
)
