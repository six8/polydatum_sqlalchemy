====================
Polydatum SqlAlchemy
====================

A SqlAlchemy plugin for Polydatum

Usage
-----

Example::

    from polydatum.dal import DataManager
    from polydatum_sqlalchemy.resources import SqlAlchemyResource

    data_manager = DataManager()

    data_manager.register_resources(
        sqlalchemy=SqlAlchemyResource('sqlite:///:memory:'),
    )

    with data_manager.dal():
        session = current_context.sqlalchemy

Testing
-------

To run tests you'll need to install the test requirements:

    pip install -r src/tests/requirements.txt

Run tests:

    py.test src/tests