# Teaching Resources for Students

Welcome! 👋

This repository contains class examples, practice activities, starter files, and completed projects. You can look through the files on GitHub, download the whole repository, or clone it to your computer.

## Finding your class files

The folders are generally organized like this:

```text
day → class code → lesson or project
```

For example:

```text
Wednesday → L4_P → Python Battleship → main.py
```

1. Open the folder for the day your class meets.
2. Open your class or group folder.
3. Open the lesson or project named by your instructor.

Lesson folders may contain:

- `main.py`, `warmup.py`, or other Python files
- `index.html`, `style.css`, and `script.js` for web projects
- images, data files, databases, or notes used by a project
- starter code, examples, or completed versions

Keep all files from a project folder together. Moving or renaming one file can sometimes stop the project from finding its images, stylesheets, scripts, or data.

## Option 1: View or download files from GitHub

You can read most files by clicking through the folders on the [repository page](https://github.com/BrewStJohn/Teaching-For-Student-Access).

To download everything without installing Git:

1. Open the repository page.
2. Select the green **Code** button.
3. Select **Download ZIP**.
4. Find the downloaded ZIP file, usually in your `Downloads` folder.
5. Extract it:
   - **Windows:** Right-click the ZIP file and choose **Extract All**.
   - **macOS:** Double-click the ZIP file.
6. Open the extracted `Teaching-For-Student-Access` folder.

The ZIP download is a snapshot. It will not update automatically when new class files are added.

## Option 2: Clone with GitHub Desktop

[GitHub Desktop](https://desktop.github.com/) is a visual way to clone and update the repository.

1. Install and open GitHub Desktop.
2. Select **File → Clone repository**.
3. Select the **URL** tab.
4. Enter:

   ```text
   https://github.com/BrewStJohn/Teaching-For-Student-Access.git
   ```

5. Choose where the repository should be saved.
6. Select **Clone**.
7. Use **Show in Explorer**, **Show in Finder**, or **Open in Visual Studio Code** to find the files.

To get new files later, open the repository in GitHub Desktop and select **Fetch origin**, followed by **Pull origin** if an update is available.

## Option 3: Clone from the terminal

### Before you begin

Install [Git](https://git-scm.com/downloads) if it is not already installed.

### Clone the repository

Open a terminal in the folder where you want to keep your class materials, then run:

```bash
git clone https://github.com/BrewStJohn/Teaching-For-Student-Access.git
cd Teaching-For-Student-Access
```

If you use Visual Studio Code, you can then run:

```bash
code .
```

If the `code` command is unavailable, open Visual Studio Code and select **File → Open Folder**, then choose the `Teaching-For-Student-Access` folder.

### Get the latest class files

The next time you need updates, open a terminal inside the repository folder and run:

```bash
git pull
```

If Git reports a conflict because you changed one of the class files, save your work somewhere else before asking your instructor for help.

## Protect your own work

The safest approach is to leave the downloaded or cloned class materials unchanged and work from a copy.

For example:

```text
Documents/
├── Teaching-For-Student-Access/   ← class materials
└── My-Class-Work/                 ← your copies and assignments
```

When beginning an activity:

1. Find the lesson or project folder.
2. Copy the entire folder into `My-Class-Work`.
3. Rename your copy clearly, such as `battleship-dylan` or `2026-06-19-battleship`.
4. Make changes only inside your copy.

This keeps `git pull` simpler and gives you a clean original to return to if something breaks.

## File-management habits that help

- Create one main folder for the course.
- Keep each project in its own folder.
- Use clear names instead of names such as `new`, `final`, or `final-final`.
- Include a date when it helps: `2026-06-19-python-practice`.
- Do not remove file extensions such as `.py`, `.html`, `.css`, `.js`, or `.csv`.
- Save frequently and make backup copies of important work.
- Avoid editing files while they are still inside a ZIP archive—extract the archive first.
- In Visual Studio Code, open the whole project folder rather than opening only one file.

## Helpful resources

- [Cloning a repository — GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [Downloading source-code archives — GitHub Docs](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)
- [Getting started with Git — GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git)
- [GitHub Desktop documentation](https://docs.github.com/en/desktop)
- [Visual Studio Code: Basic editing](https://code.visualstudio.com/docs/editing/codebasics)
- [Find and open File Explorer in Windows](https://support.microsoft.com/en-us/windows/find-and-open-file-explorer-ef370130-1cca-9dc5-e0df-2f7416fe1cb1)
- [Organize files in folders on Mac](https://support.apple.com/guide/mac-help/organize-files-in-folders-mh26885/mac)

## Need help?

Ask if:

- you do not know which day or class folder to use;
- a required file appears to be missing;
- `git clone` or `git pull` shows an error;
- a project cannot find an image, stylesheet, script, database, or data file; or
- you accidentally changed or deleted an original class file.

When asking for help, include the folder you opened and the complete error message. A screenshot can also be useful.

Happy coding! 🚀
