CREATE DATABASE finvizd_db;
use finvizd_db;

CREATE TABLE accounts (
  username VARCHAR(20),
  realname VARCHAR(40),
  password VARCHAR(20)
);

INSERT INTO accounts(username, realname, password)
VALUES
  ('julmutea', 'Julmutea', 'julmutea'),
  ('lemontea', 'Lemontea', 'lemontea');
