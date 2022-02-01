# CD

Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anything from GitHub Actions or Bash to Digital Ocean and SSH.

Discuss three problems that you encountered along the way and how you solved them.

### 1. Initial run tests workflow failed because Flask was not found

```ModuleNotFoundError: No module named 'flask'```   
Solution: Add flask to requirements.txt

### 2. Updated code did not become visible on the actual website
Solution: I found out that after updating the Python code of the Flask app it is necessary to restart the service on the Ubuntu server using `systemctl restart cd`. It seems that `systemctl restart nginx` is not needed to make changes visible on the actual website.

(optional) Anything of note that you want to share about the process of solving this assignment.

![example workflow](https://github.com/jellerodenburg/CD/actions/workflows/run-test.yml/badge.svg)
