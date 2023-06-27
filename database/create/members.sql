CREATE TABLE members(
    customer_id varchar(1),
    join_date timestamp, 
    primary key (customer_id)
)
CREATE TABLE menu(
    product_id integer,
    product_name varchar(5),
    price integer,
    primary key(product_id)
)
CREATE TABLE sales(
   customer_id varchar(1),
   order_date date,
   product_id integer,
   foreign key(customer_id) references members (customer_id),
   foreign key(product_id) references menu(product_id)
)





