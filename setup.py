import os

import numpy
from setuptools import Extension, setup


NUMPY_INCLUDE = numpy.get_include()


setup(
    ext_modules=[
        Extension(
            "volaris.data._libs.rolling",
            ["volaris/data/_libs/rolling.pyx"],
            language="c++",
            include_dirs=[NUMPY_INCLUDE],
        ),
        Extension(
            "volaris.data._libs.expanding",
            ["volaris/data/_libs/expanding.pyx"],
            language="c++",
            include_dirs=[NUMPY_INCLUDE],
        ),
    ],
)
