import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体（适用于 Windows 系统，如使用 Mac/Linux 可修改字体名称）
rcParams['font.sans-serif'] = ['SimHei']   # 黑体（支持中文）
rcParams['axes.unicode_minus'] = False     # 正常显示负号
# 设置画布
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_aspect('equal')
ax.axis('off')  # 不显示坐标轴

# 弧线参数
radii = np.linspace(1, 9, 9)  # 半径从1到6，共6条弧线
theta = np.linspace(0, np.pi, 300)  # 0到π之间画半圆

# 绘制同心半圆
for r in radii:
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color='gray')

# 年龄标尺
age_labels = np.arange(5, 85, 5)
for age in age_labels:
    angle = np.pi * (age - 5) / (80 - 5)
    r = 7.7
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    ax.text(x, y, str(age), ha='center', va='center', fontsize=8)

# 阶段标签（外环）
stage_labels = ['成长阶段', '探索阶段', '建立阶段', '维持阶段', '退出阶段']
stage_angles = [np.pi * i / 5 for i in range(len(stage_labels))]
stage_r = 8.5
for label, angle in zip(stage_labels, stage_angles):
    x = stage_r * np.cos(angle + np.pi / 10)
    y = stage_r * np.sin(angle + np.pi / 10)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold')

# 角色标签（内层）
roles = ['子女', '学生', '休闲者', '公民', '工作者', '持家者']
for i, role in enumerate(roles):
    ax.text(0, radii[i] + 0.5, role, ha='center', va='center', fontsize=10)

# 底部说明
ax.text(-7, -0.8, '生命阶段与年龄', fontsize=10)
ax.text(7, -0.8, '年龄与生命阶段', fontsize=10, ha='right')

plt.title('人生阶段图（半圆样式）', fontsize=14)
plt.tight_layout()
plt.show()


"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 设置画布
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_aspect('equal')
ax.axis('off')

# 弧线参数
radii = np.linspace(1, 9, 9)  # 9层弧线
theta = np.linspace(0, np.pi, 300)

# 定义每层颜色（从内到外）
layer_colors = [
    '#FFDDC1', '#FFCCE5', '#D4F1F9',
    '#CEF9E2', '#FFF8C1', '#FFD8B1',
    '#E6E6FA', '#C1F7D0', '#FFECF1'
]

# 先绘制填充色（从外向内）
for i in range(len(radii) - 1, 0, -1):
    r_inner = radii[i - 1]
    r_outer = radii[i]
    x_inner = r_inner * np.cos(theta)
    y_inner = r_inner * np.sin(theta)
    x_outer = r_outer * np.cos(theta)
    y_outer = r_outer * np.sin(theta)

    ax.fill_betweenx(y_outer, x_inner, x_outer,
                     color=layer_colors[i], alpha=0.5)

# 再绘制弧线（确保在填充色之上）
for r in radii:
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, color='gray', linewidth=1)

# 年龄标尺
age_labels = np.arange(5, 85, 5)
for age in age_labels:
    angle = np.pi * (age - 5) / (80 - 5)
    r = 7.7
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    ax.text(x, y, str(age), ha='center', va='center', fontsize=8)

# 阶段标签
stage_labels = ['成长阶段', '探索阶段', '建立阶段', '维持阶段', '退出阶段']
stage_angles = [np.pi * i / 5 for i in range(len(stage_labels))]
stage_r = 8.5
for label, angle in zip(stage_labels, stage_angles):
    x = stage_r * np.cos(angle + np.pi / 10)
    y = stage_r * np.sin(angle + np.pi / 10)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold')

# 角色标签（添加白色背景提高可读性）
roles = ['子女', '学生', '休闲者', '公民', '工作者', '持家者']
for i, role in enumerate(roles):
    ax.text(0, radii[i] + 0.5, role, ha='center', va='center',
            fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# 底部说明
ax.text(-7, -0.8, '生命阶段与年龄', fontsize=10)
ax.text(7, -0.8, '年龄与生命阶段', fontsize=10, ha='right')

plt.title('人生阶段图（彩色分层）', fontsize=14)
plt.tight_layout()
plt.show()
"""