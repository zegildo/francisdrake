
--drop table professores;
--drop table horario_professores;

CREATE TABLE professores(
	siape integer,
	nome varchar(200),
	departamento varchar(200),
	foto varchar(200),
	pagina varchar(200)
);

CREATE TABLE horario_professores(
	siape integer,
	nivel varchar(30),
	ano_periodo varchar(6),
	codigo_disciplina varchar(7),
	nome_disciplina varchar(300),
	carga_horaria varchar(4),
	horario varchar(500)
);

COPY horario_professores FROM '../horarios_ufersa.csv' DELIMITER ',' CSV HEADER
COPY professores FROM '../ufersa_teachers.csv' DELIMITER ',' CSV HEADER
