import redis
from sqlalchemy import create_engine

my_conn = create_engine("mysql+pymysql://test_user:password@localhost/name_of_mysql_database",
                       connect_args= dict(host='localhost', port=3306))

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

def redis_sub_to_mysql():
    sub = red.pubsub()
    sub.subscribe('name_of_channel')
    for message in sub.listen():
        if message is not None and isinstance(message, dict):
            the_message = message.get('data')
            print(the_message)
            id = my_conn.execute(f"INSERT INTO  name_of_mysql_database.name_of_mysql_table (name) \
                  VALUES ('{the_message}')")
            print("Row Added  = ",id.rowcount)
        
while True:
    redis_sub_to_mysql()