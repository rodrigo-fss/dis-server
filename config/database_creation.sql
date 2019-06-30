create schema dis

create user dis_rest with password 'E!bS{c5CS4Zsm#'

grant all privileges on schema dis to dis_rest

grant all privileges on table dis.images to dis_rest

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA dis to dis_rest

create table dis.users (
	id serial not null,
	name varchar(50) not null,
	email varchar(50) not null,
	password varchar(100) not null, 
	primary key(id)
);
grant all privileges on table dis.users to dis_rest;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA dis to dis_rest;


create table dis.images (
	image_id serial not null,
	user_id int references dis.users(id) not null,
	matrix varchar(900) not null,
	image_size varchar(10) not null,
	iterations int not null,
	init_time timestamp not null,
	finish_time timestamp not null,
	primary key(image_id)
);
grant all privileges on table dis.images to dis_rest;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA dis to dis_rest;