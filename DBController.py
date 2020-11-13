import pymysql


class SQLExecutor:
    """
    A controller that is used to interact with MYSQL DB.
    It is used to execute sql queries and retrieve results from MYSQL DB
    """

    def __init__(self, host, username, password, database):
        """

        :param host:   hostname of db
        :param username:    username of db
        :param password:    password of db
        :param database:    database that will use

        :type host: str
        :type username: str
        :type password: str
        :type database: str
        """
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def connection_test(self) -> bool:
        """

        :return: True if connection test success, False otherwise
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)

            with connection.cursor() as cursor:
                sql = "SELECT VERSION()"
                cursor.execute(sql)

                result = cursor.fetchone()
                if result:
                    pass
                else:
                    return False

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except:
            print("Unknown Connection Error")
        finally:
            connection.close()

    def select_game_by_id(self, id: str) -> tuple:
        """
        :param id: the id of the selected name
        :return: a tuple that contains all info of the selected game
        """

        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)

            with connection.cursor() as cursor:
                sql = "SELECT * FROM Game WHERE game_id = %s"
                cursor.execute(sql, id)

                result = cursor.fetchone()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except:
            print("Unknown Connection Error")
        finally:
            return result
            connection.close()

    def select_game_by_name(self, name) -> tuple:

        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)

            with connection.cursor() as cursor:
                sql = "SELECT * FROM Game WHERE game_name LIKE '%%s%'"
                cursor.execute(sql, name)

                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except:
            print("Unknown Connection Error")
        finally:
            return result
            connection.close()
