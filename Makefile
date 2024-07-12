test: downloadlinks
	hugo server -w --logLevel info --bind 0.0.0.0
release: downloadlinks
	hugo
deploy: release
	rsync --chown www-data:www-data -avz --delete --exclude 'forum/' --exclude 'codedoc/' docs/ pioneer:/var/www/pioneerspacesim.net/
downloadlinks:
	python3 make-downloadlinks.py > layouts/partials/generated/downloadlinks.html

# Unused
changelog:
	python3 make-changelog.py > layouts/partials/generated/changelog.html
releasejs:
	python3 make-release-js.py > layouts/partials/generated/releases.html
