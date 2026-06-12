import pandas as pd

df = pd.DataFrame({
    "성별":["남","남","여","여","남"],
    "합격":["O","X","O","O","X"]
})

print(df)

cross_tab = pd.crosstab(
    df["성별"], # 행은 성별
    df["합격"] # 열은 합격
)
print(cross_tab)
# 합격  O  X
# 성별      
# 남   1  2
# 여   2  0

data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Education': ['High School', 'College', 'College', 'High School', 'Graduate'],
    'Age': [25, 30, 22, 35, 28]
}
df = pd.DataFrame(data)
print(df)

df_cross = pd.crosstab(df["Gender"],df['Education'],margins=True,margins_name='total')
print(df_cross)