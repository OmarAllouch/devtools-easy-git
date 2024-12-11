# 📘 **Tutorial for Using the Easy Git CLI Tool**

This tutorial will walk you through how to **download the tool**, **run it locally**, and **configure shell aliases** to make your development experience smoother.

---

## 🚀 **1️⃣ Install the Tool from PyPI**

To get started with the **Git CLI Tool**, you can install it directly from **PyPI** (Python Package Index).

### **Installation Steps**

1. **Install the tool via pip**:
   ```bash
   pip install easy-git
   ```

2. **Verify the installation** to ensure the tool was installed successfully:
   ```bash
   easy-git --help
   ```
   If everything is set up correctly, you should see the CLI help menu.

3. **Try the `quick-commit` command**:
   ```bash
   easy-git quick-commit
   ```
   This command will list all files with changes, allow you to select which files to stage, and commit them with a message.

> **Note**: You can uninstall the tool at any time with the following command:
```bash
pip uninstall easy-git
```

---

## ⚙️ **2️⃣ Add Shell Aliases**

To make it easier to use **easy-git**, you can create aliases for its commands. This way, you can replace standard **git** commands with **easy-git** versions.

### **Why Use Aliases?**
- **Faster commands**: Replace `git commit` with `easy-git quick-commit`.
- **Shorter syntax**: Instead of typing the full command, you can simply run `git commit` as usual.

---

### **Step-by-step Guide**

1. **Open your shell configuration file** (depends on your shell):
   ```bash
   nano ~/.zshrc  # for zsh
   nano ~/.bashrc  # for bash
   ```

2. **Add the following aliases** at the end of the file:
   ```bash
   alias git='easy-git'
   alias git-commit='easy-git quick-commit'
   alias git-sync='easy-git sync'
   ```

> **What do these aliases do?**
- **git**: Changes all git commands to use **easy-git**.
- **git-commit**: Runs `easy-git quick-commit` instead of `git commit`.
- **git-sync**: Syncs your branch with the remote.

3. **Apply the changes** to your shell configuration:
   ```bash
   source ~/.zshrc  # for zsh
   source ~/.bashrc  # for bash
   ```

4. **Test the aliases** to make sure they work:
   ```bash
   git commit  # This will run easy-git quick-commit
   git sync  # This will run easy-git sync
   ```

> **Note**: If you want to customize the aliases, feel free to change the commands according to your workflow.

---

## 🎉 **You're All Set!**
You’ve successfully installed the tool, configured shell aliases, and run some commands.

To get help for any command, you can run:
```bash
easy-git --help
```

If you have any issues, feel free to **open an issue** or **reach out to the maintainers**.

