# auto-commit-message
Auto commit message

## Overview

Generate a short commit message from the result of `git status --short`.

<details><summary>Example</summary>

```bash
$ git status --short
A  test1
A  test2
?? test3
$ auto_commit_message
Create test1, test2
```

```bash
$ git status --short
M  README.md
A  test1
A  test2
?? test3
$ auto_commit_message
Update README.md & Create test1, test2
```

```bash
$ git status --short
R  Makefile -> Makefile2
M  README.md
A  test1
A  test2
?? test3
$ auto_commit_message
Update README.md & Create test1, test2 & Rename Makefile -> Makefile2
```

```bash
$ git status --short
R  Makefile -> Makefile2
M  README.md
D  setup.cfg
A  test1
A  test2
?? test3
$ auto_commit_message
Update README.md & Create test1, test2 & Delete setup.cfg & Rename Makefile -> Makefile2
```

</details>

## Getting Started

### Build Locally

#### Setup

```bash
pipenv shell
```

```bash
pipenv sync --dev
```

#### Build

```bash
make build
```

#### Run

```bash
./dist/auto_commit_message
```

```bash
python auto_commit_message.py
```

### Download Binary from Releases

#### Setup

```bash
cd /path/to/your-directory
```

```bash
curl -L -o auto_commit_message https://github.com/wasabina67/auto-commit-message/releases/latest/download/auto_commit_message && \
chmod +x auto_commit_message
```

#### Run

```bash
./auto_commit_message
```
