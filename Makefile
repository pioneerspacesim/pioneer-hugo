test: downloadlinks changelog releasejs
	hugo server -w -v --bind 0.0.0.0
release: downloadlinks changelog releasejs
	hugo
deploy: release
	rsync --chown www-data:www-data -avz --delete --exclude 'forum/' --exclude 'codedocs/' docs/ pioneer:/var/www/pioneerspacesim.net/
downloadlinks:
	python make-downloadlinks.py > themes/pioneer/layouts/shortcodes/downloadlinks.html
changelog:
	python make-changelog.py > themes/pioneer/layouts/shortcodes/changelog.html
releasejs:
	python make-release-js.py > themes/pioneer/layouts/partials/releases.html
