# school_web_app
This is a simple school management app that uses django to do most of the work of managing teacher record,student record and performances.
### Features:
- Teachers record
- Students Performance
- Addstudent.
- Deletestudent,
- Update student profile.
- Markentry ,blog ,creativity modules.

### Follow this image for better understanding :

### Prerequisites
What things you need to install the software and how to install them

### Installing
A step by step series of examples that tell you how to get a development env running

### Install Python
#### Linux Users
It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:
```
$ python3 --version
Python 3.6.1
```
#### Windows Users
You can download Python for Windows from the website https://www.python.org/downloads/windows/. Click on the "Latest Python 3 Release - Python x.x.x" link. If your computer is running a 64-bit version of Windows, download the Windows x86-64 executable installer. Otherwise, download the Windows x86 executable installer. After downloading the installer, you should run it (double-click on it) and follow the instructions there.

One thing to watch out for: During the installation, you will notice a window marked "Setup". Make sure you tick the "Add Python 3.6 to PATH" or 'Add Python to your environment variables" checkbox and click on "Install Now". And repeat When the installation completes, you may see a dialog box with a link you can follow to learn more about Python or about the version you installed. Close or cancel that dialog -- you'll be learning more in this tutorial!

### Virtual environment
All you need to do is find a directory in which you want to create the virtualenv; your home directory, for example. On Windows, it might look like C:\Users\Name\ (where Name is the name of your login).

We will make a virtualenv called myvenv. The general command will be in the format:
```
$ python3 -m venv myvenv
```
#### Working with virtualenv
The command above will create a directory called myvenv (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files).

#### Working with virtualenv: Windows
Start your virtual environment by running:
```
C:\Users\Name\Susheelgupta> myvenv\Scripts\activate
```
#### Working with virtualenv: Linux and OS X
Start your virtual environment by running:
```
$ source myvenv/bin/activate
```
### Installing Django
Now that you have your virtualenv started, you can install Django.

Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:
```
(myvenv) ~$ python -m pip install --upgrade pip
```
Now, run
```
pip install -r requirements.txt
```
to install Django.

```
(myvenv) ~$ pip install -r requirements.txt
```
