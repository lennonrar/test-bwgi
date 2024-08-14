import datetime as dt

def reconcile_accounts(
        csv_list_a: list[list[str]],
        csv_list_b: list[list[str]]
) -> [list[list[str]]]:
    for row in csv_list_a:
        i = 0
        while i < 3:
            new_date = dt.datetime.strptime(row[0], '%Y-%m-%d') + dt.timedelta(days=i-1)
            check_row = [new_date.strftime('%Y-%m-%d'), row[1], row[2], row[3]]

            if check_row in csv_list_b:
                csv_list_b[csv_list_b.index(check_row)].append('FOUND')
                csv_list_a[csv_list_a.index(row)].append('FOUND')
                break

            i += 1

    for j in range(len(csv_list_a)):
        if csv_list_a[j][-1] != 'FOUND':
            csv_list_a[j].append('MISSING')
        if csv_list_b[j][-1] != 'FOUND':
            csv_list_b[j].append('MISSING')

    return [csv_list_a, csv_list_b]

