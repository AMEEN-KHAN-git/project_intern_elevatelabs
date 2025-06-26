-- 1. Total Sales by Region
SELECT Region, ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 2. Profit by Customer Segment
SELECT Segment, ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Segment
ORDER BY Total_Profit DESC;

-- 3. Top 5 Products by Sales
SELECT Product_Name, ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 5;

-- 4. Monthly Sales Trend
SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS Month, ROUND(SUM(Sales), 2) AS Monthly_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

-- 5. Category-wise Profitability
SELECT Category, ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;
