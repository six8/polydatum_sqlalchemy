import pytest

from polydatum.dal import DataManager
from polydatum_sqlalchemy.resources import SqlAlchemyResource

@pytest.fixture(scope="function")
def data_manager(request):
    data_manager = DataManager()

    data_manager.register_resources(
        sqlalchemy=SqlAlchemyResource('sqlite:///:memory:'),
    )

    return data_manager