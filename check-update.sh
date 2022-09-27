#!/bin/sh
curl https://git.kraxel.org/cgit/libpcd/ 2>/dev/null |grep h=libpcd- |head -n1 |sed -e "s,.*h=libpcd-,,;s,-.*,,;s,'.*,,"
