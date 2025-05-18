install:
	mkdir /opt/controle-braco
	cp -r * /opt/controle-braco
	cp hand-control.service /etc/systemd/user/

uninstall:
	rm -rf /opt/controle-braco
	rm /etc/systemd/user/hand-control.service
