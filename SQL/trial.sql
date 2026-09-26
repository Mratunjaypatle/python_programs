show databases;
use datascience;
show tables;
desc employee;
create database instagram;
use instagram;
create table user(
    user_id INT primary key auto_increment,
    username varchar (50) not null unique,
    email varchar (100) not null unique,
    full_name varchar(100) not null,
    age int CHECK (age >=13),
    gender varchar(20) default 'Not specified'
);
desc user;

INSERT INTO user(user_id , username , email , full_name , age , gender)
values (4 , 'rashi_03' , "rashi@gmail.com" , "rashi sharma" , 23 , "Female");
 



select * from user;





create table Posts(
		post_id int primary key auto_increment,
        user_id int not null ,
        caption varchar(500),
        post_date date default (current_date()),
        
        foreign key (user_id) references user(user_id) );
show tables;

insert into Posts (user_id , caption) values 
 (1 , "Enjoying my weekend") , 
 (1 , "Trevel Memories"),
 (4 , "Beautiful day in mumbai");
 
select * from Posts;

create table Likes (
     like_id int primary key auto_increment,
     post_id int not null,
     user_id int not null,
     foreign key (post_id) references Posts(post_id),
     foreign key (user_id) references user(user_id)
);

insert into Likes (user_id , post_id) values 
(1,2);
select * from Likes;



insert into Posts (user_id , caption) values 
 (100 , "Enjoying my weekend") 
 







CREATE DATABASE DataScience;
use DataScience;
-- show tables;
CREATE TABLE student (
          stdID INT , 
		  stdName VARCHAR(50),
		  stdAge INT ,
		  stdCity VARCHAR(50)
);

INSERT into student
 (stdID , stdName , stdAge , stdCity) values
  (101 , "Adam" , 21 , "Mumbai" );

select * from student;

Insert into student values (102 , "Bob" , 23 , "Kolkata");

CREATE TABLE employee (
          empid INT primary key, 
		  empname VARCHAR(50) NOT NULL,
		  email varchar(50) unique,
		  city VARCHAR(50) ,
          Join_Date date
);
ALTER TABLE employee ADD Phone_number varchar(20);
show tables;

insert into employee (empid , empname , email , city , Join_Date , Phone_number)
values (1 , "Rahul Sharma" , "rahul@gmail.com" , "Indore" , "2026-09-24" , "4747575757");

select * from employee;
select empname  , email from employee;

select * from employee where city = "Lucknow";
select * from employee where empid = 4;
   

select * from employee;
alter table employee add salary int(100);
desc employee;

update employee set city = "Bhopal" where empid = 1;

update employee set salary = 80000 where empid = 2;








