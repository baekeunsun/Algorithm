WITH DeveloperSkills AS (
    SELECT 
        D.ID,
        D.EMAIL,
        D.SKILL_CODE,
        SUM(CASE WHEN SC.CATEGORY = 'Front End' THEN SC.CODE ELSE 0 END) AS FrontEndSkillSum,
        MAX(CASE WHEN SC.NAME = 'Python' THEN SC.CODE ELSE 0 END) AS PythonSkill,
        MAX(CASE WHEN SC.NAME = 'C#' THEN SC.CODE ELSE 0 END) AS CSharpSkill
    FROM DEVELOPERS D
    JOIN SKILLCODES SC ON (D.SKILL_CODE & SC.CODE) = SC.CODE
    GROUP BY D.ID, D.EMAIL, D.SKILL_CODE
),
GradedDevelopers AS (
    SELECT 
        ID,
        EMAIL,
        CASE 
            WHEN FrontEndSkillSum > 0 AND PythonSkill > 0 THEN 'A'
            WHEN CSharpSkill > 0 THEN 'B'
            WHEN FrontEndSkillSum > 0 THEN 'C'
            ELSE NULL
        END AS GRADE
    FROM DeveloperSkills
)
SELECT 
    GRADE,
    ID,
    EMAIL
FROM GradedDevelopers
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;