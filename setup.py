from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name="vpf-cli",
      version="0.0.1",
      packages=find_packages(),
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      entry_points={
          'console_scripts': [
              'vpfq=vpfq.cli:cli'
          ],
      },
      install_requires=['Click==7.1.2', 'numpy==1.20.0', 'scipy==1.6.0'],
      description="Helper scripts to manage Visitor Prioritization policies with Fair Queue and FIFO models",
      long_description=readme)
