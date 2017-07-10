from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'tox']
}

setup(
    name='data-structures',
    desctription='A variety of data structures built with Python.',
    version='0.1',
    author='James Salamonsen',
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