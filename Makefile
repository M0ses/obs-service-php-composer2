SERVICES_DIR = $(DESTDIR)/usr/lib/obs/service/

install:
	install -m 755 php-composer2 $(SERVICES_DIR)/php-composer2
	install -m 644 php-composer2.service $(SERVICES_DIR)/php-composer2.service
