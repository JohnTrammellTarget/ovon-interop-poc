

.PHONY: install restart log logs dump

do:
	make install restart

install: kamailio.cfg kemi.py
	sudo install kamailio.cfg kemi.py /etc/kamailio

restart:
	sudo systemctl restart kamailio

log logs:
	sudo journalctl -u kamailio -b

dump:
	sudo /usr/sbin/kamcmd ul.dump

