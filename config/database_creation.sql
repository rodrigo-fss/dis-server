create schema dis

create user dis_rest with password 'E!bS{c5CS4Zsm#'

grant all privileges on schema dis to dis_rest

grant all privileges on table dis.users to dis_rest

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA dis to dis_rest

create table dis.users (
	id serial not null,
	name varchar(50) not null,
	password varchar(100) not null, 
	primary key(id)
)
