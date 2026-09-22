from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_visualization(rows, summary, output_file="output/redundancy_monitor.png"):
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    status_counts = {}
    for row in rows:
        status_counts[row["Статус"]] = status_counts.get(row["Статус"], 0) + 1

    labels = list(status_counts.keys())
    values = list(status_counts.values())

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    axes[0].bar(labels, values)
    axes[0].set_title("Количество контейнеров по статусам")
    axes[0].set_ylabel("Количество")
    axes[0].tick_params(axis="x", rotation=25)

    axes[1].pie(values, labels=labels, autopct="%1.0f%%", startangle=90)
    axes[1].set_title("Распределение состояния контейнеров")

    summary_labels = ["Всего", "Разрешенных", "Избыточных"]
    summary_values = [
        summary["Всего запущено"],
        summary["Разрешенных"],
        summary["Избыточных"],
    ]
    axes[2].bar(summary_labels, summary_values)
    axes[2].set_title("Сводные показатели проверки")
    axes[2].set_ylabel("Количество")

    fig.suptitle(
        f"Контроль системной избыточности УБИ.166 — {summary['Результат']}"
    )
    fig.tight_layout()
    fig.savefig(output_file, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return output_file
