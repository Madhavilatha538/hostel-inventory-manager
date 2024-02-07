create database inventory_manager;
use inventory_manager;
create table Guest_details(Name varchar(20),
                           Qualification varchar(30),
                           Joining_date date,
                           Room_No int,
                           Sharing_type int,
                           Work_Address varchar(70),
                           Permanent_Address varchar(70));
set sql_safe_updates = 0;
alter table Guest_details drop primary key;
alter table guest_details add guest_no int;
alter table Guest_details add Vacate_date date;
update Guest_details set guest_no = 3 where Name='Prabha';
select * from Guest_details;
Update Guest_details set Name="Siri" where Name="Madhu";
Update Guest_details set Name="Swetha" where Name="Prabha";
insert into Guest_details values ('Dilshad','M.Sc Mathematics','2023-01-01',113,5,'Sri Venkateswara University','Rajamapeta','2024-02-03');
create table Worker_details(Name varchar(20),
							 work_type varchar(20),
                             Salary int,
                             Address varchar(50));
select * from Worker_details;
Insert into Worker_details values('Madhusudhan','Cooking',23000,'Rajasthan');
Insert into Worker_details values('Malathi','Sweeping',20000,'Utthar pradesh');
Insert into Worker_details values('Nivi','Washing',18000,'Madhya pradesh'),
								 ('sunitha','Cleaning',14000,'Andhra pradesh');
                                  
create table Charges(Day date,
                     Groceries_bill int,
                     Power_bill int,
                     Maintenance_bill int,
                     Gas_bill int,
                     Salaries int);
select * from Charges;
insert into Charges values('2023-09-01',14500,19000,9000,7000,82000),
						  ('2023-10-01',13000,21000,8700,7900,82000),
                          ('2023-11-01',17600,17000,9600,9000,82000);
create table Menu(Day varchar(10),
                  Morning varchar(50),
                  Afternoon varchar(50),
                  Night varchar(50));
insert into Menu values('Sunday','Pongal and chutney','chicken and curd','Flavoured rice with raitha'),
						  ('Monday','Idli and chutney','pappu,fry and curd','roti and alu curry'),
                          ('Tuesday','Flavoured rice','pappu,fry and curd','roti and califlower curry'),
                          ('Wednesday','puri and alu curry','pappu,rasam and curd','chicken and curd'),
                          ('Thursday','Bonda with chutney','pappu,fry and curd','roti and alu curry'),
                          ('Friday','upma with chutney','pappu,fry and curd','roti and capsicum curry'),
                          ('Saturday','Dosa with chutney','pappu,fry and curd','roti and chole curry');
select * from Menu;
create table facilities(Product_name varchar(20),
                        count int);
select * from facilities;
insert into facilities values('fans',57),
							 ('lights',114),
                             ('Matrices',80),
                             ('Curtains',30),
                             ('Geyser',4),
                             ('CC cameras',10),
                             ('Washing Machine',1),
                             ('Tables',3),
                             ('Chairs',25);
create table fee(guest_id int primary key,
                 amount int,
                 payment_status varchar(10));
alter table fee modify payment_status varchar(20);
select * from fee;
set foreign_key_checks = 0;
alter table Guest_details add constraint fk_fee foreign key(guest_no)references fee(guest_id);
insert into fee values(1,5500,'paid successfully'),
					   (2,5800,'unpaid'),
                       (3,5500,'paid successfully');


