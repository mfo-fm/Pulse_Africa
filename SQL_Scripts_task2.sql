------------------------------------------PostgreSQL Schema for User Interactions--------------------------------------------------------------
CREATE TABLE user_interactions (
    interaction_id SERIAL PRIMARY KEY,--Auto-incrementing unique ID
    user_id VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    page_url TEXT NOT NULL,
    action VARCHAR(20) CHECK (action IN ('read', 'click', 'watch')),
    device_type VARCHAR(20) NOT NULL,
    referrer TEXT,
    session_id VARCHAR(50),
    INDEX idx_user_id (user_id),--Indexing for faster querying
    INDEX idx_timestamp (timestamp),--Indexing for faster querying
    INDEX idx_action (action)--Indexing for faster querying
) PARTITION BY RANGE (timestamp);
--Partitioning Monthly for Scalability
CREATE TABLE user_interactions_2025_01 PARTITION OF user_interactions
FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE user_interactions_2025_02 PARTITION OF user_interactions
FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

CREATE TABLE user_interactions_2025_03 PARTITION OF user_interactions
FOR VALUES FROM ('2025-03-01') TO ('2025-04-01');
-------------------------------------------------------------------------------------------------------------------------------------------------