# Realtime Log Streaming with FastAPI and Redis

![Architecture](/imgs/architecture.png?raw=true)

## Docker Setup
You will need to run a few services in order for this to work.

1. The first is Redis. The following commands should get you up and running:

	* `docker pull redis`
	* `docker run --name my-redis -p 6379:6379 -d redis`

	If you want to see if it is setup properly, you can go into the Docker container with:

	* `docker exec -it my-redis sh`

	Then, when in the container:

	* `redis-cli`
	* `ping`

2. The second is MySQL.

	* `docker pull mysql/mysql-server:latest`
	* `docker run --name my-mysql -p 3306:3306 mysql/mysql-server:latest`

	This shows the root password in the logs. Will need to change password.

	* `ALTER USER 'root'@'localhost' IDENTIFIED BY 'glgl';`

	Can always stop the container and restart again running detached.

	* `docker run --name my-mysql -p 3306:3306 -d mysql/mysql-server:latest`
	* `docker exec -it my-mysql bash`

	Some setup would look like:

	* `create database test;`
	* `use test;`
	* `CREATE TABLE test_table (name VARCHAR(320));`

	* `CREATE USER 'test_user'@'ip_address' IDENTIFIED BY 'password';`
	* `GRANT ALL PRIVILEGES ON test.test_table TO 'test_user'@'ip_address';`

## Local Environment Setup

### Setup Virtual Environment
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

### Run the code
- `python scripts/program.py` (runs the app that generates logs)
- `python scripts/redis_pub_from_logs.py` (runs the web server that sends SSE)
- `python scripts/redis_sub_to_mysql.py` (runs the Redis sub and inserts into MySQL)
- open client/client.html in a browser to view the events
