-- Displays the 3 cities with the highest average
SELECT `city`, AVG(`value`) AS `avgtemp` FROM `temperatures`
WHERE `month` = 7 OR `month` = 8 GROUP BY `city`
ORDER BY `avgtemp` DESC
LIMIT 3;
