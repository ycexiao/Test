"""Unit tests for __version__.py."""

import my_package


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(my_package, "__version__")
    assert my_package.__version__ != "0.0.0"
