-- 1. Upsert contact (insert or update)
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phonebook WHERE name = p_name
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 2. Bulk insert with validation

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    -- check arrays length
    IF array_length(names, 1) IS DISTINCT FROM array_length(phones, 1) THEN
        RAISE EXCEPTION 'Names and phones arrays must have the same length';
    END IF;

    FOR i IN 1..array_length(names, 1) LOOP

        -- validate phone (only digits)
        IF phones[i] ~ '^[0-9]+$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone for %: %', names[i], phones[i];
        END IF;

    END LOOP;
END;
$$;


-- 3. Delete contact by name or phone

CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value
       OR phone = p_value;
END;
$$;