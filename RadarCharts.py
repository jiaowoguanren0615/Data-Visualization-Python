import numpy as np
import matplotlib.pyplot as plt

# Sample Data
labels = ['SSv2 Accuracy', 'K400 Accuracy', 'iNat18 Accuracy', 'LVIS AP box', 'COCO AP box',
          'IN1k Accuracy', 'IN1k Linear', 'IN1k 5-Shot', 'IN1k Zero Shot']
mae_wsp = [75, 86, 89, 50, 58, 81, 79, 79, 75]
wsp = [54, 82, 85, 46, 67, 78, 71, 71, 75]
mae = [58, 66, 82, 62, 66, 81, 85, 79, 86]

# Compute Rotation
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Add edges for each data
mae_wsp += mae_wsp[:1]
wsp += wsp[:1]
mae += mae[:1]

# Initial Radar Chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot data
ax.fill(angles, mae_wsp, color='b', alpha=0.25, label='MAE + WSP')
ax.plot(angles, mae_wsp, color='b', linewidth=2)

ax.fill(angles, wsp, color='r', alpha=0.25, label='WSP')
ax.plot(angles, wsp, color='r', linewidth=2)

ax.fill(angles, mae, color='g', alpha=0.25, label='MAE')
ax.plot(angles, mae, color='g', linewidth=2)

# Add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=8)
ax.tick_params(axis='x', pad=20)

# Add grid labels
ax.set_rlabel_position(30)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="black", size=10)
plt.ylim(0, 100)

# Annotate specific values
for i in range(num_vars):
    ax.text(angles[i], mae_wsp[i], str(mae_wsp[i]), horizontalalignment='center', size=10, color='black')
    ax.text(angles[i], wsp[i], str(wsp[i]), horizontalalignment='center', size=10, color='black')
    ax.text(angles[i], mae[i], str(mae[i]), horizontalalignment='center', size=10, color='black')

# plt.title("Compare with each model")

# Add classes of Radar chart
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# show Radar chart
plt.show()