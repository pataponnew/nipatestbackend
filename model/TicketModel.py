from ast import Param
from helper.ErrException import ErrException
from sqlalchemy import create_engine, text
import config
from datetime import datetime

class TicketModel:
    isLocalConnect = False
    autoCommit = False
    
    def __init__(self, **kwargs):
        self.sqluri = config.Config.DB_URL
    
    def create(self, columns):
        engine = create_engine(self.sqluri)
        params = {
            'title': columns['title'],
            'description': columns['description'],
            'contactInformation': columns['contactInformation'],
            'created_date':datetime.now(),
            'updated_date':datetime.now(),
            'status':'pending'
        }
        with engine.connect() as conn:
            try:
                result = conn.execute(text("""
                    INSERT INTO `Ticket` (title, description, contactInformation,created_date,updated_date,status)
                    VALUES (:title, :description, :contactInformation, :created_date, :updated_date, :status)
                """), params)
                conn.commit()
                return result
            except Exception as e:
                print(f"Error inserting record into database: {e}")
                raise
            finally:
                engine.dispose()

    
    def select(self, data):
        engine = create_engine(self.sqluri)
        params = {'status': data}
        sql = """
            SELECT *
            FROM `Ticket`
            WHERE status = :status
        """
        print(params)
        with engine.connect() as conn:
            result = conn.execute(text(sql), params)
            rows = result.fetchall()
            column_names = list(result.keys())
            dict_rows = []
            for row in rows:
                dict_row = {}
                for i in range(len(column_names)):
                    dict_row[column_names[i]] = row[i]
                dict_rows.append(dict_row)
        engine.dispose()
        return dict_rows
    
    def update(self, columns):
        engine = create_engine(self.sqluri)
        params = {
            'Id':columns['Id'],
            'status':columns['status'],
            'updated_date':datetime.now()
        }
        with engine.connect() as conn:
            try:
                result = conn.execute(text("""
                    UPDATE `Ticket`
                    SET status = :status,updated_date = :updated_date
                    WHERE Id = :Id
                """), params)
                conn.commit()
                return result
            except Exception as e:
                print(f"Error updating record into database: {e}")
                raise
            finally:
                engine.dispose()