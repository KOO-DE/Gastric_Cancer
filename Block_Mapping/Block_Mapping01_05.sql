SELECT
    원무접수ID,
    환자번호,
    VALUE_A1,
    VALUE_A2,
    ELSE_PARENTHESIS,
    `병리진단(5)`
FROM(
    SELECT *,
        CASE 
            WHEN (NULLIF(`RE_PARENTHESIS_BLOCK(5)`, '') IS NOT NULL AND NULLIF(VALUE_A1, '') IS NULL AND NULLIF(VALUE_A2, '') IS NULL)
            THEN `RE_PARENTHESIS_BLOCK(5)`
            ELSE NULL
        END AS ELSE_PARENTHESIS
    FROM(
        SELECT *,
            CASE 
                WHEN (REGEXP_INSTR(`RE_PARENTHESIS_BLOCK(5)`, '[(]A[)]') != 0
                    OR REGEXP_INSTR(`RE_PARENTHESIS_BLOCK(5)`, '[(]A[0-9]+[,|.|;| |)]') != 0)
                THEN `RE_PARENTHESIS_BLOCK(5)`
                ELSE NULL
            END AS VALUE_A1,
            CASE 
                WHEN (REGEXP_INSTR(`RE_PARENTHESIS_BLOCK(5)`, '[(][0-9]+[)]') != 0
                    OR REGEXP_INSTR(`RE_PARENTHESIS_BLOCK(5)`, '[(][0-9]+[,|.|;| |)]') != 0)
                THEN `RE_PARENTHESIS_BLOCK(5)`
                ELSE NULL
            END AS VALUE_A2
        FROM(
            SELECT *,
                CASE 
                    WHEN NULLIF(`PARENTHESIS_BLOCK(5)`, '') IS NOT NULL
                    THEN REPLACE(`PARENTHESIS_BLOCK(5)`, ':', ';')
                    ELSE NULL
                END AS `RE_PARENTHESIS_BLOCK(5)`
            FROM block_mapping_00
        ) a
    ) a
) a