from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="credit-card-stripe-parser",
    version="1.0.0",
    author="Nsfr750",
    author_email="nsfr750@yandex.com",
    description="A Python library for parsing credit card magnetic stripe data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nsfr750/credit-card-stripe-parser",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
    keywords='credit card stripe parser magnetic stripe iso7811',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'mypy>=0.910',
            'flake8>=3.9',
            'black>=21.7b0',
        ],
    },
)
