# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tensorwatch",
    version="0.8.5",
    author="Shital Shah",
    author_email="shitals@microsoft.com",
    description="Interactive Realtime Debugging and Visualization for AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/tensorwatch",
    packages=setuptools.find_packages(),
	license='MIT',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    include_package_data=True,
    install_requires=[
          'matplotlib', 'numpy', 'pyzmq', 'plotly', 'torchstat', 'ipywidgets', 
          'nbformat', 'scikit-image', 'nbformat', 'yaml', 'scikit-image', 'graphviz' # , 'receptivefield'
    ]
)
