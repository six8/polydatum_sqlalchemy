from polydatum.context import current_context
from sqlalchemy import text, orm, types
from sqlalchemy.schema import MetaData, Table, Column

metadata = MetaData()

test_table = Table('test', metadata,
    Column('id', types.Integer, primary_key = True),
    Column('name', types.String(16)),
)

def test_resource(data_manager):
    """
    Ensure that we get a new SQL alchemy session on each
    DAL context.
    """
    sessions = set([])
    with data_manager.dal():
        context1 = current_context._get_current_object()
        session = context1.sqlalchemy
        assert isinstance(session, orm.Session)
        sessions.add(session)

        with data_manager.dal():
            context2 = current_context._get_current_object()
            assert context2 != context1
            session = context2.sqlalchemy
            assert isinstance(session, orm.Session)
            sessions.add(session)

    # Make sure we have two unique sessions
    assert len(sessions) == 2

def test_execute(data_manager):
    """
    Ensure that a session is created and that we can run execute on it
    """
    with data_manager.dal():
        session = current_context.sqlalchemy
        assert isinstance(session, orm.Session)

        metadata.create_all(session.bind)
        
        session.execute(text('INSERT INTO test (name) VALUES (:name)'), {'name': 'Fred'})
        record = session.execute(text('SELECT * FROM test')).first()
        assert record.name == 'Fred'

    # Make sure Fred still exists after transaction
    with data_manager.dal():
        session = current_context.sqlalchemy
        assert isinstance(session, orm.Session)

        record = session.execute(text('SELECT * FROM test')).first()
        assert record.name == 'Fred'

def test_execute_transaction(data_manager):
    """
    Ensure that a session is rolled back on exception
    """
    class NotFred(Exception):
        pass

    try:
        with data_manager.dal():
            session = current_context.sqlalchemy
            metadata.create_all(session.bind)
            
            session.execute(text('INSERT INTO test (name) VALUES (:name)'), {'name': 'Fred'})
            record = session.execute(text('SELECT * FROM test')).first()
            assert record.name == 'Fred'

            # Now error out to remove "Fred"
            raise NotFred('Do not like Fred')
    except NotFred:
        pass

    with data_manager.dal():
        session = current_context.sqlalchemy
        record = session.execute(text('SELECT * FROM test')).first()
        # Fred should have been rolled back
        assert not record



