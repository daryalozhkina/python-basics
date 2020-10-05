with open('students_log.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
    #     for row in f:
    #     for sym in row:
    #         print(sym)

        l = len(row)
        shadow = []
        i = 0
        while i < l:
            s_int = ''
            a = row[i]
            # while '0' <= a <= '9':
            #     s_int += a
            #     i += 1
            #     if i < l:
            #         a = row[i]
            #     else:
            #         break
            if '0' <= a <= '9':
                    shadow.append(int(a))
            i += 1
        print(shadow)

        # print(row.split()[0], row.split()[1], row.split()[2].replace(",", ":"), integ)


        # avg = statistics.mean(integ)
        # print(avg