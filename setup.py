from setuptools import setup, Extension
from setuptools import find_packages
import numpy.distutils.misc_util

setup(name='algorithms',
      version='0.1.3',
      description='algorithms that were implemented during algorithms specialization on coursera',
      url='https://github.com/FelixKleineBoesing/algorithmsCoursera',
      author='Felix Kleine Bösing',
      license='WDL',
      packages=["algorithms"],
      install_requires=['numpy'],
      include_package_data=True,
      zip_safe=False,
      ext_modules=[Extension("algorithms/_chi2", ["c/_chi2.c", "c/chi2.c"])],
      include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
      )