
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    quantity INT NOT NULL
);


INSERT INTO products (name, description, price, quantity) VALUES
('MacBook Pro 16"', 'laptop', 2399.99, 20),
('Dell XPS 15', 'laptop', 1899.99, 25),
('HP Spectre x360', 'laptop', 1599.99, 30),
('Lenovo ThinkPad X1 Carbon', 'laptop', 1499.99, 15),
('Asus ROG Zephyrus G14', 'laptop', 1399.99, 20),
('Acer Predator Helios 300', 'laptop', 1199.99, 10),
('Microsoft Surface Laptop 4', 'laptop', 1299.99, 18),
('Razer Blade 15', 'laptop', 1799.99, 12),
('MSI GS66 Stealth', 'laptop', 2099.99, 14),
('LG Gram 17', 'laptop', 1599.99, 22);



SELECT * FROM products;