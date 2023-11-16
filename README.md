
### Date created
16-11-2023.

### Project Title
Udacity Git Project

### Description
This project aims to introduce beginners to version control using Git. Participants will start by cloning the repository, creating branches for new features, and submitting pull requests. Each task, such as adding a new task or implementing task prioritization, can be a separate branch, allowing contributors to practice branching, merging, and collaborating on a project using Git. This project encourages learning Git in the context of a practical application, making it ideal for those new to version control.

### Git Commands Documentation
Git Commands Documentation Report
Introduction
This document provides a concise guide to essential Git commands for effective version control. I forked a repository from Udacity's GitHub Project to my github repo(https://github.com/Emzykings/pdsnd_github.git).

1. Forking a Repository

Clone the repository to your local machine:
git clone https://github.com/emzykings/pdsnd_github.git

Navigate to the project directory:
cd pdsnd_github

Add the original repository as a remote:
git remote add upstream https://github.com/Udacity/pdsnd_github.git


2. Keeping Your Fork Updated

Sync Your Fork with the Original Repository
Fetch the changes from the upstream repository:
git fetch upstream

Switch to the main branch:
git checkout main

Merge the changes from the upstream repository into your fork:
git merge upstream/main

Push the updated main branch to your fork on GitHub:
git push origin main

3. Making Changes

Create a Branch for Your Changes
Create a new branch for your feature or bug fix:
git checkout -b feature-branch

Stage and Commit Changes
Stage your changes:
git add .

Commit your changes with a descriptive message:
git commit -m "Update"

Push Changes to Your Fork
Push the changes to your fork on GitHub:
git push origin feature-branch


Collaborating and Pull Requests

Create a Pull Request:
Navigate to your fork on GitHub.
Select the branch you want to merge into the original repository.
Click on "New Pull Request" and follow the prompts.

Review and Merge:
Collaborate with other contributors in the pull request.
Once approved, click "Merge Pull Request" on GitHub.



### Credits

1. **GitHub Explore:**
   - [GitHub Explore](https://github.com/explore): Explore GitHub repositories to find projects in various programming languages and domains. You can filter by topics and languages to find projects suitable for beginners.

2. **Up For Grabs:**
   - [Up For Grabs](https://up-for-grabs.net/): This website lists projects with tasks specifically tagged for newcomers. It's a good place to find projects that welcome contributions from beginners.

3. **First Contributions:**
   - [First Contributions](https://github.com/firstcontributions/first-contributions): A beginner-friendly project that helps you make your first contribution to open source. It provides a step-by-step guide.

4. **Awesome for Beginners:**
   - [Awesome for Beginners](https://github.com/MunGell/awesome-for-beginners): A curated list of awesome beginner-friendly projects. It covers a variety of programming languages and domains.

5. **Your First PR:**
   - [Your First PR](https://yourfirstpr.github.io/): Similar to First Contributions, this project aims to help beginners make their first pull request.

6. **Git Immersion:**
   - [Git Immersion](http://gitimmersion.com/): A guided tour to get hands-on experience with Git. It's not a project per se, but it's an excellent resource to learn Git through practical exercises.

7. **Simple Python Projects:**
   - [30 Python Projects in 30 Days](https://github.com/Asabeneh/30-Days-Of-Python): While this is focused on Python, it's a great source of simple projects for beginners. You can practice Git by maintaining version control for your code.

8. **Beginner-Friendly Repositories on GitHub:**
   - [Beginner-Friendly Repositories](https://github.com/jrwdunham/beginner-projects): A collection of beginner-friendly repositories on GitHub.


