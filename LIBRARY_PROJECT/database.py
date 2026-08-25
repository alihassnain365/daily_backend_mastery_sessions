from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("sqlite:///library.db")
sessionLocl = sessionmaker(bind=engine)

# applying foreign_key constraints for every opened new connection
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_recond):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


