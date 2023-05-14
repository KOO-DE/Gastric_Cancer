SELECT
    원무접수ID,
    환자번호,
    VALUE_A1,
    VALUE_A2,
    ELSE_PARAFFIN,
    `병리진단(3)`
FROM(
    SELECT *,
        CASE 
            WHEN (NULLIF(`RE_PARAFFIN_BLOCK(3)`, '') IS NOT NULL AND NULLIF(VALUE_A1, '') IS NULL AND NULLIF(VALUE_A2, '') IS NULL)
            THEN `RE_PARAFFIN_BLOCK(3)`
            ELSE NULL
        END AS ELSE_PARAFFIN
    FROM(
        SELECT *,
            CASE 
                WHEN (REGEXP_INSTR(SUBSTR(`RE_PARAFFIN_BLOCK(3)`, INSTR(`RE_PARAFFIN_BLOCK(3)`, 'paraffin block key')), '[A-z]+[|,|.|;| ]A[0-9]+') != 0
                    OR REGEXP_INSTR(SUBSTR(`RE_PARAFFIN_BLOCK(3)`, INSTR(`RE_PARAFFIN_BLOCK(3)`, 'paraffin block key')), '[A-z]+[|,|.|;| ][|,|.|;| ]A[0-9]+') != 0)
                THEN `RE_PARAFFIN_BLOCK(3)`
                ELSE NULL
            END AS VALUE_A1,
            CASE 
                WHEN REGEXP_INSTR(SUBSTR(`RE_PARAFFIN_BLOCK(3)`, INSTR(`RE_PARAFFIN_BLOCK(3)`, 'paraffin block key')), '[A-z]+ [(]A[0-9]+[)]') != 0
                THEN `RE_PARAFFIN_BLOCK(3)`
                ELSE NULL
            END AS VALUE_A2
        FROM(
            SELECT *,
                CASE 
                    WHEN NULLIF(`PARAFFIN_BLOCK(3)`, '') IS NOT NULL
                    THEN REPLACE(`PARAFFIN_BLOCK(3)`, ':', ';')
                    ELSE NULL
                END AS `RE_PARAFFIN_BLOCK(3)`
            FROM block_mapping_00
        ) a
    ) a
) a