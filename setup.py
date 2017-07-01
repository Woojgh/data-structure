"""Setup and details on use."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-cov', 'tox']
}

setup(
    name='data-structures',
    desctription='A variety of data structures built with Python.',
    version='0.1',
    author='James Salamonsen, Alex Short',
    author_email='jamessalamonsen@gmail.com',
    license='MIT',
    py_modules=[],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
        ]
    }
)
