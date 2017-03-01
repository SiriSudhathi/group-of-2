import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
<<<<<<< HEAD
=======
    

    'passlib'
>>>>>>> dca7915bde803cab8748343c2a6d3b8da4eb4afa
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

<<<<<<< HEAD
setup(name='Testprjt',
      version='0.0',
      description='Testprjt',
=======
setup(name='Prjt',
      version='0.0',
      description='Prjt',
>>>>>>> dca7915bde803cab8748343c2a6d3b8da4eb4afa
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
<<<<<<< HEAD
      main = testprjt:main
      [console_scripts]
      initialize_Testprjt_db = testprjt.scripts.initializedb:main
=======
      main = prjt:main
      [console_scripts]
      initialize_Prjt_db = prjt.scripts.initializedb:main
>>>>>>> dca7915bde803cab8748343c2a6d3b8da4eb4afa
      """,
      )
