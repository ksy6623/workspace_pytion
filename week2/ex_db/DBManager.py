import cx_Oracle
from mylogger import make_logger
logger = make_logger("DBManager.log")

class DBManager:

    def __init__(self):
        self.conn = None

    def get_connection(self):
        try:
            if self.conn is None or self.conn.closed:
                self.conn = cx_Oracle.connect("member","member","localhost:1521/xe")
                logger.info("db 연결됨")
            return self.conn
        except Exception as e:
            logger.error(f"DB 연결 오류:{e}")
            return None
    def __del__(self):
        """객체 소멸 시 연결 종료"""
        if self.conn:
            self.conn.close()
            logger.info(f"db 연결이 정상적으로 종료되었습니다.")
    def insert(self, query, param):
        """데이터 삽입"""
        cursor = None
        try:
            if self.conn is None:
                self.get_connection()
            cursor = self.conn.cursor()
            cursor.execute(query, param)
            self.conn.commit()
            logger.debug(f"저장됨 {param}")
        except Exception as e:
            logger.error(f"저장 오류!{e}")
            if self.conn:
                self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

if __name__ == '__main__':
    db = DBManager()
    conn = db.get_connection()
    if conn:
        db.insert("INSERT INTO 학생 (학번, 이름) VALUES(:1,:2)", [1, "동수"] )





