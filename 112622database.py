import sqlite3
from sqlite3 import Error
import os
import sys
import json

database = os.path.join(os.getcwd(), "film_data.db")

try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()

curs = conn.cursor()

# 1

# select = """select title
#             from film_data
#             where title like "B%"
#             """

# result = curs.execute(select)
# print(result.fetchall())

# 2

# select = """select title, length
#             from film_data
#             where length = 185
#             order by length desc
#             """
# result = curs.execute(select)
# print(result.fetchall())

# 3
#
# select = """select *
#             from film_data
#             order by film_id asc
#             """
# result = curs.execute(select)
# with open("sql_json.json", "a") as base:
#     json.dump(result.fetchall(), base, indent=4)

# 4

# update_film = """UPDATE film_data
#                 SET rate = 4
#                 WHERE release_year > 2010
#                 """
# curs.execute(update_film)
# conn.commit()


# select = """select *
#             from film_data
#             where release_year > 2010
#             """
# result = curs.execute(select)

# for args_ in result.fetchall():
    # insert_query = f"""INSERT INTO New_film (id_film, title, description, release_year, length, rate, special_features)
    #                     VALUES {args_};
    #
    #                 """
    # curs.execute(insert_query)
    # conn.commit()
select = """select *
            from New_film
            
            """
result = curs.execute(select)
print(result.fetchall())
