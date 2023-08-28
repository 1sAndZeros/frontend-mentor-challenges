DROP TABLE IF EXISTS projects CASCADE;
DROP SEQUENCE IF EXISTS projects_id_seq;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS projects_id_seq;
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description text,
    image_url VARCHAR(255)
);

INSERT INTO projects (name, description, image_url) VALUES
("Password Generator", "Generates a password with different characters, symbols etc. of a given length", "https://unsplash.com/photos/FnA5pAzqhMM")