from setuptools import setup, find_packages

setup(
    name='piosizer',
    version='0.1.0',
    packages=find_packages(),
    license='MIT',
    author='Ran Liu',
    author_email='rliu20@mgh.harvard.edu',
    description='Scans input directories for Piosolver trees, and copies highest EV tree to output directory.',
    entry_points={
        'console_scripts': [
            'piosizer = piosizer.scripts.driver:run'
        ]
    },
    install_requires=[
        'click',
        'numpy',
        'pokersolverquery.py @ git+https://github.com/mitchr1598/pokersolverquery'
    ]
)
