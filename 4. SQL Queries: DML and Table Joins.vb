<!-- SQL queries and their results -->
<!-- Entity Relationship Diagram is attached in the README.md file --> 
<!-- The data model contains 5 tables (Supplier, Customer, Product, Order item, Order) -->


<!-- DML commands-->

# List all Supplier in the France, Germany, and USA, and ordered by Country, then by ID

SELECT Id, CompanyName, ContactName, City, Country
FROM Supplier
WHERE Country IN ('France', 'Germany', 'USA')
ORDER BY Country ASC, ID ASC ; 

| ID | COMPANYNAME                            | CONTACTNAME      | CITY         | COUNTRY |
|----|----------------------------------------|------------------|--------------|---------|
| 18 | ARJUN                                  | Guylène Nodier   | Paris        | France  |
| 27 | Escargots Nouveaux                     | Marie Delamare   | Montceau     | France  |
| 28 | Gai pâturage                           | Eliane Noz       | Annecy       | France  |
| 11 | Heli Süßwaren GmbH & Co. KG            | Petra Winkler    | Berlin       | Germany |
| 12 | Plutzer Lebensmittelgroßmärkte AG      | Martin Bein      | Frankfurt    | Germany |
| 13 | Nord-Ost-Fisch Handelsgesellschaft mbH | Sven Petersen    | Cuxhaven     | Germany |
| 1  | eli lilly                              | Charlotte Cooper | indianapolis | USA     |
| 2  | New Orleans Cajun Delights             | Shelley Burke    | New Orleans  | USA     |
| 3  | Grandma Kelly's Homestead              | chandrasekar     | Oslo         | USA     |
| 8  | eli lilly                              | Peter Wilson     | Oslo         | USA     |
| 16 | Bigfoot Breweries                      | Cheryl Saylor    | Bend         | USA     |
| 19 | New England Seafood Cannery            | Robb Merchant    | Boston       | USA     |
| 30 | eli lilly                              | Ian Smith        | indianapolis | USA     |
| 31 | eli lilly                              | Ian Smith        | indianapolis | USA     |



# For Supplier Tokyo Traders change the city from Oslo to Tokyo.

(1) Check the current city of the Company: Tokyo Traders 

Select ID, CompanyName, City, Country
From Supplier 
Where CompanyName= 'Tokyo Traders';


| ID | COMPANYNAME   | CONTACTNAME  | CITY | COUNTRY |
|----|---------------|--------------|------|---------|
| 4  | Tokyo Traders | Yoshi Nagase | Oslo | Japan   |

(2) Update /Edit the city of the company from Oslo to Tokyo 

UPDATE Supplier
SET City = 'Tokyo'
WHERE CompanyName = 'Tokyo Traders' ;

| ID | COMPANYNAME   | CONTACTNAME  |  CITY   | COUNTRY |
|----|---------------|--------------|---------|---------|
| 4  | Tokyo Traders | Yoshi Nagase |  Toykyo  | Japan   |
    
    
# Discontinue the product with Id = 16.

UPDATE product
SET IsDiscontinued = 1 
WHERE ID = 16 ;

| ID | PRODUCTNAME | SUPPLIERID | UNITPRICE | PACKAGE          | ISDISCONTINUED |
|----|-------------|------------|-----------|------------------|----------------|
| 16 | Pavlova     | 7          | NULL      | 32 - 500 g boxes | 1              |


# Add new customer Jane Doe to the database. 

INSERT INTO Customer (FirstName, LastName, City, Country, Phone)
VALUES ('Jane', 'Doe', 'Nevada', 'USA', '1-725-111-1111') ;

| ID | FIRSTNAME | LASTNAME | CITY      | COUNTRY |    PHONE          | EXPR |
|----|-----------|----------|-----------|---------|--------------   --|------|
| 92 |   Jane    |   Doe    |  Nevada   |   USA   | 1 (725) 111-1111  |  0   |


# Remove products, unit price is over $50.

Delete Product
WHERE unitprice > 60 ;

       Message: 1 row(s) is affected ( 1 row is deleted)


# List all Products over than or equal to $500.

SELECT *
FROM Product
WHERE UnitPrice >= 500 ;

| ID | PRODUCTNAME                  | SUPPLIERID | UNITPRICE | PACKAGE             | ISDISCONTINUED |
|----|------------------------------|------------|-----------|---------------------|----------------|
| 1  | chai_new2                    | 1          | 561.01    | 10 boxes x 20 bags  | 0              |
| 2  | Chang                        | 1          | 561.01    | 24 - 12 oz bottles  | 0              |
| 3  | Aniseed Syrup                | 1          | 561.01    | 12 - 550 ml bottles | 0              |
| 4  | Chef Anton's Cajun Seasoning | 2          | 561.01    | 48 - 6 oz jars      | 0              |
| 6  | Grandma's Boysenberry Spread | 3          | 561.01    | 12 - 8 oz jars      | 0              |


# Get the total number of quality of Order Items 

SELECT SUM(Quantity) AS 'Total Quantity of Order_Items'
FROM Orderitem ;

| TOTAL QUANTITY OF ORDER_ITEMS  |
|--------------------------------|
| 50828                          |


# Get the total number of Suppliers 

SELECT COUNT(Id) AS 'Supplier Count'
FROM Supplier ;

| SUPPLIER COUNT |
|----------------|
| 31             |

# List all unique customer countries in alphabetical order.

SELECT DISTINCT Country
FROM Customer
ORDER BY Country;

| COUNTRY |
|---------|
| africa  |
| england |
| germany |
| india   |
| US      |
| usa     |


# Find the number of unique supplier countries.

SELECT COUNT (DISTINCT Country) AS Number
FROM Customer ;

| NUMBER |
|--------|
| 6      |

# Calculate the total sales in 2013.

SELECT AVG(TotalAmount) AS 'Average Sales 2013'
FROM [Order]
WHERE YEAR(OrderDate) = 2013

| Average Sales 2013 |
|--------------------|
| 1620.356740        |                                                            
                    
                                                            

<!-- Table Joins-->

# List all Product Name with Company Name and Unit Price 

SELECT SupplierID, ProductName, CompanyName, UnitPrice 
FROM Product P
Inner JOIN Supplier S ON P.SupplierID = S.Id ;


| SUPPLIERID | PRODUCTNAME                     | COMPANYNAME                        | UNITPRICE |
|------------|---------------------------------|------------------------------------|-----------|
| 1          | chai_new2                       | eli lilly                          | 561.01    |
| 1          | Chang                           | eli lilly                          | 561.01    |
| 1          | Aniseed Syrup                   | eli lilly                          | 561.01    |
| 2          | Chef Anton's Cajun Seasoning    | New Orleans Cajun Delights         | 561.01    |
| 3          | Grandma's Boysenberry Spread    | Grandma Kelly's Homestead          | 561.01    |
| 3          | Uncle Bob's Organic Dried Pears | Grandma Kelly's Homestead          | 0.00      |
| 3          | Northwoods Cranberry Sauce      | Grandma Kelly's Homestead          | 0.00      |
| 4          | Ikura                           | Tokyo Traders                      | 0.00      |
| 5          | Queso Cabrales                  | Cooperativa de Quesos 'Las Cabras' | 0.00      |
| 5          | Queso Manchego La Pastora       | Cooperativa de Quesos 'Las Cabras' | 0.00      |
| 6          | Konbu                           | Mayumi's                           | 0.00      |
| 6          | Tofu                            | Mayumi's                           | 0.00      |
| 6          | Genen Shouyu                    | Mayumi's                           | 0.00      |
| 7          | Pavlova                         | Pavlova, Ltd.                      | 0.00      |
| 7          | Alice Mutton                    | Pavlova, Ltd.                      | 0.00      |
| 7          | Carnarvon Tigers                | Pavlova, Ltd.                      | 0.00      |
| 8          | Teatime Chocolate Biscuits      | eli lilly                          | 0.00      |
| 8          | Sir Rodney's Marmalade          | eli lilly                          | 0.00      |
| 8          | Sir Rodney's Scones             | eli lilly                          | 0.00      |
| 9          | Gustaf's Knäckebröd             | Pakkoda Boys                       | 0.00      |
| 9          | Tunnbröd                        | Pakkoda Boys                       | 0.00      |
| 10         | Guaraná Fantástica              | Refrescos Americanas LTDA          | 0.00      |
| 11         | NuNuCa Nuß-Nougat-Creme         | Heli Süßwaren GmbH & Co. KG        | 0.00      |
| 11         | Gumbär Gummibärchen             | Heli Süßwaren GmbH & Co. KG        | 0.00      |

 ...


# Match all Customers with Order Date 

SELECT FirstName, LastName, Country, OrderDate 
FROM Customer C 
LEFT JOIN [Order] O ON O.CustomerId = C.Id ;

| FIRSTNAME | LASTNAME | COUNTRY | ORDERDATE             |
|-----------|----------|---------|-----------------------|
| Henriot   | Henriot  | india   | 7/4/2012 12:00:00 AM  |
| Josephs   | Josephs  | india   | 7/5/2012 12:00:00 AM  |
| Pontes    | Pontes   | india   | 7/8/2012 12:00:00 AM  |
| Saveley   | Saveley  | india   | 7/8/2012 12:00:00 AM  |
| Cartrain  | Cartrain | india   | 7/9/2012 12:00:00 AM  |
| Pontes    | Pontes   | india   | 7/10/2012 12:00:00 AM |
| Wang      | Wang     | india   | 7/11/2012 12:00:00 AM |
| Holz      | Holz     | india   | 7/12/2012 12:00:00 AM |

....

| Petersen  | Petersen | india   | 5/6/2014 12:00:00 AM  |
| Holz      | Holz     | india   | 5/6/2014 12:00:00 AM  |
| Lebihan   | Lebihan  | india   | 5/6/2014 12:00:00 AM  |
| Wilson    | Wilson   | india   | 5/6/2014 12:00:00 AM  |
| Roel      | Roel     | india   | NULL                  |
| Bertrand  | Bertrand | india   | NULL                  |


# Match all customers and suppliers by City 

SELECT C.FirstName, C.LastName, C.City AS CustomerCity, 
       S.City AS SupplierCity, S.CompanyName
FROM Customer C 
FULL JOIN Supplier S ON C.City = S.City
ORDER BY C.City, S.City ;

| FIRSTNAME | LASTNAME | CUSTOMERCITY | SUPPLIERCITY | COMPANYNAME                            |
|-----------|----------|--------------|--------------|----------------------------------------|
| NULL      | NULL     | NULL         | Annecy       | Gai pâturage                           |
| NULL      | NULL     | NULL         | Bend         | Bigfoot Breweries                      |
| NULL      | NULL     | NULL         | Berlin       | Heli Süßwaren GmbH & Co. KG            |
| NULL      | NULL     | NULL         | Boston       | New England Seafood Cannery            |
| NULL      | NULL     | NULL         | Cuxhaven     | Nord-Ost-Fisch Handelsgesellschaft mbH |
| NULL      | NULL     | NULL         | Frankfurt    | Plutzer Lebensmittelgroßmärkte AG      |
| NULL      | NULL     | NULL         | Göteborg     | Pakkoda Boys                           |
| NULL      | NULL     | NULL         | indianapolis | eli lilly                              |
| NULL      | NULL     | NULL         | indianapolis | eli lilly                              |
| NULL      | NULL     | NULL         | indianapolis | eli lilly                              |

...

| Fonseca   | Fonseca   | palakol     | NULL          | NULL                                  |
| Snyder    | Snyder    | palakol     | NULL          | NULL                                  |
| Pereira   | Pereira   | palakol     | NULL          | NULL                                  |
| Pontes    | Pontes    | palakol     | NULL          | NULL                                  |
| Hernández | Hernández | palakol     | NULL          | NULL                                  |
| Latimer   | Latimer   | palakol     | NULL          | NULL                                  |
| McKenna   | McKenna   | palakol     | NULL          | NULL                                  |
