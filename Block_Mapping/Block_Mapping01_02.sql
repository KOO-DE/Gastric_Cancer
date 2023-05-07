SELECT
    원무접수ID,
    환자번호,
    VALUE_A1,
    VALUE_A2,
    VALUE_FROZEN,
    `병리진단(2)`
FROM(
    SELECT *
    FROM(
        SELECT *
        FROM(
            SELECT *,
                CASE 
                    WHEN (NULLIF(`ELSE_SLIDE_BLOCK(2)`, '') IS NOT NULL AND NULLIF(VALUE_A1, '') IS NULL AND NULLIF(VALUE_A2, '') IS NULL)
                    THEN `ELSE_SLIDE_BLOCK(2)`
                    ELSE NULL
                END AS ELSE_SLIDE
            FROM(
                SELECT *,
                    CASE 
                        WHEN (REGEXP_INSTR(SUBSTR(`ELSE_SLIDE_BLOCK(2)`, INSTR(`ELSE_SLIDE_BLOCK(2)`, 'Slide key')), '[A-z]+[|,|.|;| ]A[0-9]+') != 0
                            OR REGEXP_INSTR(SUBSTR(`ELSE_SLIDE_BLOCK(2)`, INSTR(`ELSE_SLIDE_BLOCK(2)`, 'Slide key')), '[A-z]+[|,|.|;| ][|,|.|;| ]A[0-9]+') != 0
                            OR REGEXP_INSTR(SUBSTR(`ELSE_SLIDE_BLOCK(2)`, INSTR(`ELSE_SLIDE_BLOCK(2)`, 'Slide key')), 'A[0-9]+[|,|.|;| ][A-z]+') != 0
                            OR REGEXP_INSTR(SUBSTR(`ELSE_SLIDE_BLOCK(2)`, INSTR(`ELSE_SLIDE_BLOCK(2)`, 'Slide key')), 'A[0-9]+[|,|.|;| ][|,|.|;| ][A-z]+') != 0)
                        THEN `ELSE_SLIDE_BLOCK(2)`
                        ELSE NULL
                    END AS VALUE_A1,
                    CASE 
                        WHEN (REGEXP_INSTR(SUBSTR(`ELSE_SLIDE_BLOCK(2)`, INSTR(`ELSE_SLIDE_BLOCK(2)`, 'Slide key')), '[,] [(]A[0-9]+[)] [A-z]+') != 0
                            OR REGEXP_INSTR(SUBSTR(`ELSE_SLIDE_BLOCK(2)`, INSTR(`ELSE_SLIDE_BLOCK(2)`, 'Slide key')), '[A-z]+ [(]A[0-9]+[)]') != 0)
                        THEN `ELSE_SLIDE_BLOCK(2)`
                        ELSE NULL
                    END AS VALUE_A2
                FROM(
                    SELECT *,
                        CASE 
                            WHEN (NULLIF(`RE_SLIDE_BLOCK(2)`, '') IS NOT NULL AND NULLIF(VALUE_FROZEN, '') IS NULL)
                            THEN `RE_SLIDE_BLOCK(2)`
                            ELSE NULL
                        END AS `ELSE_SLIDE_BLOCK(2)`
                    FROM(
                        SELECT *,
                            CASE 
                                WHEN (INSTR(`RE_SLIDE_BLOCK(2)`, 'Frozen Gross') != 0
                                    OR INSTR(`RE_SLIDE_BLOCK(2)`, 'Frozen Diagnosis') != 0)
                                THEN `RE_SLIDE_BLOCK(2)`
                                ELSE NULL
                            END AS VALUE_FROZEN
                        FROM(
                            SELECT *,
                                CASE 
                                    WHEN NULLIF(`SLIDE_BLOCK(2)`, '') IS NOT NULL
                                    THEN REPLACE(`SLIDE_BLOCK(2)`, ':', ';')
                                    ELSE NULL
                                END AS `RE_SLIDE_BLOCK(2)`
                            FROM block_mapping_00
                        ) a
                    ) a
                ) a
            ) a
        ) a
    ) a
) a