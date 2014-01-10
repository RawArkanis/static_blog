How to sync Sublime Text 3 packages and configurations between Windows and Linux using Dropbox
##############################################################################################

:date: 2014-01-10 13:30
:modified: 2014-01-10 13:30
:tags: sync, sublime, package, dropbox
:category: sublime,
:slug: sync-sublime-text-3-with-dropbox
:author: Luiz F. A. de Prá
:summary: If there is something I like to do but makes me lose a lot of time that would be configuring tools. And when you need to do the same configuration in two or more machines? Yes, a lot of time wasted.

If there is something I like to do but makes me lose a lot of time that would be configuring tools. And when you need to do the same configuration in two or more machines? Yes, a lot of time wasted.

I use Sublime Text 3 at work and home, I need the same set of plugins and configuration in both. To accomplish that I created two scripts to configure ST3 to use packages and configuration files stored in Dropbox. I based my script on `Misfocus's Post <http://misfoc.us/post/18018400006/syncing-sublime-text-2-settings-via-dropbox>`_
.

Let's get it started.

Configuring Dropbox
===================

I'm not teaching how to create an account for dropbox nor how to install and configure the software. You can easily find how to do it googling.

First, we need to create a folder to hold our files inside Dropbox folder. I created a structure like ``AppData/SublimeText3``, but it is up to you to decide how the folder structure will be.

Now, we copy two folders from SB3, Installed Packages and Packages, to the recently created folder inside Dropbox folder. On Windows those folders are probably in ``C:\Users\<YourUserHere>\AppData\Roaming\Sublime Text 3``, and on Linux at ``/home/<YourUserHere>/.config/sublime-text-3``. Remeber to make always make a backup.

Windows
=======

*Tested with SB3 Build 3059 on Windows 8.1. Probably work fine with older version or maybe need some minor changes.*

Create a batch file anywhere. You can use any name, but I'm assuming that you picked ``install.bat``.
Copy and past this code inside:

.. code-block:: guess
	:linenos: table

    @echo off
 
	:: Change those two varaibles
	set DROPBOX_PATH=C:\Users\<YourUserHere>\Dropbox\AppData\SublimeText3
	set SUBLIME_PATH=C:\Users\<YourUserHere>\AppData\Roaming\Sublime Text 3
	 
	:: Remove default folders if exists
	if exist "%SUBLIME_PATH%\Installed Packages" (goto remove_ipkg) else (goto check_pkg)
	 
	:remove_ipkg
	echo Removing "%SUBLIME_PATH%\Installed Packages"
	rmdir /s /q "%SUBLIME_PATH%\Installed Packages"
	 
	:check_pkg
	if exist "%SUBLIME_PATH%\Packages" (goto remove_pkg) else (goto install)
	 
	:remove_pkg
	echo Removing "%SUBLIME_PATH%\Packages"
	rmdir /s /q "%SUBLIME_PATH%\Packages"
	 
	:: Install links
	:install
	mklink /D "%SUBLIME_PATH%\Installed Packages" "%DROPBOX_PATH%\Installed Packages"
	mklink /D "%SUBLIME_PATH%\Packages" "%DROPBOX_PATH%\Packages"
	 
	echo Done!

Remember to edit both two path variables accordingly with your system path.

This script will remove ``Installed Packages`` and ``Packages`` from SB3 folder and create symbolic links to the folders from Dropbox.

To run just open CMD (pressing Windows Key + R and typing cmd), navigate to the location where the script is placed and type ``install.bat``. Done!

Linux
=====

*Tested with SB3 Build 3059 on Fedora 20. Probably work fine in another linux distros.*

Same process, create a ``install.sh`` and copy and paste the following code inside:

.. code-block:: bash

    #!/bin/sh
	# Change those two varaibles
	DROPBOX_PATH=/home/<YourUserHere>/Dropbox/AppData/SublimeText3
	SUBLIME_PATH=/home/<YourUserHere>/.config/sublime-text-3
	 
	# Remove default folders if exists
	if [ -d "$SUBLIME_PATH/Installed Packages" ]; then
	  echo "Removing $SUBLIME_PATH/Installed Packages"
	  rm -rf "$SUBLIME_PATH/Installed Packages"
	fi
	 
	if [ -d "$SUBLIME_PATH/Packages" ]; then
	  echo "Removing $SUBLIME_PATH/Packages"
	  rm -rf "$SUBLIME_PATH/Packages"
	fi
	 
	# Install links
	ln -s "$DROPBOX_PATH/Installed Packages" "$SUBLIME_PATH/Installed Packages"
	ln -s "$DROPBOX_PATH/Packages" "$SUBLIME_PATH/Packages"
	 
	echo "Done!"

Again, edit both path variables.

To run open a terminal and navigate to the folder where the file is, give execution permission with ``chmod +x install.sh``, and finally type ``./install.sh``. Done!

What to do now?
===============

Now you can do this process in more than two machines if you please.

I didn't write an OS X version of the scripts because I don't use an Apple Computer, but you can do it just changing the paths from linux script (I think!?).
And if you want to sync another files it is easy to add it to the scripts. 

All done, have fun coding.
