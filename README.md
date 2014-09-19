git-jenkins-hook
================

Script for git post receive hook with Jenkins build job using Fabric (a Python library), Jenkins

This project invokes a remote Jenkins build over http after a code push.

#Uses following:

* [Fabric 1.9.0](http://docs.fabfile.org/en/1.9/)
* Paramiko 1.14.0
* Python 2.6.6


#Instructions enable the git-jenkins hook

* Add the following line to /path/to/git/hooks/post-receive
** fab -f /path/to/githooks/postpushhook.py postreceive

#Refer the [wiki page on How to Set-up Jenkins for continuous integration](https://github.com/sidnan/python-fabric-deployment-automation/wiki/Setup-for-Git-Jenkins-build-hook)

