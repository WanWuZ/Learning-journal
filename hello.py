import math
import matplotlib.pyplot as plt

# 1. 开启交互模式（让图表可以动态更新）
plt.ion()

# 2. 初始化画布
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)  # 设定X轴可视范围
ax.set_ylim(-2, 2)  # 设定Y轴可视范围
ax.set_title("moni")
ax.grid(True)

L1, L2 = 1.0, 1.0  # 大臂、小臂长度

# 3. 开始动画循环：让大臂角度从0度连续转到90度，再转回来
for angle_deg in list(range(0, 91, 5)) + list(range(90, -1, -5)):
    # 清空上一帧的画面（擦除黑板）
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.grid(True)
    ax.set_title("moni")
    
    # 计算当前角度下的坐标
    t1 = math.radians(angle_deg)
    t2 = math.radians(45)  # 小臂固定弯曲45度
    
    x1 = L1 * math.cos(t1)
    y1 = L1 * math.sin(t1)
    x2 = x1 + L2 * math.cos(t1 + t2)
    y2 = y1 + L2 * math.sin(t1 + t2)
    
    # 画出新的一帧
    ax.plot([0, x1, x2], [0, y1, y2], marker='o', color='blue', linewidth=4)
    
    # 强制刷新屏幕，并停顿0.05秒
    plt.pause(0.05)

# 4. 循环结束，关闭交互模式，保持最终画面
plt.ioff()
plt.show()