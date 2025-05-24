|Icon| |title|_
===============

.. |title| replace:: my-package
.. _title: https://billingegroup.github.io/my-package

.. |Icon| image:: https://avatars.githubusercontent.com/billingegroup
        :target: https://billingegroup.github.io/my-package
        :height: 100px

|PyPI| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/billingegroup/my-package/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/billingegroup/my-package/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/billingegroup/my-package/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/billingegroup/my-package

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/my-package
        :target: https://anaconda.org/conda-forge/my-package

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPI| image:: https://img.shields.io/pypi/v/my-package
        :target: https://pypi.org/project/my-package/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/my-package
        :target: https://pypi.org/project/my-package/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/billingegroup/my-package/issues

Python package for doing science.

* LONGER DESCRIPTION HERE

For more information about the my-package library, please consult our `online documentation <https://billingegroup.github.io/my-package>`_.

Citation
--------

If you use my-package in a scientific publication, we would like you to cite this package as

        my-package Package, https://github.com/billingegroup/my-package

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``my-package_env`` ::

        conda create -n my-package_env my-package
        conda activate my-package_env

To confirm that the installation was successful, type ::

        python -c "import my_package; print(my_package.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``my-package_env`` environment, type ::

        pip install my-package

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/billingegroup/my-package/>`_. Once installed, ``cd`` into your ``my-package`` directory
and run the following ::

        pip install .

Getting Started
---------------

You may consult our `online documentation <https://billingegroup.github.io/my-package>`_ for tutorials and API references.

Support and Contribute
----------------------

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/billingegroup/my-package/issues>`_ and/or `submit a fix as a PR <https://github.com/billingegroup/my-package/pulls>`_.

Feel free to fork the project and contribute. To install my-package
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/billingegroup/my-package/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on my-package please visit the project `web-page <https://billingegroup.github.io/>`_ or email Simon Billinge at sb2896@columbia.edu.

Acknowledgements
----------------

``my-package`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.
