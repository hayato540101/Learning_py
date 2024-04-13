from setuptools import setup, find_packages

setup(
    name='test_package',
    version='0.1.0',
    packages=find_packages(),
    description='A simple example package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_package',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
