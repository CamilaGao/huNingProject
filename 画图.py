import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体（根据系统配置调整）
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

# 数据准备，根据您的图片中的数据替换原始数据
data = {
    '模型': [
        'Meta-Llama-3-8B', 'Qianfan-Chinese-Llama-2-7B', 'ERNIE-3.5-8K',
        'gpt-3.5-turbo-0125', 'gpt-3.5-turbo', 'gpt-4-0314',
        'gpt-4o-mini', 'Qwen'
    ],
    '生物': [0.522, 0.658, 0.866, 0.600, 0.622, 0.762, 0.746, 0.678],
    '化学': [0.4612, 0.5276, 0.6946, 0.3548, 0.4300, 0.4980, 0.5212, 0.6250],
    '数学': [0.2913, 0.2440, 0.6740, 0.4107, 0.4307, 0.4573, 0.5640, 0.6784],
    '物理': [0.4267, 0.4033, 0.6951, 0.4422, 0.4022, 0.6684, 0.6784, 0.6362]
}
df = pd.DataFrame(data).set_index('模型')

# 设置颜色范围
vmin, vmax = df.min().min(), df.max().max()

# 创建热力图
plt.figure(figsize=(12, 8))

# 生成热力图，注释数值并调整颜色
sns.heatmap(df, annot=True, cmap='bone', linewidths=0.5, fmt='.4f',
            vmin=vmin, vmax=vmax, annot_kws={"size": 15, "va": "center", "ha": "center"})

# 标记每列最大值
for col in df.columns:
    max_index = df[col].idxmax()  # 找到最大值所在的行
    row_index = df.index.get_loc(max_index)  # 行的索引位置
    col_index = df.columns.get_loc(col)  # 列的索引位置
    plt.text(col_index + 0.8, row_index + 0.5, '★', ha='center', va='center',
             color='yellow', fontsize=50)

# 设置标题和轴标签
plt.title('', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel('', fontsize=25)
# 优化布局并显示图像
plt.tight_layout(pad=0.5)
plt.show()
