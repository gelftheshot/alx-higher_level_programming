-- Displays the max temperature of each state, ordered by state name.
SELECT `state`, MAX(`value`) AS `maxtemp` FROM `temperatures`
GROUP BY `state` ORDER BY `state`;
