Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
* `api_hostname`: Hostname to use for mobile API calls, e.g. `api22-normal-c-alisg.tiktokv.com`
* `app_name`: Default app name to use with mobile API calls, e.g. `trill`
* `app_version`: Default app version to use with mobile API calls - should be set along with `manifest_app_version`, e.g. `34.1.2`
* `manifest_app_version`: Default numeric app version to use with mobile API calls, e.g. `2023401020`
* `aid`: Default app ID to use with mobile API calls, e.g. `1180`
* `app_info`: Enable mobile API extraction with one or more app info strings in the format of `<iid>/[app_name]/[app_version]/[manifest_app_version]/[aid]`, where `iid` is the unique app install ID. `iid` is the only required value; all other values and their `/` separators can be omitted, e.g. `tiktok:app_info=1234567890123456789` or `tiktok:app_info=123,456/trill///1180,789//34.0.1/340001`
* `device_id`: Enable mobile API extraction with a genuine device ID to be used with mobile API calls. Default is a random 19-digit string