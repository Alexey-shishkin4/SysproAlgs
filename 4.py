import subprocess
import os


def get_commit_range(repo_path, good_commit, bad_commit):
    os.chdir(repo_path)
    commit_list = subprocess.run(['git', 'log', '--pretty=%H', f'{good_commit}..{bad_commit}'], capture_output=True,
                                 text=True)
    commits = list(reversed(commit_list.stdout.strip().split('\n')))
    return commits


def test_commit(commit_hash, test_command):
    result = subprocess.run(['git', 'checkout', commit_hash], capture_output=True)
    if result.returncode != 0:
        return False
    result = subprocess.run(test_command.split(), capture_output=True)
    subprocess.run(['git', 'checkout', '-'])
    return result.returncode == 0


def binary_search(repo_path, good_commit, bad_commit, test_command):
    commits = get_commit_range(repo_path, good_commit, bad_commit)

    left = 0
    right = len(commits) - 1
    while left <= right:
        mid = left + (right - left) // 2
        commit_hash = commits[mid]
        if test_commit(commit_hash, test_command):
            right = mid - 1
        else:
            left = mid + 1

    return commits[left]


# print(get_commit_range('/home/alex_ghoul/test_repo', '71364d0', 'a700e6c'))
# print(binary_search('/home/alex_ghoul/test_repo', '71364d0', 'a700e6c', './script'))
if __name__ == "__main__":
    repo_path = input("Enter path to the git repository: ")
    good_commit = input("Enter the hash of the good commit: ")
    bad_commit = input("Enter the hash of the bad commit: ")
    test_command = input("Enter the test command: ")

    bad_commit_found = binary_search(repo_path, good_commit, bad_commit, test_command)
    print(f"The first bad commit is: {bad_commit_found}")
