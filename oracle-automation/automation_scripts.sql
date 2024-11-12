-- automation_scripts.sql
CREATE OR REPLACE PROCEDURE update_salesforce_data IS
BEGIN
    -- Atualização de dados entre Oracle e Salesforce
    UPDATE sales_data SET status = 'Processed' WHERE status = 'Pending';
    COMMIT;
END update_salesforce_data;
/
