

### 1. Создание базы данных "Друзья человека"

```
CREATE DATABASE `Друзья человека`;
USE `Друзья человека`;
```

### 2. Создание таблиц

Предположим, у нас есть иерархия: "Животные" как основная таблица и "Лошади", "Ослики", "Верблюды" как подтаблицы.

```
CREATE TABLE Животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(50),
    дата_рождения DATE,
    тип VARCHAR(50)
);

CREATE TABLE Лошади (
    id INT,
    команда VARCHAR(50),
    FOREIGN KEY (id) REFERENCES Животные(id)
);

CREATE TABLE Ослики (
    id INT,
    команда VARCHAR(50),
    FOREIGN KEY (id) REFERENCES Животные(id)
);

CREATE TABLE Верблюды (
    id INT,
    команда VARCHAR(50),
    FOREIGN KEY (id) REFERENCES Животные(id)
);
```

### 3. Заполнение низкоуровневых таблиц

Допустим, мы хотим добавить информацию о некоторых животных и их командах:

```
INSERT INTO Животные (имя, дата_рождения, тип) VALUES 
('Конь', '2020-05-15', 'Лошадь'),
('Ослик', '2019-07-22', 'Ослик'),
('Верблюд', '2018-11-30', 'Верблюд');

INSERT INTO Лошади (id, команда) VALUES 
(1, 'Галоп');

INSERT INTO Ослики (id, команда) VALUES 
(2, 'Гречка');

INSERT INTO Верблюды (id, команда) VALUES 
(3, 'Пустынный переход');
```

### 4. Удаление верблюдов и объединение лошадей и ослов в одну таблицу

```
DELETE FROM Верблюды WHERE id = 3;

CREATE TABLE Лошади_Ослики AS
SELECT id, имя, дата_рождения, команда
FROM Животные
JOIN Лошади ON Животные.id = Лошади.id
UNION ALL
SELECT id, имя, дата_рождения, команда
FROM Животные
JOIN Ослики ON Животные.id = Ослики.id;
```

### 5. Создание таблицы "молодые животные"

```
CREATE TABLE Молодые_животные AS
SELECT id, имя, дата_рождения, 
    TIMESTAMPDIFF(MONTH, дата_рождения, CURDATE()) AS возраст_в_месяцах
FROM Животные
WHERE DATE_ADD(дата_рождения, INTERVAL 1 YEAR) > CURDATE() AND 
      DATE_ADD(дата_рождения, INTERVAL 3 YEAR) <= CURDATE();
```

### 6. Объединение всех таблиц в одну

```
CREATE TABLE Все_животные AS
SELECT id, имя, дата_рождения, тип, 'т.к. Лошади' AS старое_имя
FROM Лошади_Ослики
UNION ALL
SELECT id, имя, дата_рождения, тип, 'Верблюды' AS старое_имя
FROM Верблюды
UNION ALL
SELECT id, имя, дата_рождения, тип, 'Молодые животные' AS старое_имя
FROM Молодые_животные;
```
