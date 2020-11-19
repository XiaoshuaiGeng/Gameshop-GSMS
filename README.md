# Game Stop Management System - GSMS
GSMS is built by PyQt5/QT Designer/Python/MariaDB

## Function Documentation
### DBController.py
#### Class [SQLExecutor]() - `Contain functions that run sql queries in db`
  
#### SQLExecutor
   * \__init__(host,username,password,database)
   * connection_test(self) -> bool

##### Methods for `Game` Table
   * select_game_by_id(id:str) -> tuple
   * select_game_by_name(name:str) -> tuple
   * check_game_copies(game_id:str) -> tuple
   * list_game_by_price(low,high) -> tuple
   * list_game_by_date(start_date, end_date) -> tuple
   * getTabledata() -> tuple (**_Get all data from `Game` table_**)
   * add_game(game_name,release_date,genre,platform,price,availability)
   * delete_game(game_id)
   * update_game(game_id,game_name,release_date,genre,platform,price,availability)
   
   
##### Methods for `Store` Table
   
   * check_store_address(store_id) -> tuple
   * list_store() -> tuple (**_Get all data from `Store` table_**)
   * add_store(store_name,address)
   * update_store(store_id,store_name,address)
   * delete_store(store_id)
   
   
##### Methods for `Developer` Table
   * list_developer_games(developer_id) -> tuple
   * add_developer(developer_name,address)
   * update_developer(developer_id,developer_name,address)
   * delete_developer(developer_id)
   * search_developer_by_id(developer_id) -> tuple
   * list_developer() -> tuple

##### Methods for `Customer` Table
   * list_customer_history(customer_id,start,end) -> tuple
   * add_customer(fname,lname,address)
   * delete_customer(customer_id)
   * update_customer(customer_id,fname,lname,address)
   * list_customer() -> tuple (**_Get all data from `Customer` table_**)
   
##### Methods for `Game` and`Store` Table

   * num_of_copies(store_id) -> tuple
   * num_of_games(store_id) -> tuple
   
##### Methods for `Customer` and `Membership` Table

   * add_customer_membership(customer_id,membership_id)
   * update_customer_membership(customer_id, membership_id)
   * check_customer_membership(customer_id) -> tuple
   * list_all_customer_memberships() -> tuple

##### Methods for `Game` and `Developer` Table
   * list_all_published_games() -> tuple
   * count_published_games_by_location(location) -> tuple