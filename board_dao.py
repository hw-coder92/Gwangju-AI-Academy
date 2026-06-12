import pymysql

class BoardDAO:

    def __init__(self):
        self.host = "localhost"
        self.user = "board_user"
        self.password = "board1234"
        self.database = "board_db"

    def get_connection(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
            charset = "utf8mb4" # 
        )
    
    def insert_board(self, title, content, writer):
        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO board
        (title, content, writer)
        VALUES
        (%s, %s, %s)
        """
        cursor.execute(
            sql,
            (title, content, writer)
        )

        conn.commit()
        cursor.close()
        conn.close()

        print("등록 완료")
        
    def select_all(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        sql = """
        SELECT *
        FROM board
        ORDER BY id DESC
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result
    

    def select_one(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if board_id is None:
            return "존재하지 않는 게시물입니다."

        return result

    def delete_board(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))

        conn.commit()

        cursor.close()
        conn.close()

        print("삭제 완료")


    def update_board(self, num, title, content):

        conn = self.get_connection() 
        cursor = conn.cursor()

        try:
            sql = """
                UPDATE board 
                SET title = %s, content = %s 
                WHERE id = %s
            """
            
            cursor.execute(sql, (title, content, int(num)))
            
            conn.commit()
            
        except Exception as e:
            print(f"수정 중 오류 발생: {e}")
            conn.rollback() # 오류 발생 시 원상복구
            
        finally:
            cursor.close()
            
    def insert_reply(self, board_id, content, writer):
        """댓글 등록"""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO reply (board_id, content, writer)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (int(board_id), content, writer))
                conn.commit()

    def select_replies_by_board_id(self, board_id):
        """특정 게시글의 댓글 목록 조회"""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                sql = """
                SELECT id, content, writer, reg_date
                FROM reply
                WHERE board_id = %s
                ORDER BY id ASC
                """
                cursor.execute(sql, (int(board_id),))
                return cursor.fetchall()
