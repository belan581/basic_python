-- Creación de tablas
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INTEGER,
    carrera VARCHAR(50)
);

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    creditos INTEGER,
    profesor VARCHAR(50)
);

CREATE TABLE inscripciones (
    id SERIAL PRIMARY KEY,
    estudiante_id INTEGER REFERENCES estudiantes(id),
    curso_id INTEGER REFERENCES cursos(id),
    fecha_inscripcion DATE
);

-- Inserción de datos
INSERT INTO estudiantes (nombre, edad, carrera) VALUES ('Juan Perez', 20, 'Ingeniería Civil');
INSERT INTO estudiantes (nombre, edad, carrera) VALUES ('María Lopez', 22, 'Administración de Empresas');
INSERT INTO estudiantes (nombre, edad, carrera) VALUES ('Carlos Ramirez', 19, 'Medicina');

INSERT INTO cursos (nombre, creditos, profesor) VALUES ('Matemáticas I', 4, 'Dr. Smith');
INSERT INTO cursos (nombre, creditos, profesor) VALUES ('Economía', 3, 'Prof. Johnson');
INSERT INTO cursos (nombre, creditos, profesor) VALUES ('Anatomía', 5, 'Dr. Martinez');

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion) VALUES (1, 1, '2023-07-01');
INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion) VALUES (1, 2, '2023-07-05');
INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion) VALUES (2, 2, '2023-07-10');
INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion) VALUES (3, 3, '2023-07-15');

-- Consultas
-- Ejemplo de consulta con JOIN
SELECT estudiantes.nombre AS estudiante, cursos.nombre AS curso
FROM estudiantes
INNER JOIN inscripciones ON estudiantes.id = inscripciones.estudiante_id
INNER JOIN cursos ON cursos.id = inscripciones.curso_id;

-- Ejemplo de consulta con WHERE
SELECT nombre, edad, carrera
FROM estudiantes
WHERE edad >= 20;

-- Ejemplo de consulta con GROUP BY y HAVING
SELECT cursos.nombre, COUNT(inscripciones.id) AS num_inscripciones
FROM cursos
LEFT JOIN inscripciones ON cursos.id = inscripciones.curso_id
GROUP BY cursos.nombre
HAVING COUNT(inscripciones.id) >= 2;

-- Ejemplo de consulta con ORDER BY
SELECT nombre, creditos
FROM cursos
ORDER BY creditos DESC;

-- Ejemplo de consulta con LIMIT
SELECT nombre, edad
FROM estudiantes
LIMIT 2;
