from pylab import *

results = {
    "English": [[54.8, 71.1, 75.7, 81.6], [24.5, 24.9, 30.8, 37.8]],
    "Chinese": [[61.7, 73.6, 79.3, 83.4], [23.3, 28.2, 29.4, 36.0]],
    "French": [[57.0, 68.9, 77.3, 83.3], [24.0, 25.2, 28.4, 35.0]],
    "Spanish": [[62.3, 71.7, 78.7, 83.0], [23.5, 24.4, 28.7, 34.6]],
    "Portuguese": [[60.3, 70.4, 75.6, 84.2], [24.3, 23.8, 28.8, 36.0]],
    "Arabic": [[57.3, 72.1, 78.8, 85.4], [24.6, 24.3, 26.3, 31.0]],
    "Indonesian": [[63.5, 72.5, 73.1, 83.5], [24.4, 23.8, 28.0, 33.3]],
    "Hindi": [[72.6, 81.1, 85.5, 97.1], [24.6, 25.1, 27.4, 31.3]]
}


def plot_each_language(ax, lang, y, y2):
    # Refer to https://github.com/jbmouret/matplotlib_for_papers.
    x = [0.56, 1.7, 3.0, 7.1]
    # y = [30, 40, 50, 100]
    # y2 = [25, 25, 25, 33]
    # lang = "Arabic"
    title(lang)

    dataset = "Vicuna-80"
    line_1 = ax.plot(x, y, color='lightskyblue', linewidth=2.5, linestyle='-', marker='o', label=dataset)

    dataset = "MMLU"
    ax_right = ax.twinx()
    line_2 = ax_right.plot(x, y2, color='lightcoral', linewidth=2.5, linestyle='-', marker='v', label=dataset)

    lines = line_1 + line_2
    labels = [l.get_label() for l in lines]

    ax.legend(lines, labels, loc=0)
    ax.grid()

    xticks([0.56, 1.7, 3.0, 7.1], ['0.6', '1.7', '3.0', '7.1'])
    ax.set_ylim(55, 105)
    ax_right.set_ylim(23, 40)

    tight_layout()

    # plot(x, y[0], color='red', linewidth=2.5, linestyle='-', label='linestyle="_"')
    # plot(x, y[1], color='blue', linewidth=5, alpha=0.5, linestyle='-', label='lines tyle="-"')
    # plot(x, y, color='#aa0000', linewidth=2.5, linestyle='-', label='linestyle="--"')
    # plot(x, y[3], color='black', linestyle=':', label='linestyle=":"')
    # plot(x, y[4], color='black', linewidth=2, linestyle='-.', label='linestyle="-."')


def plot_all_languages():
    figure(figsize=(16, 8))
    for i, res in enumerate(results.items()):
        ax = subplot(2, 4, i + 1)
        plot_each_language(ax, res[0], res[1][0], res[1][1])
    tight_layout()
    savefig('eval/plots/scaling_languages.pdf')


if __name__ == '__main__':
    plot_all_languages()
