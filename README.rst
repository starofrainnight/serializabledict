=================
Serializable Dict
=================


.. image:: https://img.shields.io/pypi/v/serializabledict.svg
    :target: https://pypi.python.org/pypi/serializabledict

.. image:: https://travis-ci.org/starofrainnight/serializabledict.svg
    :target: https://travis-ci.org/starofrainnight/serializabledict.html

.. image:: https://ci.appveyor.com/api/projects/status/github/starofrainnight/serializabledict?svg=true
    :target: https://ci.appveyor.com/project/starofrainnight/serializabledict

A simple serializable dict

* License: Apache-2.0

Features
--------

* Save dict data while it's changed in realtime, so data will safety saved to file system if script crashed suddenly.
* Support context recursively save, data will only be saved during last __exit__.

Usage
-----

::

    from serializabledict.storage.yamlfilestorage import YamlFileStorage
    from serializabledict import SerializableDict

    storage = YamlFileStorage("./test.yml")
    adict = SerializableDict(storage=storage)

    # Auto save
    adict.load()
    adict["item"] = 13 # Saved to test.yml automaticly.

    # Batch save, saved to test.yml after 'with' finish
    with adict:
        adict["item"] = 14
        adict["item2"] = 15
        adict["item3"] = 16

Credits
---------

This package was created with Cookiecutter_ and the `PyPackageTemplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`PyPackageTemplate`: https://github.com/starofrainnight/rtpl-pypackage

