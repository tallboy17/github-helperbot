Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
- [Do not log](https://sobolevn.me/2020/03/do-not-log) dwells on some logging antipatterns.
- Logging does not make much sense in monitoring and error tracking. Use better tools instead: error and business monitorings with alerts, versioning, event sourcing.
- Logging adds significant complexity to your architecture. And it requires more testing. Use architecture patterns that will make logging an explicit part of your contracts
- Logging is a whole infrastructure subsystem on its own. And quite a complex one. You will have to maintain it or to outsource this job to existing logging services
- [Lies My Parents Told Me (About Logs)](https://www.honeycomb.io/blog/lies-my-parents-told-me-about-logs/)
- Logs are cheap
- I can run it better myself
- Leveled logging is a great way to separate information
- Logs are basically the same as events
- A standard logging format is good enough
- [Logging - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [The Audit Log Wall of Shame](https://audit-logs.tax/): list of vendors that don’t prioritize high-quality, widely-available audit logs for security and operations teams.
- [Guide on Structured Logs](https://signoz.io/blog/structured-logs/)