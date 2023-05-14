SELECT
    원무접수ID,
    환자번호,
    PARAFFIN_VALUE_A,
    SLIDE_VALUE_A,
    ELSE_SLIDE_PARAFFIN,
    `병리진단(4)`
FROM(
    SELECT *,
        CASE 
            WHEN (NULLIF(`RE_SLIDE_PARAFFIN_BLOCK(4)`, '') IS NOT NULL AND NULLIF(SLIDE_VALUE_A, '') IS NULL AND NULLIF(PARAFFIN_VALUE_A, '') IS NULL)
            THEN `RE_SLIDE_PARAFFIN_BLOCK(4)`
            ELSE NULL
        END AS ELSE_SLIDE_PARAFFIN
    FROM(
        SELECT *,
            CASE 
                WHEN REGEXP_INSTR(SUBSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, INSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, 'paraffin block key')), 'A[0-9]+') != 0
                THEN SUBSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, INSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, 'paraffin block key'))
                ELSE NULL
            END AS PARAFFIN_VALUE_A,
            CASE 
                WHEN REGEXP_INSTR(SUBSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, INSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, 'Slide key')), 'A[0-9]+') != 0
                THEN SUBSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, INSTR(`RE_SLIDE_PARAFFIN_BLOCK(4)`, 'Slide key'))
                ELSE NULL
            END AS SLIDE_VALUE_A
        FROM(
            SELECT *,
                CASE
                    WHEN NULLIF(`SLIDE_PARAFFIN_BLOCK(4)`, '') IS NOT NULL
                    THEN REPLACE(`SLIDE_PARAFFIN_BLOCK(4)`, ':', ';')
                    ELSE NULL
                END AS `RE_SLIDE_PARAFFIN_BLOCK(4)`
            FROM block_mapping_00
        ) a
    ) a
) a