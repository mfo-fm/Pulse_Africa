--------------------------------------------------------Data Processing Queries-------------------------------------------------------------------
--1. Calculate the number of unique visitors per day
SELECT DATE(timestamp) AS visit_date, COUNT(DISTINCT user_id) AS unique_visitors
FROM user_interactions
GROUP BY visit_date
ORDER BY visit_date;
--2. Compute the most popular articles based on user interactions
SELECT page_url, COUNT(*) AS interaction_count
FROM user_interactions
GROUP BY page_url
ORDER BY interaction_count DESC
LIMIT 10;
--3. Calculate user retention by session counts per user
SELECT user_id, COUNT(DISTINCT session_id) AS total_sessions
FROM user_interactions
GROUP BY user_id
ORDER BY total_sessions DESC;
--4. Device type distribution of users
SELECT device_type, COUNT(*) AS usage_count
FROM user_interactions
GROUP BY device_type
ORDER BY usage_count DESC;
--5. Traffic sources analysis (top referrers)
SELECT referrer, COUNT(*) AS referral_count
FROM user_interactions
WHERE referrer IS NOT NULL AND referrer <> ''
GROUP BY referrer
ORDER BY referral_count DESC
LIMIT 10;
-----------------------------------------------------------------------------------------------------------------------------------------------