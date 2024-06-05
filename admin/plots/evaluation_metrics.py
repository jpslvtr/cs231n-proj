import matplotlib.pyplot as plt

# Example data for demonstration
methods = ['NeRF', 'InstantNGP', 'Plenoxels', 'Ours-One-15k', 'Ours-Two-7k']
ssim_scores = [0.85, 0.80, 0.83, 0.87, 0.86]
psnr_scores = [25.5, 24.0, 26.0, 27.0, 26.5]

x = range(len(methods))

fig, ax1 = plt.subplots()

ax1.set_xlabel('Method')
ax1.set_ylabel('SSIM', color='tab:red')
ax1.bar(x, ssim_scores, color='tab:red', alpha=0.6, label='SSIM')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.set_xticks(x)
ax1.set_xticklabels(methods)

ax2 = ax1.twinx()
ax2.set_ylabel('PSNR', color='tab:blue')
ax2.plot(x, psnr_scores, color='tab:blue', marker='o', label='PSNR')
ax2.tick_params(axis='y', labelcolor='tab:blue')

fig.tight_layout()
plt.title('Evaluation Metrics')
plt.savefig('evaluation_metrics.png')
plt.show()
