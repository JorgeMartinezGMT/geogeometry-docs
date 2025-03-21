#########################
GeoGeometry Documentation
#########################

**Version**: |release|

.. toctree::
    :maxdepth: 2
    :caption: Documentation
    :hidden:

    geometry_types/index
    user_guide/index
    tutorials/index
    examples/index
    reference/index
    releases/index

Description
===========

GeoGeometry is a high-performance geometry processing library for geotechnical and mining applications.
It is not a pure Python package, relying on compiled extensions through libraries like NumPy and PyVista (which themselves use C/C++ backends) to ensure efficient numerical and 3D geometry operations.




Install
=======

.. tab-set::

    .. tab-item:: pip

        .. code-block:: bash

            pip install geogeometry

    .. tab-item:: conda

        .. code-block:: bash

            conda install -c conda-forge geogeometry




About us
========

.. grid:: 1 1 2 2
    :class-row: sd-align-minor-center

    .. grid-item::

        GeoGeometry is being developed by engineer Jorge Martínez as part of GMT
        to process and analyze geotechnical data. The project serves as the foundation
        for the GeoAssistant suite, a specialized geotechnical library.

