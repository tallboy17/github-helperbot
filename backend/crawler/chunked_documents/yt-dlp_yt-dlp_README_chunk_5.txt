Repository: yt-dlp/yt-dlp
Language: Python
Stars: 115712
Forks: 9143
-----
File|Description
:---|:---
[yt-dlp.tar.gz](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.tar.gz)|Source tarball
[SHA2-512SUMS](https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-512SUMS)|GNU-style SHA512 sums
[SHA2-512SUMS.sig](https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-512SUMS.sig)|GPG signature file for SHA512 sums
[SHA2-256SUMS](https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-256SUMS)|GNU-style SHA256 sums
[SHA2-256SUMS.sig](https://github.com/yt-dlp/yt-dlp/releases/latest/download/SHA2-256SUMS.sig)|GPG signature file for SHA256 sums  
The public key that can be used to verify the GPG signatures is [available here](https://github.com/yt-dlp/yt-dlp/blob/master/public.key)
Example usage:
```
curl -L https://github.com/yt-dlp/yt-dlp/raw/master/public.key | gpg --import
gpg --verify SHA2-256SUMS.sig SHA2-256SUMS
gpg --verify SHA2-512SUMS.sig SHA2-512SUMS
```
<!-- MANPAGE: END EXCLUDED SECTION -->  
**Note**: The manpages, shell completion (autocomplete) files etc. are available inside the [source tarball](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.tar.gz)