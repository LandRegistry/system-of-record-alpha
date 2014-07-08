CREATE TABLE titles (
  id SERIAL PRIMARY KEY,
  data text
);

GRANT ALL PRIVILEGES ON DATABASE sysofrec to sysofrec;
GRANT ALL PRIVILEGES ON TABLE titles to sysofrec;
GRANT USAGE, SELECT  ON SEQUENCE  titles_id_seq TO sysofrec;
