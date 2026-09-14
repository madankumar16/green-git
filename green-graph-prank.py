import os
from datetime import datetime, timedelta

# Terminal colors for the hacker vibe
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Configurations
days_back = 365       # How many days in the past to go
commits_per_day = 4   # Number of commits per day (controls the green shade)

# Calculate the starting date
start_date = datetime.now() - timedelta(days=days_back)

print(f"\n{RED}🚨 SYSTEM OVERRIDE: Planting fake commits for 1 YEAR...{RESET}\n")

# Step 1: Loop through the past 365 days
for i in range(days_back + 1):
    current_date = start_date + timedelta(days=i)
    formatted_date = current_date.strftime("%Y-%m-%dT12:00:00")
    
    # Step 2: Plant the fake commits for each day
    for _ in range(commits_per_day):
        # Overriding the system dates in Git
        cmd = f'GIT_COMMITTER_DATE="{formatted_date}" GIT_AUTHOR_DATE="{formatted_date}" git commit --allow-empty -m "Fake commit" > /dev/null'
        os.system(cmd)
        
    print(f"{GREEN}✅ Fake Green Square planted for: {formatted_date[:10]}{RESET}")

# Step 3: Prompt the user for the final almighty push
print(f"\n{RED}🔥 All commits staged!{RESET}")
print(f"👉 Now run this command in your terminal: {GREEN}git push -u origin main --force{RESET}\n")
