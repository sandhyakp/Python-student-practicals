import os
import subprocess
from datetime import datetime, timedelta

# Start and end dates
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 12, 31)

# Generate dates between start and end date
current_date = start_date
while current_date <= end_date:
    commit_date = current_date.strftime("%a %b %d %H:%M:%S %Y +0000")
    
    # Create a temporary file to commit
    with open("temp.txt", "w") as file:
        file.write(f"Commit for {current_date.strftime('%Y-%m-%d')}")
    
    # Stage the file
    subprocess.run(["git", "add", "temp.txt"])
    
    # Commit with the specified date
    subprocess.run(["git", "commit", "--date", commit_date, "-m", f"Backdated commit for {current_date.strftime('%Y-%m-%d')}"])
    
    # Remove the temporary file
    os.remove("temp.txt")
    
    # Move to the next day
    current_date += timedelta(days=1)

