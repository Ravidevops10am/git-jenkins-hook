from fabric.operations import local
from fabric.api import task

# post receive git-jenkins hook
# This is invoked after every remote push by the user
# This hook invoke jenkins build
@task
def postreceive():
	local('curl <http://<jenkins_server>/git/notifyCommit?url=</path/project.git>')
	return