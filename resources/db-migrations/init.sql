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


INSERT INTO question (id, title, first_answer, second_answer, third_answer, fourth_answer)
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