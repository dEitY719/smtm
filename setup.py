import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='smtm',
      version='0.1',
      description='make money using algorithm with python',
      long_description=long_description(),
      url='https://github.com/dEitY719/smtm',
      author='dEitY719',
      author_email='deity719@naver.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)
