import os
from setuptools import setup, find_packages

version = '0.1'

def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()

long_description = "\n\n".join(
    [read('README.rst'),
     read('docs', 'HISTORY.txt'),
    ]
)

setup(name='memopolutils',
      version=version,
      description="Python utils for accessing memopol.lqdn.fr datas",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='python memopol political memory',
      author='Sylvain Boureliou',
      author_email='sylvain.boureliou@gmail.com',
      url='https://github.com/sylvainb/memopolutils',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      )
