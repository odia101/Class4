# Class4
Learning Docker

INSTRUCTIONS:
A. BUILDING
	$ docker build -t myimage .
	REPOSITORY	TAG	IMAGE ID	CREATED		SIZE
	myimage		latest	f9bf9770ddad	5 minutes ago	426MB

B. SHOWING THAT IT EXISTS
	$ docker image ls
	
C. RUNNING
	$ docker run -ti myimage


CONTONOUS INTEGRATION (CI)
	This is a process or system by which developers keep track of their coding projects. It helps maintain a 
single source repository, makes the build self-testing, and makes it easy for collaborators to see what is 
happening, and get the latest executed change.
 
	The process involves the developers checking out their codes in a private workspace. 
CI server monitors changes commited to the repository, checks changes and alerts everyone of test failures and success.
This helps the team fix problems at the earliest opportunity.

	One common tool that can be used as a Continous Integration tool with Github is Jenkins. 
	
 

