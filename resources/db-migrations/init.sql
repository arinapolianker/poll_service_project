DROP TABLE IF EXISTS question;

CREATE TABLE question(
    id INT(11) NOT NULL AUTO_INCREMENT,
    title VARCHAR(300) NOT NULL DEFAULT '',
    a VARCHAR(300) NOT NULL DEFAULT '',
    b VARCHAR(300) NOT NULL DEFAULT '',
    c VARCHAR(300) NOT NULL DEFAULT '',
    d VARCHAR(300) NOT NULL DEFAULT '',
    PRIMARY KEY (id)
);

CREATE TABLE questions_users_answer(
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT(11) NOT NULL,
    user_id INT(11) NOT NULL,
    answer VARCHAR(1) NOT NULL,
    FOREIGN KEY (question_id) REFERENCES question(id)
);


INSERT INTO question (id, title, a, b, c, d)
VALUES
    (1, 'Who is the best pop artist of the 2010s?', 'Ariana Grande', 'Beyonce', 'Ed Sheeran', 'Taylor Swift'),
    (2, 'Which TV series had the best finale?', 'Breaking Bad', 'Friends', 'The Sopranos', 'Game of Thrones'),
    (3, 'Who is the most iconic superhero?', 'Spider-Man', 'Batman', 'Wonder Woman', 'Superman'),
    (4, 'Which is the best animated movie of all time?', 'The Lion King', 'Toy Story', 'Frozen', 'Finding Nemo'),
    (5, 'Which artist made the best comeback?', 'Britney Spears', 'Justin Bieber', 'Lady Gaga', 'Eminem'),
    (6, 'What is the best streaming platform?', 'Netflix', 'Disney+', 'Amazon Prime', 'Hulu'),
    (7, 'Which celebrity has the best fashion style?', 'Rihanna', 'Zendaya', 'Harry Styles', 'Kim Kardashian'),
    (8, 'Which social media platform is the most influential?', 'Instagram', 'TikTok', 'Twitter', 'Facebook'),
    (9, 'Which video game franchise is the most popular?', 'Call of Duty', 'Fortnite', 'Super Mario', 'The Legend of Zelda'),
    (10, 'Who is the best-selling author of the 21st century?', 'J.K. Rowling', 'Stephen King', 'James Patterson', 'Dan Brown');

INSERT INTO questions_users_answer (id, question_id, user_id, answer)
VALUES
    (1, 1, 1, 'A'),
    (2, 2, 1, 'C'),
    (3, 3, 1, 'B'),
    (4, 4, 1, 'D'),
    (5, 5, 1, 'A'),
    (6, 6, 2, 'B'),
    (7, 7, 2, 'A'),
    (8, 8, 2, 'C'),
    (9, 9, 2, 'D'),
    (10, 10, 2, 'B'),
    (11, 1, 3, 'D'),
    (12, 2, 3, 'A'),
    (13, 3, 3, 'C'),
    (14, 4, 3, 'B'),
    (15, 5, 3, 'A'),
    (16, 6, 4, 'D'),
    (17, 7, 4, 'C'),
    (18, 8, 4, 'A'),
    (19, 9, 4, 'B'),
    (20, 10, 4, 'C');
