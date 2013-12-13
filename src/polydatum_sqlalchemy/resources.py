from polydatum.resources import Resource
from sqlalchemy import orm, create_engine

class SqlAlchemyResource(Resource):
    def __init__(self, dburi, engine_options=None):
        super(SqlAlchemyResource, self).__init__()
        self.dburi = dburi

        engine_options = engine_options or {}
        self.engine = create_engine(self.dburi, **engine_options)

        self.session_maker = orm.sessionmaker(bind=self.engine)

    def __call__(self, context):
        session = self.session_maker()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()