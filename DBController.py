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
        finally:
            connection.close()
            return True

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
        finally:
            return result
            connection.close()

    def select_game_by_name(self, name: str = "") -> tuple:
        """
        :param name: the name of the selected name
        :return: a tuple that contains all info of the selected game
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)

            with connection.cursor() as cursor:

                sql = "SELECT * FROM Game WHERE game_name LIKE %s"
                # ('%'+name+'%',) is semantically equal to "%name%"
                game_name = "'%" + name + "%'"
                print(game_name)
                cursor.execute(sql, game_name)
                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result

    def check_store_address(self, store_id: str) -> tuple:
        """
        :param store_id: the store id
        :return: a tuple contains the store information
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Store WHERE store_id = %s"
                cursor.execute(sql, store_id)
                result = cursor.fetchone()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result

    def check_game_copies(self, game_id: str) -> tuple:
        """
        :param game_id: the game id
        :return: list num of copies of a game within a store
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "SELECT Has_Games.store_id,Store.store_name, Has_Games.game_id,Game.game_name,num_of_copies \
                        FROM Has_Games, Store, Game \
                        WHERE Store.store_id = Has_Games.store_id \
                        and Game.game_id = Has_Games.game_id \
                        and Has_Games.game_id = %s"
                cursor.execute(sql, game_id)
                result = cursor.fetchone()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()

            return result if result else ('No Results Found',)

    def check_customer_memberships(self, customer_id: str ) -> tuple:
        """
        :param customer_id: the customer id
        :return: a tuple with customer info with hes/her corresponding membership
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "select Customer.customer_id, fname, lname, membership_type \
                      from Customer, Customer_Membership,Membership \
                      where Customer.customer_id = Customer_Membership.customer_id \
                      and Membership.membership_id = Customer_Membership.membership_id \
                      and Customer.customer_id = %s"
                cursor.execute(sql, customer_id)
                result = cursor.fetchone()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()

            return result if result else ('No Results Found',)

test = SQLExecutor(host="159.203.59.83", username="gamestop", password="Sn123456", database="gamestop")
print(test.check_game_copies('4'))