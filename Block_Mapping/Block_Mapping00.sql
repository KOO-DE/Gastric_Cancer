# Block A를 기준으로 Column을 나눔
SELECT * FROM(
    SELECT
        원무접수ID,
        환자번호,
        `FROZEN_BLOCK(0)`,
        `병리진단(0)`,
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
                # Block A Key 값에 대한 설명은 주어져 있으나 Block A Key 값은 주어져 있지 않은 경우
                CASE 
                    WHEN (NULLIF(BLOCK_ELSE4, '') IS NOT NULL AND NULLIF(`NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NULL)
                    THEN BLOCK_ELSE4
                    ELSE NULL
                END AS `NONE_KEY(9)`,
                CASE 
                    WHEN NULLIF(`NONE_SLIDE_PARAFFIN_BLOCK(8)`, '') IS NOT NULL
                    THEN 병리진단
                    ELSE NULL
                END AS `병리진단(8)`
            FROM(
                # Block 
                SELECT *,
                    # Key 값이 주어져 있지만 Slide나 Paraffin Block으로 주어져 있지 않은 경우
                    CASE 
                        WHEN (REGEXP_INSTR(BINARY BLOCK_ELSE4, 'A[0-9]+[:|;]') != 0
                            OR REGEXP_INSTR(BINARY BLOCK_ELSE4, '[:|;]A[0-9]+') != 0
                            OR REGEXP_INSTR(BINARY BLOCK_ELSE4, '[:|;] A[0-9]+') != 0)
                        THEN BLOCK_ELSE4
                        ELSE NULL
                    END AS `NONE_SLIDE_PARAFFIN_BLOCK(8)`
                FROM(
                    SELECT *,
                        CASE 
                            WHEN NULLIF(`PARENTHESIS_BLOCK(5)`, '') IS NOT NULL
                            THEN 병리진단
                            ELSE NULL
                        END AS `병리진단(5)`,
                        CASE 
                            WHEN NULLIF(`NONE_SLIDE_BLOCK(6)`, '') IS NOT NULL
                            THEN 병리진단
                            ELSE NULL
                        END AS `병리진단(6)`,
                        CASE 
                            WHEN NULLIF(`NONE_PARAFFIN_BLOCK(7)`, '') IS NOT NULL
                            THEN 병리진단
                            ELSE NULL
                        END AS `병리진단(7)`
                    FROM(
                        SELECT *,
                            # 괄호 안에 Block Key 값이 주어져 있는 경우
                            CASE 
                                WHEN NULLIF(BLOCK_ELSE3_1, '') IS NOT NULL
                                THEN BLOCK_ELSE3_1
                                /*
                                WHEN (REGEXP_INSTR(BLOCK_ELSE2_4, '[(]A[,|-|)]') != 0
                                    OR REGEXP_INSTR(BLOCK_ELSE2_4, '[(]A[0-9]+') != 0)
                                THEN BLOCK_ELSE2_4
                                WHEN (REGEXP_INSTR(BLOCK_ELSE2_4, '[(][0-9]+[,|-]') != 0
                                    OR REGEXP_INSTR(BLOCK_ELSE2_4, '[,|-][0-9]+[)]') != 0)
                                THEN BLOCK_ELSE2_4
                                */
                                ELSE NULL
                            END AS `PARENTHESIS_BLOCK(5)`,
                            # Slide Key 값이 주어져 있지만 Block A 값은 주어져 있지 않은 경우
                            CASE 
                                /*
                                WHEN (REGEXP_INSTR(BLOCK_ELSE2_1, '[S|s]lide key') != 0
                                    AND(REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_1, REGEXP_INSTR(BLOCK_ELSE2_1, '[S|s]lide key')), '[0-9]+[:|;| ]') != 0
                                        OR REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_1, REGEXP_INSTR(BLOCK_ELSE2_1, '[S|s]lide key')), '[:|;| ][0-9]+') != 0))
                                */
                                /*
                                WHEN REGEXP_INSTR(BLOCK_ELSE2_1, '[S|s]lide key') != 0
                                THEN BLOCK_ELSE2_1
                                */
                                WHEN REGEXP_INSTR(BINARY BLOCK_ELSE3_3, '[S|s]lide key') != 0
                                THEN BLOCK_ELSE3_3
                                ELSE NULL
                            END AS `NONE_SLIDE_BLOCK(6)`,
                            # Paraffin Block Key 값이 주어져 있지만 Block A 값은 주어져 있지 않은 경우
                            CASE 
                                /*
                                WHEN (REGEXP_INSTR(BLOCK_ELSE2_1, '[P|p]araffin block key') != 0
                                    AND (REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_1, INSTR(BLOCK_ELSE2_1, '[P|p]araffin block key')), '[0-9]+[:|;| ]') != 0
                                        OR REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_1, INSTR(BLOCK_ELSE2_1, '[P|p]araffin block key')), '[:|;| ][0-9]+') != 0))
                                */
                                /*
                                WHEN REGEXP_INSTR(BLOCK_ELSE2_1, '[P|p]araffin block key') != 0
                                THEN BLOCK_ELSE2_1
                                */
                                WHEN REGEXP_INSTR(BINARY BLOCK_ELSE3_3, '[P|p]araffin block key') != 0
                                THEN BLOCK_ELSE3_3
                                ELSE NULL
                            END AS `NONE_PARAFFIN_BLOCK(7)`
                        FROM(
                            SELECT *,
                                CASE 
                                    WHEN (NULLIF(BLOCK_ELSE3_2, '') IS NOT NULL AND NULLIF(BLOCK_ELSE3_3, '') IS NULL)
                                    THEN BLOCK_ELSE3_2
                                    ELSE NULL
                                END AS BLOCK_ELSE4
                            FROM(
                                SELECT *,
                                    CASE
                                        WHEN REGEXP_INSTR(BINARY BLOCK_ELSE3_2, '[S|s]lide key') != 0
                                            OR REGEXP_INSTR(BINARY BLOCK_ELSE3_2, '[P|p]araffin block key') != 0
                                        THEN BLOCK_ELSE3_2
                                        /*
                                        WHEN (REGEXP_INSTR(BLOCK_ELSE2_2, '[S|s]lide key') != 0
                                            AND REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_2, REGEXP_INSTR(BLOCK_ELSE2_2, '[S|s]lide key')), '[A-Z][0-9]+') = 0
                                            AND REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_2, REGEXP_INSTR(BLOCK_ELSE2_2, '[S|s]lide key')), 'RG[0-9]+') != 0)
                                        THEN BLOCK_ELSE2_2
                                        WHEN (REGEXP_INSTR(BLOCK_ELSE2_2, '[P|p]araffin block key') != 0
                                            AND REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_2, REGEXP_INSTR(BLOCK_ELSE2_2, '[P|p]araffin block key')), '[A-Z][0-9]+') = 0
                                            AND REGEXP_INSTR(SUBSTR(BLOCK_ELSE2_2, REGEXP_INSTR(BLOCK_ELSE2_2, '[P|p]araffin block key')), 'RG[0-9]+') != 0)
                                        THEN BLOCK_ELSE2_2
                                        */
                                        ELSE NULL
                                    END AS BLOCK_ELSE3_3
                                FROM(
                                    SELECT *,
                                        CASE 
                                            WHEN (NULLIF(BLOCK_ELSE3, '') IS NOT NULL AND NULLIF(BLOCK_ELSE3_1, '') IS NULL)
                                            THEN BLOCK_ELSE3
                                            ELSE NULL
                                        END AS BLOCK_ELSE3_2
                                    FROM(
                                        SELECT *,
                                            # BLOCK_ELSE2 Column에서 Slide Key나 Paraffin Block Key가 주어져 있는 경우
                                            CASE 
                                                /*
                                                WHEN (REGEXP_INSTR(BLOCK_ELSE2, '[S|s]lide key') != 0 
                                                    AND REGEXP_INSTR(SUBSTR(BLOCK_ELSE2, REGEXP_INSTR(BLOCK_ELSE2, '[S|s]lide key')), '[A-Z][0-9]+') = 0)
                                                THEN BLOCK_ELSE2
                                                WHEN (REGEXP_INSTR(BLOCK_ELSE2, '[P|p]araffin block key') != 0
                                                    AND REGEXP_INSTR(SUBSTR(BLOCK_ELSE2, REGEXP_INSTR(BLOCK_ELSE2, '[P|p]araffin block key')), '[A-Z][0-9]+') = 0)
                                                THEN BLOCK_ELSE2
                                                */
                                                WHEN (REGEXP_INSTR(BINARY BLOCK_ELSE3, '[(]A[)]') != 0
                                                    OR REGEXP_INSTR(BINARY BLOCK_ELSE3, '[(]A(,|-)') != 0
                                                    OR REGEXP_INSTR(BINARY BLOCK_ELSE3, '[(]A[0-9]+[)]') != 0
                                                    OR REGEXP_INSTR(BINARY BLOCK_ELSE3, '[(]A[0-9]+(,|-)') != 0)
                                                THEN BLOCK_ELSE3
                                                WHEN (REGEXP_INSTR(BLOCK_ELSE3, '[(][0-9]+[)]') != 0
                                                    OR REGEXP_INSTR(BLOCK_ELSE3, '[(][0-9]+(,|-)') != 0)
                                                THEN BLOCK_ELSE3
                                                ELSE NULL
                                            END AS BLOCK_ELSE3_1
                                        FROM(
                                            SELECT *,
                                                CASE 
                                                    WHEN (NULLIF(BLOCK_ELSE2, '') IS NOT NULL AND NULLIF(`SLIDE_BLOCK(2)`, '') IS NULL AND NULLIF(`PARAFFIN_BLOCK(3)`, '') IS NULL AND NULLIF(`SLIDE_PARAFFIN_BLOCK(4)`, '') IS NULL)
                                                    THEN BLOCK_ELSE2
                                                    ELSE NULL
                                                END AS BLOCK_ELSE3,
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
                                                # Block A가 주어져 있는 경우
                                                SELECT *,
                                                    CASE 
                                                        WHEN REGEXP_INSTR(SUBSTR(BINARY SLIDE_BLOCK, REGEXP_INSTR(BINARY SLIDE_BLOCK, '[S|s]lide key')), 'A[0-9]+') != 0
                                                        THEN SLIDE_BLOCK
                                                        ELSE NULL
                                                    END AS `SLIDE_BLOCK(2)`,
                                                    CASE 
                                                        WHEN REGEXP_INSTR(SUBSTR(BINARY PARAFFIN_BLOCK, REGEXP_INSTR(BINARY PARAFFIN_BLOCK, '[P|p]araffin block key')), 'A[0-9]+') != 0
                                                        THEN PARAFFIN_BLOCK
                                                        ELSE NULL
                                                    END AS `PARAFFIN_BLOCK(3)`
                                                FROM(
                                                    SELECT *,
                                                        # Slide Key 값이 주어져 있는 경우
                                                        CASE 
                                                            WHEN (REGEXP_INSTR(BINARY BLOCK_ELSE2, '[S|s]lide key') != 0 AND REGEXP_INSTR(BINARY BLOCK_ELSE2, '[P|p]araffin block key') = 0)
                                                            THEN BLOCK_ELSE2
                                                            ELSE NULL
                                                        END AS SLIDE_BLOCK,
                                                        # Paraffin Block Key 값이 주어져 있는 경우
                                                        CASE 
                                                            WHEN (REGEXP_INSTR(BINARY BLOCK_ELSE2, '[S|s]lide key') = 0 AND REGEXP_INSTR(BINARY BLOCK_ELSE2, '[P|p]araffin block key') != 0)
                                                            THEN BLOCK_ELSE2
                                                            ELSE NULL
                                                        END AS PARAFFIN_BLOCK,
                                                        # Slide Key와 Paraffin Block Key 값이 주어져 있는 경우
                                                        CASE 
                                                            WHEN (REGEXP_INSTR(BINARY BLOCK_ELSE2, '[S|s]lide key') != 0 AND REGEXP_INSTR(BINARY BLOCK_ELSE2, '[P|p]araffin block key') != 0)
                                                            THEN BLOCK_ELSE2
                                                            ELSE NULL
                                                        END AS `SLIDE_PARAFFIN_BLOCK(4)`
                                                    FROM(
                                                        SELECT *,
                                                            CASE 
                                                                WHEN NULLIF(BLOCK_ELSE1, '') IS NOT NULL AND NULLIF(`DOU_KEY(1)`, '') IS NULL
                                                                THEN BLOCK_ELSE1
                                                                ELSE NULL
                                                            END AS BLOCK_ELSE2,
                                                            CASE 
                                                                WHEN NULLIF(`DOU_KEY(1)`, '') IS NOT NULL
                                                                THEN 병리진단
                                                                ELSE NULL
                                                            END AS `병리진단(1)`
                                                        FROM(
                                                            SELECT *,
                                                                # 육안소견과 병리진단의 Block Key가 다르게 주어진 경우
                                                                # 우선 NULL 값으로 처리
                                                                CASE 
                                                                    WHEN ((REGEXP_INSTR(BINARY 병리진단, 'A[0-9]+') = 0 AND REGEXP_INSTR(BINARY BLOCK_ELSE1, 'A[0-9]+') != 0)
                                                                        OR (REGEXP_INSTR(BINARY 병리진단, 'A[0-9]+') != 0 AND REGEXP_INSTR(BINARY BLOCK_ELSE1, 'A[0-9]+') = 0))
                                                                    THEN BLOCK_ELSE1
                                                                    ELSE NULL
                                                                END AS `DOU_KEY(1)`
                                                            FROM(
                                                                SELECT *,
                                                                    CASE 
                                                                        WHEN (NULLIF(육안소견, '') IS NOT NULL AND NULLIF(`FROZEN_BLOCK(0)`, '') IS NULL)
                                                                        THEN 육안소견
                                                                        ELSE NULL
                                                                    END AS BLOCK_ELSE1,
                                                                    CASE 
                                                                        WHEN NULLIF(`FROZEN_BLOCK(0)`, '') IS NOT NULL
                                                                        THEN 병리진단
                                                                        ELSE NULL
                                                                    END AS `병리진단(0)`
                                                                FROM(
                                                                    SELECT *,
                                                                        CASE 
                                                                            WHEN (REGEXP_INSTR(BINARY 육안소견, '[F|f]rozen [G|g]ross [E|e]xamination') != 0
                                                                                OR REGEXP_INSTR(BINARY 육안소견, '[F|f]rozen [D|d]iagnosis') != 0)
                                                                            THEN 육안소견
                                                                            ELSE NULL
                                                                        END AS `FROZEN_BLOCK(0)`
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
                    ) a
                ) a
            ) a
        ) a
    ) a
) a