# Write your MySQL query statement below
select tweet_id from tweets
where length(concat(content)) > 15;
