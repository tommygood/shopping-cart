create table shop_cart (
`no` INT PRIMARY KEY AUTO_INCREMENT,
`uId` int(11),
`pId` int(11),
`amount` int(3),
`paid` int(1) default 0,
`delivered` int(1) default 0
)
