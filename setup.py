from setuptools import setup, find_packages

setup(
    name='steganography',
    version='1.0',
    description='A steganography toolbox',
    author='Thibault Bitenc',
    author_email='thibault.bitenc@tum.de',
    package_dir={'': 'sources'},
    packages=find_packages(where='sources'),
    install_requires=[
          'pillow',
          'numpy'
    ]
)

