# 🚀 Git & Pull Request Practice Guide

Welcome! This repository is set up for practicing Git workflows and learning how to create and submit Pull Requests (PRs) on GitHub.

---

## 🛠️ Step-by-Step Pull Request Guide

### 1. Clone the Repository & Create a Branch
Before making changes, always create a dedicated branch so you don't commit directly to `main`.

```bash
# Clone this repository to your computer
git clone <REPOSITORY_URL>
cd <REPOSITORY_FOLDER>

# Make sure you have the latest code from main
git checkout main
git pull origin main

# Create and switch to your feature branch
git checkout -b feature/your-name-practice
```

---

### 2. Make Your Edits & Commit Changes
Make your changes or complete your exercise in your editor, then save your progress using Git.

```bash
# Check which files you modified
git status

# Stage all updated files
git add .

# Save a snapshot of your changes with a clear message
git commit -m "Add my changes for the practice exercise"
```

---

### 3. Push Your Branch to GitHub
Send your local branch up to GitHub.

```bash
# Push your branch to the remote repository
git push -u origin feature/your-name-practice
```

---

### 4. Open a Pull Request (PR)

1. Navigate to the repository page on **GitHub**.
2. Click the yellow **"Compare & pull request"** banner near the top of the page.
3. Title your PR clearly (e.g., `Practice PR - [Your Name]`).
4. Add a quick summary of what you did in the description field.
5. Click **Create pull request**! 🎉

---

## 🔄 How to Update an Open PR
If your reviewer asks for changes or you spot a mistake after opening a PR, you don't need to open a new PR:

1. Make your edits locally on your branch.
2. Run `git add .`
3. Run `git commit -m "Address feedback"`
4. Run `git push`

*GitHub will automatically update your existing Pull Request!*
