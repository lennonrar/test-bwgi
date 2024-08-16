import datetime as dt


def reconcile_accounts(
    csv_list_a: list[list[str]], csv_list_b: list[list[str]]
) -> [list[list[str]]]:
    """
    Compare two CSV files and mark the rows that are missing or found in the other file.
    :param csv_list_a: list of lists representing the first CSV file
    :param csv_list_b: list of lists representing the second CSV file
    :return: list of lists with the rows marked as MISSING or FOUND
    """
    for row in csv_list_a:
        i = 0
        while i < 3:
            new_date = dt.datetime.strptime(row[0], "%Y-%m-%d") + dt.timedelta(
                days=i - 1
            )
            check_row = [new_date.strftime("%Y-%m-%d"), row[1], row[2], row[3]]

            if check_row in csv_list_b:
                csv_list_b[csv_list_b.index(check_row)].append("FOUND")
                csv_list_a[csv_list_a.index(row)].append("FOUND")
                break

            i += 1

    for j in range(len(csv_list_a)):
        if csv_list_a[j][-1] != "FOUND":
            csv_list_a[j].append("MISSING")

    for k in range(len(csv_list_b)):
        if csv_list_b[k][-1] != "FOUND":
            csv_list_b[k].append("MISSING")

    return [csv_list_a, csv_list_b]
