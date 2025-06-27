Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
Also see this section on my [list of management resources, "Incident response"](https://github.com/charlax/engineering-management/).  
Also see the Debugging section in this doc.  
- [Incident Response at Heroku](https://blog.heroku.com/archives/2014/5/9/incident-response-at-heroku)
- Described the Incident Commander role, inspired by natural disaster incident response.
- Also in presentation: [Incident Response Patterns: What we have learned at PagerDuty - Speaker Deck](https://speakerdeck.com/arupchak/incident-response-patterns-what-we-have-learned-at-pagerduty)
- The Google SRE book's [chapter about oncall](https://landing.google.com/sre/workbook/chapters/on-call/)
- [Writing Runbook Documentation When You’re An SRE](https://www.transposit.com/blog/2020.01.30-writing-runbook-documentation-when-youre-an-sre/)
- Playbooks “reduce stress, the mean time to repair (MTTR), and the risk of human error.”
- Using a template can be beneficial because starting from a blank document is incredibly hard.
- The Curse of Knowledge is a cognitive bias that occurs when someone is communicating with others and unknowingly assumes the level of knowledge of the people they are communicating with.
- Make your content easy to glance over.
- If a script is longer than a single line, treat it like code, and check it into a repository to be source control and potentially tested.
- [Incident Review and Postmortem Best Practices](https://newsletter.pragmaticengineer.com/p/incident-review-best-practices?s=r), Gergely Orosz
- [Computer Security Incident Handling Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf), NIST
- [Incident Management Resources](https://resources.sei.cmu.edu/library/asset-view.cfm?assetID=505044), Carnegie Mellon University
- [Sterile flight deck rule](https://en.wikipedia.org/wiki/Sterile_flight_deck_rule), Wikipedia
- [Shamir Secret Sharing It’s 3am.](https://max.levch.in/post/724289457144070144/shamir-secret-sharing-its-3am-paul-the-head-of)
- [Site Reliability Engineering and the Art of Improvisation](https://thenewstack.io/site-reliability-engineering-and-the-art-of-improvisation/) has lots of good training ideas
- Walkthroughs of observability toolsets
- Decision requirements table building
- Team knowledge elicitation
- Asking the question, “Why do we have on-call?”
- Spin the Wheel of Expertise!
- [Severity Levels](https://response.pagerduty.com/before/severity_levels/), PagerDuty  
Alerting:  
- [My Philosophy On Alerting](https://linuxczar.net/sysadmin/philosophy-on-alerting/)
- Pages should be urgent, important, actionable, and real.
- Err on the side of removing noisy alerts – over-monitoring is a harder problem to solve than under-monitoring.
- Symptoms are a better way to capture more problems more comprehensively and robustly with less effort.
- Include cause-based information in symptom-based pages or on dashboards, but avoid alerting directly on causes.
- The further up your serving stack you go, the more distinct problems you catch in a single rule. But don’t go so far you can’t sufficiently distinguish what’s going on.
- If you want a quiet oncall rotation, it’s imperative to have a system for dealing with things that need timely response, but are not imminently critical.
- This classical article has now become a [chapter](https://sre.google/sre-book/monitoring-distributed-systems/) in Google's SRE book.
- 🏙 [The Paradox of Alerts](https://speakerdeck.com/charity/the-paradox-of-alerts): why deleting 90% of your paging alerts can make your systems better, and how to craft an on-call rotation that engineers are happy to join.