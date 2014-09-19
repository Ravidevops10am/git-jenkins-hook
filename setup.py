from distutils.core import setup

setup(
    name='HookD',
    version='0.1.0',
    author='Siddharth Nandagopal',
    author_email='sid.nandhan@gmail.com',    
    scripts=['githooks/postpushhook.py'],
    description='Git Jenkins Hook',
    long_description=open('README.md').read(),
    install_requires=[
        "Python >= 2.7.5",
        "Fabric >= 1.9.0",
    ],
)
