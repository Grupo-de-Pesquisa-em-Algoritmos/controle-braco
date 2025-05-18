install:
	mkdir /opt/hand-control
	cp -r * /opt/hand-control
	cp hand-control.service /etc/systemd/user/

uninstall:
	rm -rf /opt/hand-control
	rm /etc/systemd/user/hand-control.service
