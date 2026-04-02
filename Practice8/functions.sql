-- =========================================
-- FUNCTIONS.SQL
-- =========================================

-- 1. Search contacts by pattern (name or phone)
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM phonebook c
    WHERE c.name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- =========================================
-- 2. Get contacts with pagination
-- =========================================
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    limit_val INT,
    offset_val INT
)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM phonebook c
    ORDER BY c.id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;