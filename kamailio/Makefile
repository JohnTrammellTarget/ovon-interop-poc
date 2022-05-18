

.PHONY: install restart log logs dump


install: kamailio.cfg
	sudo install kamailio.cfg /etc/kamailio

restart:
	sudo systemctl restart kamailio

log logs:
	sudo journalctl -u kamailio -b

dump:
	sudo /usr/sbin/kamcmd ul.dump

