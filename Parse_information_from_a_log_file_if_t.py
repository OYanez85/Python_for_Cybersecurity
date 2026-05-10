# Parse information from a log file if the status code != 200
def parse_line(line):
    error_code = line[0:3]

    if (error_code == "200"):
        return "Successful event - no parsing needed."

    date = line[4:12]
    time = line[13:21]
    application_name = line[22:43]

    parsed_line = []
    parsed_line.insert(0, error_code)
    parsed_line.insert(1, date)
    parsed_line.insert(2, time)
    parsed_line.insert(3, application_name)

    return parsed_line


final_parsed_line = parse_line("200 02082022 05:11:00 buffer_application")
print(final_parsed_line)
