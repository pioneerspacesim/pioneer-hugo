test: downloadlinks changelog releasejs
	hugo server -w -v --bind 0.0.0.0
release: downloadlinks changelog releasejs
	hugo
deploy: release
	rsync --chown www-data:www-data -avz --delete --exclude 'forum/' --exclude 'codedoc/' docs/ pioneer:/var/www/pioneerspacesim.net/
downloadlinks:
	python3 make-downloadlinks.py > themes/pioneer/layouts/shortcodes/downloadlinks.html
changelog:
	python3 make-changelog.py > themes/pioneer/layouts/shortcodes/changelog.html
releasejs:
	python3 make-release-js.py > themes/pioneer/layouts/partials/releases.html
