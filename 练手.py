
import random
import matplotlib.pyplot as plt


# 模拟生成温度传感器数据（范围20-30度）
time = list(range(1,21))
temperature = [random.uniform(20, 30)for _ in time]

# 创建图表
plt.plot(time, temperature, marker="o", color="blue")
plt.title("mock temperature sensor data")
plt.xlabel("time(s)")
plt.ylabel("temperture(C)")
plt.grid(True)

# 显示图表
plt.show()










