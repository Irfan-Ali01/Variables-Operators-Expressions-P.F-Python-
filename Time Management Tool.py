durations = {}
num_tasks = 5
for i in range(num_tasks):
    task = input("Enter the task name: ")
    duration_in_minutes = float(input("Enter the duration in minutes: "))
    duration_in_seconds = round(duration_in_minutes * 60)
    durations[task] = duration_in_seconds
print("Durations for each task:")
for task, duration in durations.items():
    duration_in_minutes = round(duration / 60, 2)
    print(f"{task}: {duration_in_minutes} minutes")
