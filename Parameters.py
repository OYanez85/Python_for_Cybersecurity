def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = (failed_attempts / total_attempts) * 100
    return fail_percentage

percentage = calculate_fails(4,2)
print(f"{percentage}%")