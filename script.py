import os
import random
import subprocess
from datetime import datetime, timedelta

os.chdir(r"D:\LeafDiseasesDataset\lirope\beefbesees\LeafDisease")

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 3, 20)

current = start_date

while current <= end_date:
    commits_today = random.randint(1, 7)
    print(f"{current.date()} -> {commits_today} commits")

    for _ in range(commits_today):
        commit_time = current.replace(
            hour=random.randint(9, 23),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )

        date_str = commit_time.strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as f:
            f.write(date_str + "\n")

        subprocess.run(["git", "add", "."], check=True)

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str

        subprocess.run(
            ["git", "commit", "-m", "update"],
            env=env,
            check=True
        )

    current += timedelta(days=1)

print("DONE")