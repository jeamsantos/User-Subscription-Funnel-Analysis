-- Total users
SELECT COUNT(*) AS total_users FROM users;

-- Total subscribers
SELECT COUNT(*) AS subscribers
FROM users
WHERE subscribed = 1;

-- Conversion rate
SELECT 
    COUNT(CASE WHEN subscribed = 1 THEN 1 END) * 1.0 / COUNT(*) AS conversion_rate
FROM users;

-- Churn rate
SELECT 
    COUNT(CASE WHEN canceled = 1 THEN 1 END) * 1.0 /
    COUNT(CASE WHEN subscribed = 1 THEN 1 END) AS churn_rate
FROM users;

-- Revenue metrics
SELECT 
    SUM(revenue) AS total_revenue,
    AVG(revenue) AS avg_revenue_per_user
FROM users;

-- Plan distribution
SELECT plan, COUNT(*) AS total_users
FROM users
GROUP BY plan;

-- Conversion by plan
SELECT 
    plan,
    COUNT(CASE WHEN subscribed = 1 THEN 1 END) * 1.0 / COUNT(*) AS conversion_rate
FROM users
GROUP BY plan;
