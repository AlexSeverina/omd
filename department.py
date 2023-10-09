import csv


def read_file(file_name: str) -> list:
    """
    Reads data from csv-file with the given name.

    :param file_name: Name of the csv-file to read from
    :return: data from csv-file where each row is represented by dict
    """
    data = list()
    with open(file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def separate_data(data: list, by: str) -> dict:
    """
    Separates data of employees into lists by some criteria.

    :param data: list where each employee is represented by dict
    :param by: name of the field of separation
    :return: for each field instance list of its employees
    """
    separated_data: dict[str, list] = dict()
    for row in data:
        if row[by] in separated_data.keys():
            separated_data[row[by]].append(row)
        else:
            separated_data[row[by]] = [
                row,
            ]
    return separated_data


def print_hierarchy(data: dict):
    """
    Prints hierarchy of the commands in departments.

    :param data: data separated by departments
    :return:
    """
    for dep, person_list in data.items():
        print(f"Название департамента: {dep}")
        commands = separate_data(person_list, by="Отдел")

        for command_name, command_employees in commands.items():
            print(f"\tОтдел: {command_name}")
            print("\tСотрудники:")
            for employee in command_employees:
                print(f'\t\t{employee["ФИО полностью"]}')


def get_report(data: dict) -> list:
    """
    Transforms data to the department report.

    :param data: departments data in format department name: list of employees
    :return: list of dicts for every department with info about them
    """
    report = list()
    for dep, person_list in data.items():
        salary = [int(person["Оклад"]) for person in person_list]
        report.append(
            {
                "Название департамента": dep,
                "Численность": len(person_list),
                "Вилка зарплат": f"{min(salary)}-{max(salary)}",
                "Средняя зарплата": f"{sum(salary) / len(person_list):.2f}",
            }
        )
    return report


def print_report(data: dict):
    """
    Creates report based on data and prints it to stdout.

    :param data: data to make the report
    :return:
    """
    report = get_report(data)

    print("Сводный отчет по департаментам.")
    for dep in report:
        for key, val in dep.items():
            print(f"{key}: {val}")
        print("\n")


def save_report(data: dict, name: str):
    """
    Creates report based on data and saves it to csv-file with the given name.

    :param data: data to make the report
    :param name: string to name the resulting csv-file
    :return:
    """
    report = get_report(data)
    if not report:
        return

    with open(name, "w", newline="") as csvfile:
        fieldnames = report[0].keys()
        writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=fieldnames)
        writer.writeheader()

        for row in report:
            writer.writerow(row)


if __name__ == "__main__":
    filename = "Corp_Summary"
    corp_data = separate_data(read_file(filename + ".csv"), by="Департамент")

    while True:
        print("Меню:")
        print("1. Вывести иерархию команд")
        print("2. Вывести сводный отчет по департаментам")
        print("3. Сохранить сводный отчет по департаментам")

        n = int(input())
        if n == 1:
            print_hierarchy(corp_data)
        elif n == 2:
            print_report(corp_data)
        elif n == 3:
            save_report(corp_data, name=filename + "_report.csv")
        else:
            print("Неизвестная команда!")
