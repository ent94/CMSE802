from distutils.core import setup

setup(
    name='TeachingTools',
    version='0.1dev',
    description='Tools to improve course management on lms for instructors',
    autor='Emily T.',
    author_email='thom1618@msu.edu',
    packages=['see',],
    license='MIT',
    #long_description=open('README.md').read(),
    install_requires=[
        'numpy',
        'pandas', 
    ])