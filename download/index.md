
<!--
.. title: Download
.. slug: download
.. description: download the UAAccess application for Mac and Windows. Installer and portable versions available.
.. type: text
-->

This page contains the most recent binary releases of UAAccess for MacOS and Windows.

If you would like to contribute or simply see how the code works, this is an open-source project, feel free to do so by clicking on the sourcecode link in the navigation above. It can also be found under the "app" folder in the portable release or where ever your app is installed. Happy hacking!

# Latest release

## Release v0.0.3 ()
Published on 2025-03-29T03:29:22Z

### New in this version

- cysimdjson was causing an issue on ARM64 versions of MacOS, so we pulled it out on MacOS temporarily in favor of the JSON module from the standard library. Please open an issue or let us know if you face performance bottlenecks.
- All outputs are now shown in the outputs tab, not just the current one.
- Fixes a memory leak and improperly disabled controls in the updater.
- On Windows, the updater now reads the MSI installer database instead of enumerating through installed applications.
- Note that the auto-updater is not working properly in a few limited circumstances and the cause has been especially difficult to track down. We aim to fix this soon, but would like to focus on core functionality (the things that really matter) while the app is still in alpha. For now it is probably best to manually download and install newly released builds.
-Other speed and reliability improvements. Seriously.


<table><caption>Downloads for Release v0.0.3</caption>
<thead><tr>
<th scope="col">File Name</th>
<th scope="col">Size</th>
<th scope="col">Download Count</th>
</tr></thead>
<tbody>
<tr>
<td><a href="https://github.com/uaaccess/uaaccess/releases/download/v0.0.3/UAAccess-0.0.3.dmg">UAAccess-0.0.3.dmg</a></td>
<td>53.3MB</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://github.com/uaaccess/uaaccess/releases/download/v0.0.3/UAAccess-0.0.3.msi">UAAccess-0.0.3.msi</a></td>
<td>42.3MB</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://github.com/uaaccess/uaaccess/releases/download/v0.0.3/UAAccess-0.0.3.pkg">UAAccess-0.0.3.pkg</a></td>
<td>58.7MB</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://github.com/uaaccess/uaaccess/releases/download/v0.0.3/UAAccess-0.0.3.zip">UAAccess-0.0.3.zip</a></td>
<td>42.6MB</td>
<td>0</td>
</tr>
</tbody></table>

