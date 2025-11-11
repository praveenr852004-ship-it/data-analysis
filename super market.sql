use supermarketproject
select*from supermarketproject

1# who spend more male or female  from gender#
select gender,sum(total_sales)as reveune
from supermarketproject
group by gender

2# which product get more review rating
select product_line,avg(rating) as "average product rating"
from supermarketproject
group by product_line
order by avg (rating)desc

3#who spend more member or normal people
select Customer_Type,
count(Customer_Type) as total_customer,
avg (total_sales) as avg_spend
from supermarketproject
group by Customer_Type;
 
4#best selling product and total revenue
SELECT Product_line,
SUM(Quantity) AS total_quantity_sold,
SUM(Total_Sales) AS total_revenue
FROM supermarketproject
GROUP BY Product_line
ORDER BY total_revenue desc

