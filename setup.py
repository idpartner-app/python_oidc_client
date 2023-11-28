from setuptools import setup, find_packages

setup(
    name='python_oidc_client',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'authlib',
        'requests',
    ],
)
