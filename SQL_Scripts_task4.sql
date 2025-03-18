---------------------------------------------------Performance Optimization--------------------------------------------------------------------
--1. Create Indexes to Speed Up Queries
CREATE INDEX idx_user_timestamp ON user_interactions(user_id, timestamp);
CREATE INDEX idx_page_url ON user_interactions(page_url);
CREATE INDEX idx_device_type ON user_interactions(device_type);
CREATE INDEX idx_referrer ON user_interactions(referrer);
--2. Partitioning Strategy (Already Implemented in Schema)
-- Monthly partitioning on timestamp(SQL_Scripts_task2) ensures efficient query performance
--3. Materialized View for Frequently Accessed Data
CREATE MATERIALIZED VIEW mv_top_articles AS
SELECT page_url, COUNT(*) AS interaction_count
FROM user_interactions
GROUP BY page_url
ORDER BY interaction_count DESC
LIMIT 10;

REFRESH MATERIALIZED VIEW mv_top_articles;--Refresh the materialized view periodically
--4. Caching Results for Faster Access
ALTER DATABASE your_db_name SET enable_result_cache = on;-- Enabling query caching for frequently accessed results
--5. Optimize Aggregation Queries Using Parallel Processing
SET max_parallel_workers_per_gather = 4;
-----------------------------------------------------------------------------------------------------------------------------------------------