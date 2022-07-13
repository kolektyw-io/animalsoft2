# Database configuration

[Back to documentation home](../00_intro.md)

## Synopsis
As the application is designed to be cloud ready we do not store
any information in the app itself. The app is designed to be stateless.
Application is configured via environment variables. These environment variables may be used in Docker Compose or Nomad.

## Available configuration options

- `DB_TYPE` - allows selection of database type. Currently supported configurations are PostgreSQL - value shall be `postgres`. or MySQL/MariaDB: `mariadb`. 
  
  Example:
  `export DB_TYPE=postgres`
- `DB_HOST` - FQDN or IP of the database host address.
  
  Examples:
  - `export DB_HOST=psql1.cloud.kolektyw.io`
  - `export DB_HOST=192.168.1.2`

- `DB_PASSWORD` - Accepts password (cleartext). It is advised that this password could be set i.e. from Hashicorp Vault
  
  Example:
  `export DB_PASSWORD=postpass`

- `DB_USER` - Accepts username (cleartext). It is advised that this user could be set i.e. from Hashicorp Vault
  
  Example:
  `export DB_USER=postgres`

- `DB_NAME` - (string) - Databse name as set on host.
  
  Example:
  `export DB_NAME=animalsoft`