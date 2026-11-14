================================================================================
              🚀 GIT & GITHUB — THE ABSOLUTE BASICS
================================================================================

ONE-TIME SETUP (do this once, ever):
─────────────────────────────────────
  git config --global user.name "Your Name"
  git config --global user.email "you@email.com"


START A NEW PROJECT:
─────────────────────
  mkdir my-project          # create folder
  cd my-project             # go inside
  git init                  # 🌟 turn on git tracking


DAILY WORKFLOW (repeat every time you work):
─────────────────────────────────────────────

  1.  git status            # 👀 what changed?

  2.  git add .             # 📦 stage all changes

  3.  git commit -m "what I did"   # 💾 save snapshot

  4.  git push              # ☁️ upload to GitHub


SEE HISTORY:
─────────────
  git log --oneline         # 📜 see all your saves


CONNECT TO GITHUB (one-time per project):
──────────────────────────────────────────
  # 1. Create repo on github.com (empty, no README)
  # 2. Then run:

  git remote add origin https://github.com/YOU/repo-name.git
  git push -u origin main


DOWNLOAD SOMEONE'S PROJECT:
────────────────────────────
  git clone https://github.com/someone/repo-name.git


DOWNLOAD LATEST CHANGES:
─────────────────────────
  git pull


THAT'S IT. 5 COMMANDS YOU'LL USE EVERY DAY:
────────────────────────────────────────────
  git status                # 👀 check
  git add .                 # 📦 stage
  git commit -m "message"   # 💾 save
  git push                  # ⬆️ upload
  git pull                  # ⬇️ download

================================================================================


================================================================================
              🔧 GIT & GITHUB — INTERMEDIATE LEVEL
================================================================================

📌 PREREQUISITE: You already know add, commit, push, pull, clone.


================================================================================
1. BRANCHING & MERGING
================================================================================

  git branch                  # list all branches
  git branch feature-login    # create branch
  git checkout feature-login  # switch to it
  git checkout -b feature-ui  # create + switch (shortcut)

  # ... make changes, add, commit on the branch ...

  git checkout main           # switch back to main
  git merge feature-login     # merge branch INTO main
  git branch -d feature-login # delete branch when done


  VISUAL:
  main:        A → B → C ──────────→ F (merge)
                         ↘          ↗
  feature-login:          D → E ────


================================================================================
2. MERGE CONFLICTS (when two people edit the same line)
================================================================================

  # Git will tell you which files conflict. Open them:

  <<<<<<< HEAD
  your code here
  =======
  their code here
  >>>>>>> feature-branch

  # FIX:
  #   1. Manually edit the file — keep what you want, delete markers
  #   2. git add <file>
  #   3. git commit -m "Resolve merge conflict"


================================================================================
3. UNDOING MISTAKES
================================================================================

  # Fix last commit message:
  git commit --amend -m "corrected message"

  # Add forgotten file to last commit:
  git add forgotten-file.txt
  git commit --amend --no-edit

  # Undo changes in a file (before staging):
  git restore filename.txt

  # Unstage a file (after git add, before commit):
  git restore --staged filename.txt

  # Undo a commit but keep changes (safe):
  git revert <commit-hash>

  # Nuke everything back to a commit (⚠️ DESTRUCTIVE):
  git reset --hard <commit-hash>

  # Undo last commit but keep changes staged:
  git reset --soft HEAD~1


  DECISION TREE:
  ┌─ Not staged yet?     → git restore <file>
  ├─ Staged, not commit? → git restore --staged <file>
  ├─ Committed, not push?→ git commit --amend / git reset --soft
  └─ Already pushed?     → git revert (NEVER reset --hard on shared)


================================================================================
4. STASHING (save work temporarily without committing)
================================================================================

  git stash                 # save current changes & clean workspace
  git stash list            # see all stashes
  git stash pop             # restore latest stash & remove it
  git stash apply           # restore latest stash & keep it
  git stash drop            # delete latest stash
  git stash clear           # delete ALL stashes

  # USE CASE: You're working on feature-A, boss says "fix bug NOW!"
  #   git stash
  #   git checkout -b hotfix
  #   ... fix bug, commit, push, merge ...
  #   git checkout feature-A
  #   git stash pop          ← your work is back!


================================================================================
5. .gitignore (tell Git to ignore files)
================================================================================

  # Create file named .gitignore in project root:

  node_modules/       # ignore folder
  .env                # ignore secrets
  *.log               # ignore all .log files
  build/              # ignore build output
  .DS_Store           # ignore Mac junk

  # If file is already tracked, remove it first:
  git rm --cached .env
  git commit -m "Stop tracking .env"


================================================================================
6. WORKING WITH REMOTES
================================================================================

  git remote -v                       # see connected remotes
  git remote add upstream <url>       # add original repo (for forks)
  git fetch origin                    # download changes, don't merge
  git pull origin main                # fetch + merge
  git push origin feature-branch      # push a specific branch
  git push -u origin feature-branch   # push & set upstream (first time)
  git branch -r                       # list remote branches
  git branch -a                       # list ALL branches (local + remote)


================================================================================
7. TAGS & RELEASES
================================================================================

  git tag v1.0.0                      # lightweight tag
  git tag -a v1.0.0 -m "First release" # annotated tag (recommended)
  git tag                             # list all tags
  git push origin v1.0.0              # push tag to GitHub
  git push origin --tags              # push ALL tags
  git checkout v1.0.0                 # view code at that tag


================================================================================
8. COLLABORATION WORKFLOW (Fork + Pull Request)
================================================================================

  # 1. FORK the repo on GitHub (click Fork button)
  # 2. CLONE your fork:
     git clone https://github.com/YOU/original-repo.git
     cd original-repo

  # 3. CONNECT to original repo:
     git remote add upstream https://github.com/ORIGINAL/repo.git

  # 4. CREATE branch, make changes:
     git checkout -b my-feature
     # ... edit, add, commit ...

  # 5. PUSH to YOUR fork:
     git push origin my-feature

  # 6. OPEN Pull Request on GitHub (your fork → original repo)

  # 7. KEEP YOUR FORK UPDATED:
     git fetch upstream
     git checkout main
     git merge upstream/main
     git push origin main


================================================================================
9. USEFUL INTERMEDIATE COMMANDS
================================================================================

  git log --oneline --graph --all   # 🌳 visual branch history
  git log --author="Name"           # commits by specific person
  git log --since="2024-01-01"     # commits since date
  git diff main..feature            # compare two branches
  git diff HEAD~2                   # changes in last 2 commits
  git show <commit-hash>            # see details of one commit
  git cherry-pick <commit-hash>     # copy one commit to current branch
  git shortlog -sn                  # who made how many commits


================================================================================
10. COMMON SCENARIOS
================================================================================

  "I committed to main by mistake!"
  ──────────────────────────────────
    git checkout -b feature-branch    # move work to new branch
    git checkout main
    git reset --hard origin/main      # reset main to remote
    git checkout feature-branch       # your work is safe here

  "I want to combine my last 3 commits into one"
  ────────────────────────────────────────────────
    git rebase -i HEAD~3
    # In editor: change "pick" to "squash" for commits 2 & 3
    # Save & write new commit message

  "Someone force-pushed and my branch is broken"
  ────────────────────────────────────────────────
    git fetch origin
    git rebase origin/main

  "I want to see what changed between my branch and main"
  ────────────────────────────────────────────────────────
    git diff main...my-branch


================================================================================
📊 SKILL PROGRESSION
================================================================================

  BEGINNER        INTERMEDIATE (you are here)      ADVANCED
  ────────        ──────────────────────────       ────────
  add             branching & merging              interactive rebase
  commit          merge conflicts                  bisect
  push/pull       stashing                         submodules
  clone           .gitignore                       hooks
  status          revert / reset                   reflog
                  tags                             worktrees
                  fork + PR workflow               cherry-pick
                  remote management                git flow


================================================================================