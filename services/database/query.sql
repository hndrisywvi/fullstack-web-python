create table users (
    id serial primary key,
    name varchar(100) not null,
    username varchar(200) not null,
    password text not null,
    role varchar(1),
    created_at timestamp
);