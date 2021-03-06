import constants

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set()

__all__ = [
    'plot_loss', 'plot_bleu', 'plot_rouge', 'plot_f1',
    'plot_all_scores', 'plot_num_names'
]


# Not used
def plot_confusion_dataframe(df, nrows=5, with_percents=False, total=None):
    df = df.head(nrows)
    plt.tight_layout()

    if with_percents:
        assert total != None
        percents = df / total * 100

        fig, ax = plt.subplots(1, 2, figsize=(18,5), sharey=True)
        __plot_heatmap(df, ax=ax[0], fmt="d")
        __plot_heatmap(percents, ax=ax[1], fmt="0.1f")

    else:
        fig, ax = plt.subplots()
        __plot_heatmap(df, ax=ax, fmt="d")

    return fig


def plot_loss(history):
    return __plot_history(
        history = history,
        color = constants.COLOR_RED,
        title = 'Average Loss',
        ylabel = 'Loss')


def plot_bleu(history):
    return __plot_history(
        history = history,
        color = constants.COLOR_BLUE,
        title = 'Average BLEU',
        ylabel = 'BLEU')


def plot_rouge(history):
    return __plot_history(
        history = history,
        color = constants.COLOR_RED,
        title = 'Average ROUGE',
        ylabel = 'ROUGE')


def plot_f1(history):
    return __plot_history(
        history = history,
        color = constants.COLOR_GREEN,
        title = 'Average F1 score',
        ylabel = 'F1 score')


def plot_num_names(history):
    return __plot_history(
        history = history,
        color = constants.COLOR_YELLOW,
        title = 'Number of unique names',
        ylabel = '# names')


def plot_all_scores(bleu_history, rouge_history, f1_history):
    fig, ax = plt.subplots()
    x = constants.LOG_EVERY * np.arange(len(bleu_history))
    ax.plot(x, bleu_history, constants.COLOR_BLUE)
    ax.plot(x, rouge_history, constants.COLOR_RED)
    ax.plot(x, f1_history, constants.COLOR_GREEN)
    ax.set_title('Average BLEU, ROUGE, and F1 hiestories')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('')
    return fig


def __plot_history(history, color, title, ylabel, xlabel='Iteration'):
    fig, ax = plt.subplots()
    x = constants.LOG_EVERY * np.arange(len(history))
    ax.plot(x, history, color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig


def __plot_heatmap(df, ax, fmt):
    sns.heatmap(df, ax=ax, annot=True, fmt=fmt, cmap="Blues", cbar=False)
    ax.xaxis.tick_top()
    ax.set_ylabel('')
    ax.tick_params(axis='y', labelrotation=0)
    ax.tick_params(axis='both', labelsize=16)
