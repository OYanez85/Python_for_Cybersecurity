# Extract email addresses

import re
email_log = """Email received June 2 from user1@email.com.
            Email received June 2 from user2@email.com.
            Email rejected June 2 from invalid_email@email.com."""
print(re.findall("\w+@\w+\.\w+".email_log))

# import re
import re
re.findall("ts", "tsnow, tshah, bmoreno")
# output: ['ts', 'ts']

# Regular expressions symbols
## Symbols for character types

import re
re.findall("\w", "h32rb17")
# output: ['h', '3', '2', 'r', 'b', '1', '7']

import re
re.findall("\d", "h32rb17")
# output: ['3', '2', '1', '7']

# Symbols to quantify ocurrences
import re
re.findall("\d+", "h32rb17")
# output: ['32', '17']

import re
re.findall("\d*", "h32rb17")
# output: ['', '32', '', '', '17', '']

import re
re.findall("\d{2}", "h32rb17 k825t0m c2994eh")
# output: ['32', '17', '82', '29', '94']

import re
re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")
# output: ['32', '17', '825', '0', '299', '4']

# Constructing a pattern
import re
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))
# ['bmoreno: 12', 'tshah: 7', 'sgilmore: 5']