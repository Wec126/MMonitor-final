import mindspore as ms
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Set up warning filtering
warnings.filterwarnings(action='once')

# Set the fontsize and some other elements
large = 22 
med = 16
small = 12
params = {
    'axes.titlesize': large,
    'legend.fontsize': med,
    'figure.figsize': (16, 10),
    'axes.labelsize': med,
    'axes.titlesize': med,
    'xtick.labelsize': med,
    'ytick.labelsize': med,
    'figure.titlesize': large
}

# Update matplotlib parameters
plt.rcParams.update(params)
sns.set_theme()
sns.set_style("white")

# Define color and line style cycles
color_cycle = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#FF0000', '#00FF00', '#0000FF', '#FF00FF', '#FFFF00',
    '#00FFFF', '#FF5733', '#33FF57', '#5733FF', '#FF3366',
    '#33FFC7', '#B45F04', '#96C703', '#93F5C0', '#D303D3',
    '#4C1463', '#7C4B00', '#AE7F37', '#00E2E2', '#C70039'
]

line_style_cycle = ['-', '--', '-.', ':'] * 7 + ['-', '--']

# Set the prop cycle for axes
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_cycle) + plt.cycler(linestyle=line_style_cycle)


