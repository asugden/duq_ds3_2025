# duq_ds3_2025

## Setting up VSCode (Microsoft Visual Studio Code) for your whole computer for the first time

The first rule of VSCode: _only open the folder of the project_, not a folder including multiple projects. You want to open the outermost folder of a single project, which should contain git information for your project (a hidden .git directory).

I organize my directories as follows:

```
programming
└─── duq_ds3_2025
│   │    .gitignore
│   │    README.md
│   └─── .vscode
│       │    launch.json
│       │    settings.json
│
│   └─── duq_ds3_2025
│       │    __init__.py
│       │    some_class.py
│
│   └─── scripts
│       │    some_script.py
│
└─── duq_ds3_2023
│   │    .gitignore
│   │    README.md
```

In VSCode, do NOT open `programming`. Instead, you should have a separate window for `duq_ds3_2025` and any other project, such as `duq_ds3_2024`.

The new hip alternative to `pip` is called `poetry`. I would install it now, using

```
curl -sSL https://install.python-poetry.org | python3 -
```

see https://python-poetry.org/docs/#installing-with-the-official-installer for Windows installation.

I am a strong propoennt of having virual environments within the project. Therefore, I also change the configuration:

```
poetry config virtualenvs.in-project true
```

## Setting up a git project (once)

The easiest way is to first set up the project in `git` and then clone it to your computer.

1. In github, create a new repository and name it
1. Once, you will have to add your SSH keys
1. Click on the green button called "Code", select "SSH", and copy the resulting code.
1. Clone the repository to your computer. I'm going to navigate to the right place in the terminal first and then clone. This will create a new folder in programming with the name `duq_ds3_2025` in which the project will live.

```
cd /Users/arthur/programming
git clone git@github.com:asugden/duq_ds3_2025.git duq_ds3_2025/
```

5. Now you're ready to open it in vscode.

## Setup VSCode for project (once)

In VSCode, open the directory for ONLY A SINGLE PROJECT. I cannot stress this enough. Anything else will cause problems with git and environments.

1. Create a `.vscode` directory and copy in the `launch.json` and `settings.json` files included here.
1. Copy in the `.gitignore` file to ensure random junk is not uploaded to git. This is important. If you make a mistake and accidentally push your `.venv` directory, it's a massive pain and can make a repo worse for the future.
1. Open the VSCode terminal (you can create a New Terminal in the top menu or just click the circle with an X button at the bottom). Type `poetry init`. This will create a new virtual environment and will ask you a few questions. You don't need to add requirements interactively. This will create a file called `pyproject.toml`. This is a very important file that describes all of the dependencies of your project, and it should go to github.
1. You can add new packages with `poetry add pandas` for example. And run `poetry install` to make sure everything is up to date. You will see a new file called `poetry.lock`, which is also very important and should go to github. It ensures that you can perfectly reproduce all of the packages and package versions on a different computer.
1. Change the path in `settings.json` to match your computer. You can keep everything from `.venv/bin/activate` but you will have to change the first part of the line to be the location of the directory on your computer.
1. As you go, you can continue to add packages with `poetry add` and `poetry install`.

## Other packages

NOTE: Installing fasttext on python 3.12 or higher requires a workaround:

```
poetry add git+https://github.com/cfculhane/fastText
```
