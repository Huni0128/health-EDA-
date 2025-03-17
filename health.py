import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family="NanumGothic")

health_data = pd.read_excel("./data/health_data.xlsx")

health_data = health_data.drop(columns="시점") # 시점 칼럼 삭제
health_data = health_data[health_data["대분류"]=="성별"]
health_data = health_data.rename(columns={"합계": "운동을 할 충분한 시간이 없어서"})
health_data = health_data.set_index("분류")

plt.figure(figsize=(10,8))
health_data["운동을 할 충분한 시간이 없어서"].plot.pie(explode=(0,0.02))
plt.savefig("man_women.png")
print(health_data)
