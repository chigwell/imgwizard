from setuptools import setup, find_packages

setup(
    name='imgwizard',
    version='0.0.1',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Simple image resizing and caching using wsrv.nl service',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/imgwizard',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)
