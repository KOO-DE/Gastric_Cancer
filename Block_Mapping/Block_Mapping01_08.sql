SELECT
    원무접수ID,
    환자번호,
    VALUE_A,
    VALUE_FROZEN,
    NONE_A,
    `병리진단(8)`
FROM(
    SELECT *,
        CASE 
            WHEN NULLIF(`ELSE_NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NOT NULL AND NULLIF(VALUE_A, '') IS NULL
            THEN `ELSE_NONE_SLIDE_PARAFFIN_BLOCK(8)`
            ELSE NULL
        END AS NONE_A
    FROM(
        SELECT *,
            CASE 
                WHEN NULLIF(`ELSE_NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NOT NULL
                THEN `ELSE_NONE_SLIDE_PARAFFIN_BLOCK(8)`
                ELSE NULL
            END AS VALUE_A
        FROM(
            SELECT *,
                CASE 
                    WHEN (NULLIF(`RE_NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NOT NULL AND NULLIF(VALUE_FROZEN, '') IS NULL)
                    THEN `RE_NONE_SLIDE_PARAFFIN_BLOCK(8)`
                    ELSE NULL
                END AS `ELSE_NONE_SLIDE_PARAFFIN_BLOCK(8)`
            FROM(
                SELECT *,
                    CASE 
                        WHEN (INSTR(`RE_NONE_SLIDE_PARAFFIN_BLOCK(8)`, 'Frozen Gross') != 0
                            OR INSTR(`RE_NONE_SLIDE_PARAFFIN_BLOCK(8)`, 'Frozen Diagnosis') != 0)
                        THEN `RE_NONE_SLIDE_PARAFFIN_BLOCK(8)`
                        ELSE NULL
                    END AS VALUE_FROZEN
                FROM(
                    SELECT *,
                        CASE 
                            WHEN NULLIF(`NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NOT NULL
                            THEN REPLACE(`NONE_SLIDE_PARAFFIN_BLOCK(8)`, ':', ';')
                            ELSE NULL
                        END AS `RE_NONE_SLIDE_PARAFFIN_BLOCK(8)`
                    FROM block_mapping_00
                ) a
            ) a
        ) a
    ) a
) a