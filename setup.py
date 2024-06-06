from setuptools import find_packages,setup 


setup(
    name="mcqgenerator",
    version="0.0.1",
    author='Aaditya Seal',
    author_email = 'contact@aadityaseal.com',    
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "scipy",
        "statsmodels"
    ]
)