# schema of cart

create table users(
`no` INT PRIMARY KEY AUTO_INCREMENT,
`pwd` varchar(3),
`title` varchar(10)
)

create table product(
`no` INT PRIMARY KEY AUTO_INCREMENT,
`name` varchar(15),
`price` int(5),
`stock` int(5)
)

create table shop_cart (
`no` INT PRIMARY KEY AUTO_INCREMENT,
`uId` int(11),
`pId` int(11),
`amount` int(3),
`paid` int(1) default 0,
`deleted` int(1) default 0
)
