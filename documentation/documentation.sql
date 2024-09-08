psql postgres
CREATE DATABASE weather_db;
CREATE USER weather_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE weather_db TO weather_user;
GRANT ALL PRIVILEGES ON SCHEMA public TO weather_user;
ALTER USER weather_user WITH SUPERUSER;
GRANT CREATE ON SCHEMA public TO weather_user;
