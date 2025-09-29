
-- Зв'язок клас ↔️ учні (багато до багатьох)
CREATE TABLE class_student (
    class_id INT,
    student_id INT,
    PRIMARY KEY (class_id, student_id),
    FOREIGN KEY (class_id) REFERENCES class(id),
    FOREIGN KEY (student_id) REFERENCES student(id)
);

-- Таблиця предметів
CREATE TABLE subject (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

-- Таблиця уроків (розклад)
CREATE TABLE lesson (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lesson_number INT,           -- 1–8
    subject_id INT,
    class_id INT,
    teacher_id INT,
    FOREIGN KEY (subject_id) REFERENCES subject(id),
    FOREIGN KEY (class_id) REFERENCES class(id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(id)
);
