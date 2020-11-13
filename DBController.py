from datetime import date

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

    def list_developer_games(self,developer_id:str) -> tuple:
        """
        List all games that published by a specific developer
        :param developer_id: The developer id
        :return: a tuple contain a list of games that the developer published
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "select D.developer_id, developer_name, G.game_id, game_name, release_date, genre, platform, price \
                        from Game as G, Developer as D, Published_Games as P \
                        where G.game_id = P.game_id \
                        and D.developer_id = P.developer_id \
                        and D.developer_id = %s"
                cursor.execute(sql, developer_id)
                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result if result else ('No Results Found',)

    def list_all_published_games(self):
        """
        list all games that published by all developer
        :return: a tuple that list all developers with all games they published
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "select developer_name, game_name,release_date, genre, price,platform \
                        from Published_Games, Developer, Game \
                        where Published_Games.developer_id = Developer.developer_id \
                        and Published_Games.game_id = Game.game_id \
                        ORDER BY developer_name"
                cursor.execute(sql)
                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result if result else ('No Results Found',)

    def list_all_customer_memberships(self):
        """
        list all customers and their memberships
        :return:
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "select fname,lname,membership_type \
                        from Customer_Membership as R,Customer as C,Membership as M \
                        where R.membership_id = M.membership_id \
                        and R.customer_id = C.customer_id \
                        ORDER BY C.customer_id"
                cursor.execute(sql)
                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result if result else ('No Results Found',)

    def list_game_by_price(self,low:str,high:str) -> tuple:
        """
        List all games within a certain price range
        :param low: the lower bound of the price range
        :param high: the higher bound of the price range
        :return: a tuple contains all games within a specific price range
        """
        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "select game_name, price, release_date, genre,platform \
                        from Game, Has_Games,Store \
                        where Store.store_id = Has_Games.store_id \
                        and Game.game_id = Has_Games.game_id \
                        and price between %s and %s"
                cursor.execute(sql, low, high)
                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result if result else ('No Results Found',)

    def list_game_by_date(self,start_date:str, end_date:str) -> tuple:
        """
        List all games within a date range
        :param start_date: The start date of the date boundary
        :param end_date: The end date of the date boundary
        :return: a tuple contains a list of games within a date range
        """

        try:
            connection = pymysql.connect(self.host, self.username, self.password, self.database)
            with connection.cursor() as cursor:
                sql = "select DISTINCT game_name, release_date, genre, platform, price \
                        from Game,Store, Has_Games \
                        where Store.store_id = Has_Games.store_id \
                        and Game.game_id = Has_Games.game_id \
                        and release_date between %s and %s"
                start = date.fromisoformat(start_date)
                end = date.fromisoformat(end_date)
                cursor.execute(sql, [start_date,end_date])
                result = cursor.fetchall()

        except pymysql.err.ProgrammingError:
            print('A DB error caught')
        except ConnectionError:
            print("Unknown Connection Error")
        finally:
            connection.close()
            return result if result else ('No Results Found',)


test = SQLExecutor(host="159.203.59.83", username="gamestop", password="Sn123456", database="gamestop")
print(test.list_game_by_date("2000-01-01","2020-01-01"))