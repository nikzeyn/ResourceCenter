# ############## #
# ResourceCenter #
# ############## #


# CONTENT
	ABOUT
	ARCHITECTURE


# ABOUT

	ResourceCentre is a web application that can be used to access and book internal resources.


# ARCHITECTURE

	Host OS: Linux Centos 8
	Language: Python 3.6
	Framework: Django 3.0.8
	Database: Postgres 10.6
	Http Server: gunicorn 20.0.4
	Proxy server: ngnix
	Container deatils:
		docker swarm stack of services:
			webapp:
				image: centos8 + django3 + gunicorn20
			db:
				image: centos8 + postgres10
			webserver:
				image: centos8 + nginx





