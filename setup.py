"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="datahawk",  # Required
    version="0.0.1",  # Required
    description="A visualization tool for text data",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    url="https://github.com/nihaljn/datahawk",  # Optional
    author="Nihal Jain",  # Optional
    author_email="nihal.b.jain@gmail.com",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    keywords="data visualization, research, natural language processing",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.8",
    install_requires=[
        "flask>=2.0",
        "datasets>=3.0",
        "ijson>=3.3.0"
    ],  # Optional
    # Entry points. The following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        "console_scripts": [
            "datahawk=datahawk.app:main",
        ],
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/nihaljn/datahawk/issues",
        "Funding": "buymeacoffee.com/nihaljn",
        "Say Thanks!": "https://saythanks.io/to/nihal.b.jain",
        "Source": "https://github.com/nihaljn/datahawk",
    },
)
