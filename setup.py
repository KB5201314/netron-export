import os.path
import setuptools


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), "r", encoding="utf8") as file:
        return file.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]

    raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netron-export-graph",
    version=get_version("netron_export_graph/__init__.py"),
    author="ImFusion GmbH, Munich",
    author_email="info@imfusion.com",
    description="A helper package for plotting and exporting netron graph figures as PNG or SVG file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imfusion/netron_export_graph",
    packages=setuptools.find_packages(),
    install_requires=[
        'netron==7.1.6',
        'playwright'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
