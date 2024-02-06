import argparse
import os
import subprocess


def execute(command):
    return subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode


def is_bad(commit):
    execute(f'git checkout {commit}')
    result = execute(' '.join(args.command)) != 0
    execute('git checkout -')
    return result


parser = argparse.ArgumentParser()
parser.add_argument('repo_path')
parser.add_argument('first_commit')
parser.add_argument('latest_commit')
parser.add_argument('command', nargs='+')
args = parser.parse_args()

os.chdir(args.repo_path)

command = f'git log {args.first_commit}..{args.latest_commit} --oneline'
output = subprocess.check_output(command, shell=True, text=True).splitlines()
commits = [i.split()[0] for i in output]


low = 0
high = len(commits) - 1
while low <= high:
    mid = (low + high) // 2
    if is_bad(commits[mid]):
        high = mid - 1
    else:
        low = mid + 1

if low < len(commits):
    print(f"Первый плохой коммит: {commits[low]}")
else:
    print("Нет 'плохих' коммитов")

execute('git checkout -')