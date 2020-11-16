import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LibTXNDCPy",
    version="0.1.0",
    author="Aaron Averett, Bureau of Economic Geology",
    author_email="aaron.averett@beg.utexas.edu",
    description="A library for generating the USGS NDGGDPP's XML metadata format for ingestion into the National Digital (geologic sample) Catalog (NDC).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )

