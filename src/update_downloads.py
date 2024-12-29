"""
update_downloads.py

Automatically consult the GitHub releases page and upload the downloads section of the site accordingly.
For now, this script needs to be run each and every time the application is updated, prior to `nikola github_deploy`.

if you are wanting to change the text that shows up on the downloads page, update the content of DOWNLOAD_TEMPLATE below.
"""


DOWNLOAD_FILE_TEMPLATE = """
<!--
.. title: Download
.. slug: download
.. description: download the UAAccess application for Mac and Windows. Installer and portable versions available.
.. type: text
-->

This page contains the most recent binary releases of UAAccess for MacOS and Windows.

If you would like to contribute or simply see how the code works, this is an open-source project, feel free to do so by clicking on the sourcecode link in the navigation above. It can also be found under the "app" folder in the portable release or whereever your app is installed. Happy hacking!

"""

import sys
import os
try:
	from nikola.utils import get_root_dir
except ModuleNotFoundError:
	print("Unable to import Nikola. Please ensure this script is ran using the python installation that has the Nikola module installed.\nIf you keep getting this error, try typing \"where nikola\" and using that binary.")
	sys.exit(1)
import requests


releases_url = "https://api.github.com/repos/uaaccess/uaaccess/releases"
releases_json = {}
 

def bytes2human(n):
	"""
	Given a number like 4096, returns a human readable representation like "4 MB"

	taken and partially modified from http://code.activestate.com/recipes/578019
	"""
	symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	prefix = {}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if n >= prefix[s]:
			value = float(n) / prefix[s]
			return '%.1f%s' % (value, s)
	return "%sB" % n


def get_releases_json():
	global releases_json
	request = requests.get(releases_url)
	request.raise_for_status()
	releases_json = request.json()


def format_release(json):
	text = f"""
## {json["name"]} ({"beta" if json["prerelease"] else ""})
Published on {json["published_at"]}

{json["body"]}

"""
	assets = json["assets"]
	if len(assets) == 0:
		text += "No assets available"
	else:
		text += f"""<table><caption>Downloads for {json['name']}</caption>
<thead><tr>
<th scope="col">File Name</th>
<th scope="col">Size</th>
<th scope="col">Download Count</th>
</tr></thead>
<tbody>
"""
		for asset in assets:
			text += f"""<tr>
<td><a href="{asset['browser_download_url']}">{asset['name']}</a></td>
<td>{bytes2human(asset['size'])}</td>
<td>{asset['download_count']}</td>
</tr>
"""
		text += "</tbody></table>\n"
		return text

def build_releases_html():
	if len(releases_json) == 0:
		print("No releases found. Please ensure that at least one has been created.")
		sys.exit(1)
	output = ""
	for i, json in enumerate(releases_json):
		if i == 0:  # GitHub releases are ordered
			output += "# Latest release\n"
			output += format_release(json)+"\n"
		elif i == 1:
			output += "# Past releases"
			output += format_release(json)+"\n"
		else:
			output += format_release(json)+"\n"
		return output


def main():
	root = get_root_dir()
	if not root:
		print("Cannot find your site's root directory. Please ensure this script is run in the top-level of the Nikola site, then try again.")
		sys.exit(1)
	downloads_file = os.path.join(root, "pages", "download.md")
	get_releases_json()
	releases_html = build_releases_html()
	with open(downloads_file, "w") as f:
		f.write(DOWNLOAD_FILE_TEMPLATE + releases_html)
	print(f"Writing to {downloads_file} complete. Please build the site, and if everything looks good, continue with the deployment.")


if __name__ == "__main__":
	main()
