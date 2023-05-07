SELECT
    원무접수ID,
    환자번호,
    VALUE_A1,
    VALUE_A2,
    VALUE_FROZEN,
    NONE_A,
    `병리진단(5)`
FROM(
    SELECT *
    FROM(
        SELECT *,
            CASE 
                WHEN (NULLIF(`ELSE_PARENTHESIS_BLOCK(5)`, '') IS NOT NULL AND NULLIF(VALUE_A1, '') IS NULL AND NULLIF(VALUE_A2, '') IS NULL)
                THEN `ELSE_PARENTHESIS_BLOCK(5)`
                ELSE NULL
            END AS NONE_A
        FROM(
            SELECT *,
                CASE 
                    WHEN (REGEXP_INSTR(`ELSE_PARENTHESIS_BLOCK(5)`, '[(]A[)]') != 0
                        OR REGEXP_INSTR(`ELSE_PARENTHESIS_BLOCK(5)`, '[(]A[0-9]+[,|.|;| |)]') != 0)
                    THEN `ELSE_PARENTHESIS_BLOCK(5)`
                    ELSE NULL
                END AS VALUE_A1,
                CASE 
                    WHEN (REGEXP_INSTR(`ELSE_PARENTHESIS_BLOCK(5)`, '[(][0-9]+[)]') != 0
                        OR REGEXP_INSTR(`ELSE_PARENTHESIS_BLOCK(5)`, '[(][0-9]+[,|.|;| |)]') != 0)
                    THEN `ELSE_PARENTHESIS_BLOCK(5)`
                    ELSE NULL
                END AS VALUE_A2
            FROM(
                SELECT *,
                    CASE 
                        WHEN (NULLIF(`RE_PARENTHESIS_BLOCK(5)`, '') IS NOT NULL AND NULLIF(VALUE_FROZEN, '') IS NULL)
                        THEN `RE_PARENTHESIS_BLOCK(5)`
                        ELSE NULL
                    END AS `ELSE_PARENTHESIS_BLOCK(5)`
                FROM(
                    SELECT *,
                        CASE 
                            WHEN (INSTR(`RE_PARENTHESIS_BLOCK(5)`, 'Frozen Gross') != 0
                                OR INSTR(`RE_PARENTHESIS_BLOCK(5)`, 'Frozen Diagnosis') != 0)
                            THEN `RE_PARENTHESIS_BLOCK(5)`
                            ELSE NULL
                        END AS VALUE_FROZEN
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
        ) a
    ) a
) a