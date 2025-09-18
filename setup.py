from setuptools import setup, find_packages

setup(
    name="saiv",
    version="1.0.0",
    description="Sorting Algorithm Image Visualizer",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.6",
)
