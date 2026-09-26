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




---------------------------------------------------------------------------------------

create database FoodDeliveryDB;
use FoodDeliveryDB;

create table FoodOrders (
      Order_ID INT primary key auto_increment,
      Customer_Name VARCHAR(50) NOT NULL,
      Food_Name VARCHAR(50) NOT NULL ,
      Category varchar(50) ,
      Quantity INT , 
      Price DECIMAL(10,2) ,
      Delivery_Status varchar(20) 
);

alter table FoodOrders add customer_city varchar(50) not null;
desc FoodOrders;
 
INSERT INTO FoodOrders (Customer_Name, Food_Name, Category, Quantity, Price, Delivery_Status, customer_city)
VALUES
    ('Aarav Sharma', 'Paneer Butter Masala', 'Main Course', 2, 280.00, 'Delivered', 'Delhi'),
    ('Priya Patel', 'Masala Dosa', 'Breakfast', 3, 120.00, 'Delivered', 'Ahmedabad'),
    ('Rohan Iyer', 'Hyderabadi Chicken Biryani', 'Main Course', 1, 350.00, 'Out for Delivery', 'Hyderabad'),
    ('Ananya Chatterjee', 'Fish Curry', 'Main Course', 1, 320.00, 'Preparing', 'Kolkata'),
    ('Vikram Malhotra', 'Chole Bhature', 'Breakfast', 2, 160.00, 'Delivered', 'Chandigarh'),
    ('Sneha Kulkarni', 'Pav Bhaji', 'Snacks', 2, 140.00, 'Delivered', 'Mumbai'),
    ('Aditya Verma', 'Gulab Jamun', 'Dessert', 4, 90.00, 'Preparing', 'Lucknow'),
    ('Kavya Nair', 'Idli Sambar', 'Breakfast', 2, 80.00, 'Delivered', 'Bengaluru'),
    ('Rahul Joshi', 'Dal Baati Churma', 'Main Course', 1, 250.00, 'Cancelled', 'Jaipur'),
    ('Meera Menon', 'Filter Coffee', 'Beverage', 2, 60.00, 'Out for Delivery', 'Chennai');

select * from FoodOrders;

-- Operators 

select * from FoodOrders where Quantity >= 2;

-- get data from FoodOrders table who have ordered meal more than 150 rupees

select * from FoodOrders where Price>=150;



-- get data from FoodOrders table who have ordered meal less than 200 rupees

select * from FoodOrders where Price<200;

-- get name , quantity , category from FoodOrders table who have ordered from Mumbai

select Customer_Name , Quantity  , Category from FoodOrders where customer_city = "Mumbai";


-- get the name , city , food name ,and category of the cutomer who did not get there order due to some conditions

select Customer_Name , Food_Name , customer_city , category , Delivery_Status from FoodOrders where Delivery_Status != "Delivered";


-- get the name of customer who is from Hyderabad and they ordered more than 350 rupees minimum

select Customer_Name , customer_city , Food_Name , Price from FoodOrders where customer_city = "Hyderabad"  and Price>=350;

-- get the name of cutomer who is from lucknow or mumbai 

select Customer_Name , customer_city , Food_Name from FoodOrders where customer_city = "Lucknow" or customer_city =  "Mumbai";

-- BETWEEN 

select * from FoodOrders where price between 100 and 300;

-- IN 

-- get the list of cutomer who ordered from Jaipur , Chandigarh , Ahmedabad and Chennai

select * from FoodOrders where customer_city In ("Jaipur" , "Chandigarh" , "Ahmedabad" , "Chennai");


-- Like -> Like is used to pattern matching 
-- 'p%' starts with p , %p ends with p, %an% contains an

 select Customer_Name from FoodOrders where Customer_Name LIKE 'R%';
 select Customer_Name from FoodOrders where Customer_Name LIKE '%r, s%';
 select Customer_Name from FoodOrders where Customer_Name LIKE '%an%';
select * from FoodOrders where Food_Name Like '%Chicken%';
  
-- as is used to provide a temperary name to the column or table 
Select Customer_Name as Customer ,  Food_Name  as food   , Category as TypesOfFood , Quantity as Q, Quantity  / Price as money  from FoodOrders;  
  



