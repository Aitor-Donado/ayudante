from setuptools import setup, find_packages

setup(
    name="ayudante",
    version="0.1.0",
    description="Repositorio de ayuda para EDA y Machine Learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scipy",
    ],
    python_requires=">=3.10",
)