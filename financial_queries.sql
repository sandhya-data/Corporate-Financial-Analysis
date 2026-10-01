
-- Total Revenue and Net Profit Analysi
SELECT
Year ,
Total_Revenue ,
Net_Profit ,
(Net_Profit / Total_Revenue) * 100 AS Profit_Margin_percentage
FROM Corporate_Finance_Data
ORDER BY Year DESC;
