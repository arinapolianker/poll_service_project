DROP TABLE IF EXISTS questions;

CREATE TABLE questions(
    id INT(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(300) NOT NULL DEFAULT '',
    last_name VARCHAR(300) NOT NULL DEFAULT '',
    email VARCHAR(300) NOT NULL DEFAULT '',
    age VARCHAR(300) NOT NULL DEFAULT '',
    address VARCHAR(300) NOT NULL DEFAULT '',
    joining_date DATE NOT NULL,
    registered TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);


INSERT INTO user (first_name, last_name, email, age, address, joining_date, registered)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com', 28, '123 Elm St, Springfield', '2023-01-15', 1),
    ('Bob', 'Smith', 'bob.smith@example.com', 34, '456 Maple Ave, Riverdale', '2022-11-20', 1),
    ('Catherine', 'Brown', 'catherine.brown@example.com', 26, '789 Oak Dr, Westfield', '2023-06-01', 1),
    ('David', 'Wilson', 'david.wilson@example.com', 40, '101 Pine Ln, Center ville', '2021-09-10', 0),
    ('Ella', 'Taylor', 'ella.taylor@example.com', 31, '202 Birch Blvd, Lakeview', '2022-12-25', 1),
    ('Frank', 'Moore', 'frank.moore@example.com', 45, '303 Cedar Ct, Hilton', '2020-08-15', 0);