Repository: donnemartin/system-design-primer
Language: Python
Stars: 306777
Forks: 50696
-----
After a write, reads may or may not see it.  A best effort approach is taken.  
This approach is seen in systems such as memcached.  Weak consistency works well in real time use cases such as VoIP, video chat, and realtime multiplayer games.  For example, if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.