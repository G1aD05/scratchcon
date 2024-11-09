from setuptools import setup, find_packages

setup(
    name='scratchcon',
    version='1.2.5-beta',
    packages=find_packages(),
    install_requires=[
        'requests',
        'scratchattach',
        'pyperclip',
        'colorama',
    ],
    author='G1ad0s, webbrowser11',
    author_email="on67703@gmail.com, terpstragraham@gmail.com",
    description='A Python library for interacting with the scratch.mit.edu API',
    long_description="https://github.com/g1ad05/scratchcon",
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