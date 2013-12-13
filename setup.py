from distutils.core import setup

def main():

    setup(
        name = 'polydatum_sqlalchemy',
        packages=['polydatum_sqlalchemy'],
        package_dir = {'':'src'},
        version = open('VERSION.txt').read().strip(),
        author='Mike Thornton',
        author_email='six8@devdetails.com',
        keywords=['orm', 'polydatum', 'sqlalchemy'],
        license='MIT',
        description='A SqlAlchemy plugin for Polydatum',
        classifiers = [
            "Programming Language :: Python",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        long_description=open('README.rst').read(),
        install_requires = [
            'polydatum',
            'sqlalchemy',
        ],        
    )

if __name__ == '__main__':
    main()