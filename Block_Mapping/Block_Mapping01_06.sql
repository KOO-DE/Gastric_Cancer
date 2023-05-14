SELECT
    원무접수ID,
    환자번호,
    VALUE_A,
    ELSE_NONE_SLIDE,
    `병리진단(6)`
FROM(
    SELECT *,
        CASE 
            WHEN (NULLIF(`RE_NONE_SLIDE_BLOCK(6)`, '') IS NOT NULL AND NULLIF(VALUE_A, '') IS NULL)
            THEN `RE_NONE_SLIDE_BLOCK(6)`
            ELSE NULL
        END AS ELSE_NONE_SLIDE
    FROM(
        SELECT *,
            CASE 
                WHEN NULLIF(`RE_NONE_SLIDE_BLOCK(6)`, '') IS NOT NULL
                THEN `RE_NONE_SLIDE_BLOCK(6)`
                ELSE NULL
            END AS VALUE_A
        FROM(
            SELECT *,
                CASE 
                    WHEN NULLIF(`RE_NONE_SLIDE_BLOCK(6)`, '') IS NOT NULL
                    THEN REPLACE(`RE_NONE_SLIDE_BLOCK(6)`, ':', ';')
                    ELSE NULL
                END AS `RE_NONE_SLIDE_BLOCK(6)`
            FROM block_mapping_00
        ) a
    ) a
) a