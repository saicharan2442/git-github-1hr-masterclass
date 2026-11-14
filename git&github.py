================================================================================
          🚀 GIT & GITHUB 1-HOUR MASTERCLASS FOR COMPLETE BEGINNERS
================================================================================

📋 TIMELINE OVERVIEW
────────────────────────────────────────────────────────────────────────────────
  0:00 - 0:05  │ What is Git & GitHub?                  │ Theory
  0:05 - 0:10  │ Installation & Setup                   │ Practical
  0:10 - 0:25  │ Core Git Commands                      │ Practical
  0:25 - 0:35  │ GitHub - Remote Repositories           │ Practical
  0:35 - 0:45  │ Branching & Merging                    │ Practical
  0:45 - 0:55  │ Collaboration (Pull Requests)          │ Practical
  0:55 - 1:00  │ Cheat Sheet & Q&A                      │ Wrap-up
────────────────────────────────────────────────────────────────────────────────


================================================================================
⏱️  PART 1: WHAT IS GIT & GITHUB?  (0:00 - 0:05)
================================================================================

🧠 ANALOGY — Think of Git like a "SAVE GAME" in a video game:

  WITHOUT Git:                          WITH Git:
  ─────────────                         ─────────
  report_final.doc                      report.doc → full history tracked 😎
  report_final_v2.doc                   - Go back to ANY previous save
  report_final_FINAL.doc                - Multiple people work simultaneously
  report_final_FINAL_really_final.doc 😫


KEY CONCEPTS:
  ┌─────────────────────────────────────────────────────┐
  │  GIT    = Version Control System (on YOUR computer) │
  │  GITHUB = Cloud hosting for Git repos (online)      │
  │           (Like Google Drive for code)              │
  │  GIT ≠ GITHUB  (Git works without GitHub!)          │
  └─────────────────────────────────────────────────────┘


THE 3 STAGES OF GIT (CRITICAL CONCEPT):

  Working Directory  →  Staging Area  →  Repository
  (Your files)          (Ready to save)   (Saved permanently)
       📝                   📦                 💾

    git add              git commit
  ──────────►          ──────────────►


================================================================================
⏱️  PART 2: INSTALLATION & SETUP  (0:05 - 0:10)
================================================================================

STEP 1: INSTALL GIT
───────────────────
  # Check if Git is already installed
  git --version

  # If not installed:
  # Windows: Download from https://git-scm.com/download/win
  # Mac:     brew install git  (or download from git-scm.com)
  # Linux:   sudo apt install git


STEP 2: CONFIGURE GIT (FIRST TIME ONLY)
────────────────────────────────────────
  # Set your name (appears in your commits)
  git config --global user.name "Your Name"

  # Set your email (use the same email as your GitHub account)
  git config --global user.email "your.email@example.com"

  # Verify your configuration
  git config --list


STEP 3: CREATE A GITHUB ACCOUNT
────────────────────────────────
  🌐 Go to https://github.com
  📧 Sign up with your email
  ✅ Verify your account


================================================================================
⏱️  PART 3: CORE GIT COMMANDS — HANDS-ON PROJECT  (0:10 - 0:25)
================================================================================

🎯 PROJECT: Build a Simple Portfolio Page


STEP 1: CREATE PROJECT FOLDER & INITIALIZE GIT
───────────────────────────────────────────────
  mkdir my-portfolio
  cd my-portfolio

  # 🌟 Initialize Git in this folder
  git init
  # Output: "Initialized empty Git repository in .../my-portfolio/.git/"

  # Check status (you'll use this ALL the time)
  git status


STEP 2: CREATE YOUR FIRST FILE
───────────────────────────────
  # Create an HTML file
  touch index.html          # Mac/Linux
  New-Item index.html       # Windows PowerShell

  # Open index.html in a text editor and add:

  <!DOCTYPE html>
  <html>
  <head>
      <title>My Portfolio</title>
  </head>
  <body>
      <h1>Hello! I'm [Your Name]</h1>
      <p>Welcome to my portfolio.</p>
  </body>
  </html>


STEP 3: STAGE AND COMMIT
─────────────────────────
  # Check status — file should show as "Untracked"
  git status

  # 🌟 Stage the file (add to staging area)
  git add index.html

  # Check status again — should show "Changes to be committed"
  git status

  # 🌟 Commit (save snapshot)
  git commit -m "Add initial portfolio page"

  # ✅ Congratulations! You made your first commit!


STEP 4: MAKE CHANGES AND COMMIT AGAIN
──────────────────────────────────────
  # Edit index.html — add more content:

  <!DOCTYPE html>
  <html>
  <head>
      <title>My Portfolio</title>
  </head>
  <body>
      <h1>Hello! I'm [Your Name]</h1>
      <p>Welcome to my portfolio.</p>

      <h2>My Skills</h2>
      <ul>
          <li>HTML</li>
          <li>CSS</li>
          <li>Git & GitHub</li>
      </ul>
  </body>
  </html>

  # Check what changed
  git status

  # 🌟 See exact changes (line by line)
  git diff

  # Stage and commit
  git add index.html
  git commit -m "Add skills section"


STEP 5: ADD ANOTHER FILE
─────────────────────────
  # Create style.css:   

  body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background-color: #f0f0f0;
  }
  h1 { color: #333; }

  # Update index.html <head> to link CSS:
  <link rel="stylesheet" href="style.css">

  # 🌟 Stage ALL changed/new files at once
  git add .

  # Commit
  git commit -m "Add styling with CSS"


STEP 6: VIEW HISTORY
─────────────────────
  # 🌟 See all commits
  git log

  # Compact view (one line per commit)
  git log --oneline
  # Output:
  #   a3b4c5d Add styling with CSS
  #   f6g7h8i Add skills section
  #   j9k0l1m Add initial portfolio page


VISUAL SUMMARY:
  Commit 1              Commit 2              Commit 3
  ──────►               ──────►               ──────►
  "Add initial          "Add skills           "Add styling
   portfolio page"       section"              with CSS"


BONUS UNDO COMMANDS:
  git restore index.html          # Discard unstaged changes
  git restore --staged index.html # Unstage a file
  git blame index.html            # See who changed each line


================================================================================
⏱️  PART 4: GITHUB — REMOTE REPOSITORIES  (0:25 - 0:35)
================================================================================

🎯 GOAL: Push our local project to GitHub


STEP 1: CREATE A REPOSITORY ON GITHUB
──────────────────────────────────────
  🌐 Go to github.com → Click "+" → "New Repository"
  📝 Fill in:
     Repository name: my-portfolio
     Description: My first portfolio website
     ✅ Public
     ❌ Do NOT initialize with README (we already have files)
  📋 Click "Create Repository"


STEP 2: CONNECT LOCAL REPO TO GITHUB
─────────────────────────────────────
  # 🌟 Add GitHub as a remote (copy URL from GitHub page)
  git remote add origin https://github.com/YOUR-USERNAME/my-portfolio.git

  # Verify
  git remote -v

  # 🌟 Push your code to GitHub!
  git push -u origin main
  # Note: use 'master' instead of 'main' if your default branch is 'master'


AUTHENTICATION (if prompted):
  Option A: Personal Access Token (PAT)
    GitHub → Settings → Developer Settings → Personal Access Tokens → Generate
    Use this token as your "password"

  Option B: SSH (Recommended long-term)
    ssh-keygen -t ed25519 -C "your.email@example.com"
    cat ~/.ssh/id_ed25519.pub
    # Copy output → GitHub → Settings → SSH Keys → New SSH Key → Paste


STEP 3: VERIFY ON GITHUB
─────────────────────────
  🌐 Refresh your GitHub repository page
  ✅ You should see all your files and commit history!


STEP 4: CREATE README ON GITHUB (Edit online)
──────────────────────────────────────────────
  🌐 On GitHub → Click "Add file" → "Create new file"
  📝 Name: README.md
  Content:

  # My Portfolio 🎨
  This is my personal portfolio website built while learning Git & GitHub!
  ## Technologies Used
  - HTML
  - CSS

  💾 Click "Commit new file"


STEP 5: PULL CHANGES FROM GITHUB
─────────────────────────────────
  # 🌟 Download changes made on GitHub to your local machine
  git pull origin main

  # You should now have README.md locally!
  ls
  # Output: index.html  style.css  README.md


UNDERSTANDING PUSH & PULL:
   YOUR COMPUTER                         GITHUB (Cloud)
  ┌──────────────┐                    ┌──────────────────┐
  │              │   git push ──────► │                  │
  │  Local Repo  │                    │  Remote Repo     │
  │              │   git pull ◄────── │  (origin)        │
  └──────────────┘                    └──────────────────┘


================================================================================
⏱️  PART 5: BRANCHING & MERGING  (0:35 - 0:45)
================================================================================

🧠 WHY BRANCHES?

  Without Branches:                With Branches:
  A → B → C → 💥BROKEN!           A → B → C (main — stable)
                                         ↘
                                          D → E (feature — experimental)
                                         ↙
                                   A → B → C → F (merged safely!)


🎯 PRACTICAL: Add a Contact Section Using a Branch


STEP 1: CREATE AND SWITCH TO A NEW BRANCH
──────────────────────────────────────────
  git branch                    # See current branch

  # 🌟 Create and switch to new branch
  git checkout -b feature-contact
  # Or newer syntax: git switch -c feature-contact

  git branch
  # Output:
  #   main
  # * feature-contact    ← you are here


STEP 2: MAKE CHANGES ON THE NEW BRANCH
───────────────────────────────────────
  # Add to index.html:
      <h2>Contact Me</h2>
      <p>Email: yourname@example.com</p>
      <p>GitHub: github.com/your-username</p>

  # Add to style.css:
  h2 {
      color: #0066cc;
      border-bottom: 2px solid #0066cc;
      padding-bottom: 5px;
  }

  git add .
  git commit -m "Add contact section and improve styling"


STEP 3: SWITCH BACK TO MAIN AND SEE THE DIFFERENCE
───────────────────────────────────────────────────
  git checkout main

  # Open index.html — CONTACT SECTION IS GONE! 😱
  # Don't worry — it's safe on the feature-contact branch

  git checkout feature-contact
  # Contact section is back! 😌


STEP 4: MERGE FEATURE BRANCH INTO MAIN
───────────────────────────────────────
  git checkout main              # Switch to main (merge INTO this)
  git merge feature-contact      # 🌟 Merge!

  # Output: "Fast-forward" merge
  # Now main has ALL the changes from feature-contact!


STEP 5: CLEAN UP
─────────────────
  git branch -d feature-contact  # Delete merged branch
  git branch                     # Verify: only * main
  git push origin main           # Push updated main to GitHub


WHAT JUST HAPPENED:
  BEFORE MERGE:
  main:            A → B → C
                         ↘
  feature-contact:        D → E

  AFTER MERGE:
  main:            A → B → C → D → E  ✅
  feature-contact: (deleted)


================================================================================
⏱️  PART 6: COLLABORATION WITH PULL REQUESTS  (0:45 - 0:55)
================================================================================

🎯 SIMULATE A REAL TEAM WORKFLOW


STEP 1: CREATE ANOTHER BRANCH & PUSH TO GITHUB
───────────────────────────────────────────────
  git checkout -b feature-projects

  # Add to index.html:
      <h2>My Projects</h2>
      <ol>
          <li>Portfolio Website (this one!)</li>
          <li>Coming soon...</li>
      </ol>

  git add .
  git commit -m "Add projects section"

  # 🌟 Push this BRANCH to GitHub
  git push origin feature-projects


STEP 2: CREATE A PULL REQUEST ON GITHUB
────────────────────────────────────────
  🌐 Go to your GitHub repository
  📢 You should see: "feature-projects had recent pushes"
     → Click "Compare & pull request"
  📝 Fill in:
     Title: Add projects section
     Description: Added a new projects section to showcase my work
  🔍 Review the "Files changed" tab
  ✅ Click "Create Pull Request"


STEP 3: REVIEW AND MERGE THE PULL REQUEST
──────────────────────────────────────────
  🌐 On the Pull Request page:
  📋 Review the changes
  💬 Add comments (in real teams, teammates review here)
  ✅ Click "Merge pull request"
  ✅ Click "Confirm merge"
  🗑️ Click "Delete branch"


STEP 4: UPDATE YOUR LOCAL REPOSITORY
─────────────────────────────────────
  git checkout main
  git pull origin main
  git branch -d feature-projects
  # ✅ Everything is in sync!


PULL REQUEST WORKFLOW (How Real Teams Work):
  ┌──────────┐     ┌──────────┐     ┌───────────┐     ┌─────────┐
  │ Create   │     │ Push     │     │ Open Pull │     │ Review  │
  │ Branch   │────►│ Branch   │────►│ Request   │────►│ & Merge │
  │ Locally  │     │ to GitHub│     │ on GitHub │     │         │
  └──────────┘     └──────────┘     └───────────┘     └─────────┘


================================================================================
⏱️  PART 7: BONUS — .gitignore & CLONING  (Quick)
================================================================================

.gitignore — FILES GIT SHOULD IGNORE:
──────────────────────────────────────
  touch .gitignore

  # .gitignore content:
  .DS_Store
  Thumbs.db
  .vscode/
  .idea/
  node_modules/
  .env
  *.exe
  *.log

  git add .gitignore
  git commit -m "Add .gitignore"
  git push origin main


CLONING — DOWNLOAD SOMEONE ELSE'S REPO:
────────────────────────────────────────
  git clone https://github.com/ANY-USER/ANY-REPO.git

  # Example — clone your own repo on a new computer:
  git clone https://github.com/YOUR-USERNAME/my-portfolio.git
  cd my-portfolio
  git log --oneline


FORKING (GitHub Feature):
──────────────────────────
  🌐 Go to ANY public repository on GitHub
  🍴 Click "Fork" (top right)
  📋 Creates YOUR OWN COPY of the repo
  🔧 Clone your fork → make changes → submit Pull Request to original!


================================================================================
📝 COMPLETE CHEAT SHEET  (0:55 - 1:00)
================================================================================

🟢 SETUP
  git config --global user.name "Name"    # Set name
  git config --global user.email "email"  # Set email
  git init                                # Initialize repo
  git clone <url>                         # Clone repo

🔵 DAILY WORKFLOW
  git status                  # Check status (USE THIS OFTEN!)
  git add <file>              # Stage specific file
  git add .                   # Stage all changes
  git commit -m "message"     # Commit with message
  git push origin main        # Push to GitHub
  git pull origin main        # Pull from GitHub

🟡 BRANCHING
  git branch                  # List branches
  git branch <name>           # Create branch
  git checkout <name>         # Switch branch
  git checkout -b <name>      # Create + switch (shortcut)
  git merge <name>            # Merge branch into current
  git branch -d <name>        # Delete branch

🟠 INSPECTION
  git log                     # View commit history
  git log --oneline           # Compact history
  git diff                    # See unstaged changes
  git blame <file>            # See who changed each line

🔴 UNDO
  git restore <file>          # Discard working changes
  git restore --staged <file> # Unstage
  git revert <commit>         # Undo a commit (safe)
  git reset --hard <commit>   # Go back in time (⚠️ destructive)


================================================================================
🎯 HOMEWORK / PRACTICE CHALLENGES
================================================================================

  Challenge 1 (Solo):
    ✅ Create a new repo called "learning-git"
    ✅ Add 3 different files with 3 separate commits
    ✅ Push to GitHub
    ✅ Create a branch, make changes, merge it

  Challenge 2 (Collaboration):
    ✅ Fork a classmate's repository
    ✅ Clone your fork
    ✅ Create a branch, make improvements
    ✅ Push and open a Pull Request

  Challenge 3 (Build Something):
    ✅ Create a "recipes" repo with your favorite recipes
    ✅ Each recipe = 1 branch → merge when done
    ✅ Use proper commit messages
    ✅ Add a README with a table of contents


================================================================================
📚 RESOURCES TO CONTINUE LEARNING
================================================================================

  🎮 Interactive:
     - https://learngitbranching.js.org   (HIGHLY RECOMMENDED!)
     - https://github.com/skills          (GitHub's official courses)

  📖 Documentation:
     - https://git-scm.com/doc
     - https://docs.github.com

  🎥 Visual Tools:
     - GitHub Desktop (GUI for beginners)
     - GitLens (VS Code extension)


================================================================================
🏗️  THE COMPLETE WORKFLOW (Everything Together)
================================================================================

  ┌──────────────── ONE-TIME SETUP ────────────────┐
  │ git config → GitHub Account → SSH/Token Setup  │
  └────────────────────────────────────────────────┘
                         │
                         ▼
  ┌──────────────── START PROJECT ─────────────────┐
  │ git init (new)  OR  git clone (existing)       │
  └────────────────────────────────────────────────┘
                         │
                         ▼
           ┌──── DAILY WORKFLOW (LOOP) ────┐
           │                                │
           │  1. git checkout -b feature-x  │
           │  2. Write code / Make changes  │
           │  3. git add .                  │
           │  4. git commit -m "desc"       │
           │  5. git push origin feature-x  │
           │  6. Open Pull Request          │
           │  7. Review → Merge             │
           │  8. git checkout main          │
           │  9. git pull origin main       │
           │  10. Repeat!                   │
           │                                │
           └────────────────────────────────┘


================================================================================
✨ KEY TAKEAWAYS
================================================================================

  1️⃣  git add .              → Stage your changes
  2️⃣  git commit -m "msg"    → Save a snapshot
  3️⃣  git push               → Upload to GitHub
  4️⃣  git pull               → Download from GitHub
  5️⃣  git checkout -b name   → Create a branch
  6️⃣  Always use branches for new features!
  7️⃣  Write meaningful commit messages!
  8️⃣  git status is your best friend — use it constantly!

================================================================================
  🎉 Congratulations! You now know enough Git & GitHub to work on real
     projects and collaborate with other developers!
================================================================================