import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ec-cart",
    version="0.0.1",
    author="Sang Nguyen",
    author_email="sang.nguyen@recustomer.co",
    description="ReCustomer Interface package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anviedd/recustomer-interface-sdk.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.27.1',
        'pydantic>=1.9.1',
        'six>=1.16.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=4.4.1'],
)
