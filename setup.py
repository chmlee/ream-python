"""setup"""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Chih-Ming Louis Lee",
    author_email="louis@chihminglee.com",
    name='ream',
    license="MIT",
    description="REAM Ain't Markdown",
    version='v0.1-alpha',
    long_description=README,
    url='https://github.com/chmlee/ream-python',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['lark'],
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: Development Status :: 3 — Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Science/Research'
    ]
)
