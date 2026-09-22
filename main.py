from calculator import analyze_containers
from table_view import build_table
from logger_utils import write_log
from secrets_check import check_secrets

try:
    from visualization import build_visualization
except ImportError:
    build_visualization = None


def main():
    print("=== Контейнер контроля системной избыточности УБИ.166 ===")

    secret_state = check_secrets()
    print("Состояние Secrets:")
    for name, state in secret_state.items():
        print(f"  {name}: {state}")

    rows, summary, config = analyze_containers()
    dataframe = build_table(rows)
    write_log(summary, rows, config["log_file"])

    print("\nРезультаты проверки:")
    print(dataframe.to_string(index=False))
    print("\nСводка:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\nТаблица сохранена: output/results.csv")
    if build_visualization is not None:
        image_path = build_visualization(rows, summary)
        print(f"Графики сохранены: {image_path}")
    else:
        print("Модуль визуализации отсутствует: расчет и таблица продолжают работать.")
    print(f"Лог сохранен: {config['log_file']}")


if __name__ == "__main__":
    main()
