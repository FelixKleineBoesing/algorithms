from setuptools import setup, Extension
from setuptools import find_packages
import numpy.distutils.misc_util

setup(name='algorithms',
      version='0.1.3',
      description='algorithms that were implemented during algorithms specialization on coursera',
      url='https://github.com/FelixKleineBoesing/algorithmsCoursera',
      author='Felix Kleine Bösing',
      license='MIT',
      packages=["algorithms"],
      install_requires=['numpy'],
      include_package_data=True,
      zip_safe=False,
      ext_modules=[Extension("algorithms/_apsp", ["c/apsp/_apsp.c", "c/apsp/apsp.c"])],
      include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
      )