from setuptools import setup, find_packages

setup(
    name='metagpt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Automatically installs the latest compatible version
        'numpy',
        'openai'
    ],
    author='Daniela Perry, Amanda Birmingham',
    author_email='dsperry@ucsd.edu',
    description='Integrating LLMs with a jupyter notebook.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dpear/metagpt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
