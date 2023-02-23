INSERT INTO `burgers`.`restaurants` (`id`, `name`, `created_at`, `updated_at`)
VALUES (1,'Arbys',NOW(),NOW()), (2,'Burger King',NOW(),NOW()), (3,'Mc Donalds',NOW(),NOW()), (4,'Red Robbin',NOW(),NOW()), (5,'Zaxbys',NOW(),NOW());

INSERT INTO `burgers`.`burgers` (`id`, `restaurant_id`, `name`, `bun`, `meat`, `calories`, `created_at`, `updated_at`)
VALUES (1, 3, 'Mc Aloo Tikki', 'Regular Bun', 'Potato', 180, NOW(), NOW()),
(2, 3, 'Mc Chicken', 'Regular Bun', 'Chicken', 480, NOW(), NOW()),
(3, 3, 'Mc Maharaja', 'Regular Bun', 'Grounded beef', 945, NOW(), NOW()),
(4, 3, 'Mc Veggie', 'Regular Bun', 'No Meat', 140, NOW(), NOW()),
(5, 4, 'Banzai', 'Regular Bun', 'Pineapple', 260, NOW(), NOW());

SELECT * FROM restaurants;
SELECT * FROM burgers;