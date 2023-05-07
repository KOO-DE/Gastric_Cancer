SELECT * FROM(
    SELECT
        원무접수ID,
        환자번호,
        `DOU_KEY(1)`,
        `병리진단(1)`,
        `SLIDE_BLOCK(2)`,
        `병리진단(2)`,
        `PARAFFIN_BLOCK(3)`,
        `병리진단(3)`,
        `SLIDE_PARAFFIN_BLOCK(4)`,
        `병리진단(4)`,
        `PARENTHESIS_BLOCK(5)`,
        `병리진단(5)`,
        `NONE_BLOCK_SLIDE(6)`,
        `병리진단(6)`,
        `NONE_BLOCK_PARAFFIN(7)`,
        `병리진단(7)`,
        `NONE_SLIDE_PARAFFIN_BLOCK(8)`,
        `병리진단(8)`,
        `NONE_KEY(9)`,
        `병리진단(9)`
    FROM(
        SELECT *,
            CASE 
                WHEN NULLIF(`NONE_KEY(9)`, '') IS NOT NULL
                THEN 병리진단
                ELSE NULL
            END AS `병리진단(9)`
        FROM(
            SELECT *,
                CASE 
                    WHEN (NULLIF(BLOCK_ELSE3, '') IS NOT NULL AND NULLIF(`NONE_BLOCK_SLIDE(6)`, '') IS NULL AND NULLIF(`NONE_BLOCK_PARAFFIN(7)`, '') IS NULL AND NULLIF(`NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NULL)
                    THEN BLOCK_ELSE3
                    ELSE NULL
                END AS `NONE_KEY(9)`,
                CASE 
                    WHEN NULLIF(`NONE_BLOCK_SLIDE(6)`, '') IS NOT NULL
                    THEN 병리진단
                    ELSE NULL
                END AS `병리진단(6)`,
                CASE 
                    WHEN NULLIF(`NONE_BLOCK_PARAFFIN(7)`, '') IS NOT NULL
                    THEN 병리진단
                    ELSE NULL
                END AS `병리진단(7)`,
                CASE 
                    WHEN NULLIF(`NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NOT NULL
                    THEN 병리진단
                    ELSE NULL
                END AS `병리진단(8)`
            FROM(
                # Block 
                SELECT *,
                    CASE 
                        WHEN (INSTR(BLOCK_ELSE3, 'Slide key') != 0
                            AND(REGEXP_INSTR(SUBSTR(BLOCK_ELSE3, INSTR(BLOCK_ELSE3, 'Slide key')), '[0-9]+[:|;| ]') != 0
                                OR REGEXP_INSTR(SUBSTR(BLOCK_ELSE3, INSTR(BLOCK_ELSE3, 'Slide key')), '[:|;| ][0-9]+') != 0))
                        THEN BLOCK_ELSE3
                        ELSE NULL
                    END AS `NONE_BLOCK_SLIDE(6)`,
                    CASE 
                        WHEN (INSTR(BLOCK_ELSE3, 'paraffin block key') != 0
                            AND (REGEXP_INSTR(SUBSTR(BLOCK_ELSE3, INSTR(BLOCK_ELSE3, 'paraffin block key')), '[0-9]+[:|;| ]') != 0
                                OR REGEXP_INSTR(SUBSTR(BLOCK_ELSE3, INSTR(BLOCK_ELSE3, 'paraffin block key')), '[:|;| ][0-9]+') != 0))
                        THEN BLOCK_ELSE3
                        ELSE NULL
                    END AS `NONE_BLOCK_PARAFFIN(7)`,
                    CASE 
                        WHEN (REGEXP_INSTR(BLOCK_ELSE3, 'A[0-9]+[:|;]') != 0
                            OR REGEXP_INSTR(BLOCK_ELSE3, '[:|;]A[0-9]+') != 0
                            OR REGEXP_INSTR(BLOCK_ELSE3, '[:|;] A[0-9]+') != 0)
                        THEN BLOCK_ELSE3
                        ELSE NULL
                    END AS `NONE_SLIDE_PARAFFIN_BLOCK(8)`
                FROM(
                    SELECT *,
                        CASE 
                            WHEN (NULLIF(BLOCK_ELSE2, '') IS NOT NULL AND NULLIF(`PARENTHESIS_BLOCK(5)`, '') IS NULL)
                            THEN BLOCK_ELSE2
                            ELSE NULL
                        END AS BLOCK_ELSE3,
                        CASE 
                            WHEN NULLIF(`PARENTHESIS_BLOCK(5)`, '') IS NOT NULL
                            THEN 병리진단
                            ELSE NULL
                        END AS `병리진단(5)`
                    FROM(
                        SELECT *,
                            CASE 
                                WHEN (REGEXP_INSTR(BLOCK_ELSE2, '[(]A[,|-|)]') != 0
                                    OR REGEXP_INSTR(BLOCK_ELSE2, '[(]A[0-9]+') != 0)
                                THEN BLOCK_ELSE2
                                WHEN (REGEXP_INSTR(BLOCK_ELSE2, '[(][0-9]+[,|-]') != 0
                                    OR REGEXP_INSTR(BLOCK_ELSE2, '[,|-][0-9]+[)]') != 0)
                                THEN BLOCK_ELSE2
                                ELSE NULL
                            END AS `PARENTHESIS_BLOCK(5)`
                        FROM(
                            SELECT *,
                                CASE 
                                    WHEN (NULLIF(BLOCK_ELSE1, '') IS NOT NULL AND NULLIF(`SLIDE_BLOCK(2)`, '') IS NULL AND NULLIF(`PARAFFIN_BLOCK(3)`, '') IS NULL AND NULLIF(`SLIDE_PARAFFIN_BLOCK(4)`, '') IS NULL)
                                    THEN BLOCK_ELSE1
                                    ELSE NULL
                                END AS BLOCK_ELSE2,
                                CASE 
                                    WHEN NULLIF(`SLIDE_BLOCK(2)`, '') IS NOT NULL
                                    THEN 병리진단
                                    ELSE NULL
                                END AS `병리진단(2)`,
                                CASE 
                                    WHEN NULLIF(`PARAFFIN_BLOCK(3)`, '') IS NOT NULL
                                    THEN 병리진단
                                    ELSE NULL
                                END AS `병리진단(3)`,
                                CASE 
                                    WHEN NULLIF(`SLIDE_PARAFFIN_BLOCK(4)`, '') IS NOT NULL
                                    THEN 병리진단
                                    ELSE NULL
                                END AS `병리진단(4)`
                            FROM(
                                # Block A Key가 주어져 있는 Column
                                SELECT *,
                                    CASE 
                                        WHEN REGEXP_INSTR(SUBSTR(SLIDE_BLOCK, INSTR(SLIDE_BLOCK, 'Slide key')), 'A[0-9]+') != 0
                                        THEN SLIDE_BLOCK
                                        ELSE NULL
                                    END AS `SLIDE_BLOCK(2)`,
                                    CASE 
                                        WHEN REGEXP_INSTR(SUBSTR(PARAFFIN_BLOCK, INSTR(PARAFFIN_BLOCK, 'paraffin block key')), 'A[0-9]+') != 0
                                        THEN PARAFFIN_BLOCK
                                        ELSE NULL
                                    END AS `PARAFFIN_BLOCK(3)`
                                FROM(
                                    SELECT *,
                                        CASE 
                                            WHEN (INSTR(BLOCK_ELSE1, 'Slide key') != 0 AND INSTR(BLOCK_ELSE1, 'paraffin block key') = 0)
                                            THEN BLOCK_ELSE1
                                            ELSE NULL
                                        END AS SLIDE_BLOCK,
                                        CASE 
                                            WHEN (INSTR(BLOCK_ELSE1, 'Slide key') = 0 AND INSTR(BLOCK_ELSE1, 'paraffin block key') != 0)
                                            THEN BLOCK_ELSE1
                                            ELSE NULL
                                        END AS PARAFFIN_BLOCK,
                                        CASE 
                                            WHEN (INSTR(BLOCK_ELSE1, 'Slide key') != 0 AND INSTR(BLOCK_ELSE1, 'paraffin block key') != 0)
                                            THEN BLOCK_ELSE1
                                            ELSE NULL
                                        END AS `SLIDE_PARAFFIN_BLOCK(4)`
                                    FROM(
                                        SELECT *,
                                            CASE 
                                                WHEN NULLIF(육안소견, '') IS NOT NULL AND NULLIF(`DOU_KEY(1)`, '') IS NULL
                                                THEN 육안소견
                                                ELSE NULL
                                            END AS BLOCK_ELSE1,
                                            CASE 
                                                WHEN NULLIF(`DOU_KEY(1)`, '') IS NOT NULL
                                                THEN 병리진단
                                                ELSE NULL
                                            END AS `병리진단(1)`
                                        FROM(
                                            SELECT *,
                                                # 우선 NULL 값으로 처리
                                                CASE 
                                                    WHEN ((REGEXP_INSTR(병리진단, 'A[0-9]+') = 0 AND REGEXP_INSTR(육안소견, 'A[0-9]+') != 0)
                                                        OR (REGEXP_INSTR(병리진단, 'A[0-9]+') != 0 AND REGEXP_INSTR(육안소견, 'A[0-9]+') = 0))
                                                    THEN 육안소견
                                                    ELSE NULL
                                                END AS `DOU_KEY(1)`
                                            FROM(
                                                SELECT * FROM data_type
                                            ) result
                                        ) a
                                    ) a
                                ) a
                            ) a
                        ) a
                    ) a
                ) a
            ) a
        ) a
    ) a
) a