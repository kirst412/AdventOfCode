with open('day2_in.txt') as fp:
    lst = fp.read().split('\n')

# check if they are all increasing and differences of 1, 2 or 3
def check_increasing(report_list):
    truth_list = []
    for i in range(len(report_list) - 1):
        delta = int(report_list[i+1]) - int(report_list[i])
        if delta > 0 and delta < 4:
            truth_list.append(True)
        else:
            truth_list.append(False)
    
    return all(truth_list)

# check if they are all decreasing and differences of 1, 2 or 3
def check_decreasing(report_list):
    truth_list = []
    for i in range(len(report_list) - 1):
        delta = int(report_list[i]) - int(report_list[i+1])
        if delta > 0 and delta < 4:
            truth_list.append(True)
        else:
            truth_list.append(False)

    return all(truth_list)

total_reports = 0

for report in lst:
    report_list = report.split(" ")
    inc_boolean = check_increasing(report_list)
    dec_boolean = check_decreasing(report_list)
    if inc_boolean or dec_boolean:
        total_reports += 1

print("Part A answer: ", total_reports)

###########################################################
## Part B
###########################################################

# check if they are all increasing and differences of 1, 2 or 3
def check_increasing(report_list):
    truth_list = []
    for i in range(len(report_list) - 1):
        delta = int(report_list[i+1]) - int(report_list[i])
        if delta > 0 and delta < 4:
            truth_list.append(True)
        else:
            truth_list.append(False)
    
    return all(truth_list)

# check if they are all decreasing and differences of 1, 2 or 3
def check_decreasing(report_list):
    truth_list = []
    for i in range(len(report_list) - 1):
        delta = int(report_list[i]) - int(report_list[i+1])
        if delta > 0 and delta < 4:
            truth_list.append(True)
        else:
            truth_list.append(False)

    return all(truth_list)

total_reports = 0

for report in lst:
    report_list = report.split(" ")
    inc_boolean = check_increasing(report_list)
    dec_boolean = check_decreasing(report_list)
    if inc_boolean or dec_boolean:
        total_reports += 1
    else:
        # try removing each index and see if any pass as safe
        atleast_one_safe_option = []
        for index, item in enumerate(report_list):
            lst_copy = report_list.copy()
            lst_copy.pop(index)
            inc_boolean = check_increasing(lst_copy)
            dec_boolean = check_decreasing(lst_copy)
            if inc_boolean or dec_boolean:
                atleast_one_safe_option.append(True)
        if any(atleast_one_safe_option):
            total_reports += 1



print("Part B answer: ", total_reports)
