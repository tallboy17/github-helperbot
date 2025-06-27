Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
Also see the Incident Response section in this doc  
- [Rubber Duck Problem Solving](http://blog.codinghorror.com/rubber-duck-problem-solving/)
- [Rubber Ducking](http://c2.com/cgi/wiki?RubberDucking)
- [Five Whys](https://en.wikipedia.org/wiki/5_Whys)
- [The Five Lies Analysis](https://serce.me/posts/14-10-2021-the-five-lies-analysis)
- The real problem reveals itself when the technique becomes a part of a template.
- Action items can be very distant from the root cause.
- Related article: [The Evolution of SRE at Google](https://www.usenix.org/publications/loginonline/evolution-sre-google)
- [The Infinite Hows](http://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/) criticizes the five whys method and advocates for a different set of questions to learn from the most from incidents.
- See also: [Human errors: models and management](https://app.box.com/s/7z35l09amvr1vwxouh2s)
- "The issue with the Five Whys is that it’s tunnel-visioned into a linear and simplistic explanation of how work gets done and events transpire."
- "Human error becomes a starting point, not a conclusion." (Dekker, 2009)
- "When we ask 'how?', we’re asking for a narrative."
- "When it comes to decisions and actions, we want to know how it made sense for someone to do what they did."
- At each "why" step, only one answer will be selected for further investigation. Asking "how" encourage broader exploration.
- "In accident investigation, as in most other human endeavours, we fall prey to the What-You-Look-For-Is-What-You-Find or WYLFIWYF principle. This is a simple recognition of the fact that assumptions about what we are going to see (What-You-Look-For), to a large extent will determine what we actually find (What-You-Find)." (Hollnagel, 2009, p. 85) (see [illustration of WYLFIWYF](https://www.youtube.com/watch?v=vJG698U2Mvo))
- "A final reason why a 'root cause' may be selected is that it is politically acceptable as the identified cause. Other events or explanations may be excluded or not examined in depth because they raise issues that are embarrassing to the organization or its contractors or are politically unacceptable." (Nancy Leveson, Engineering a Safer World, p. 20)
- [Bounded rationality](https://en.wikipedia.org/wiki/Bounded_rationality): rational individuals will select a decision that is satisfactory rather than optimal
- The article provide concrete ways and questions to solicit stories from people, which will yield better insights.
- What were you expecting to happen?
- If you had to describe the situation to your colleague at that point, what would you have told?
- Did this situation fit a standard scenario?
- What were you trying to achieve?Were there multiple goals at the same time?Was there time pressure or other limitations on what you could do?
- [See template here](http://www.kitchensoap.com/wp-content/uploads/2014/09/Velocity2014-PM-Fac-Handout-Debrief.pdf)
- [Linux Performance Analysis in 60,000 Milliseconds](http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html)
- [Post-Mortems at HubSpot: What I Learned From 250 Whys](https://product.hubspot.com/blog/bid/64771/post-mortems-at-hubspot-what-i-learned-from-250-whys)
- [Debugging zine](https://jvns.ca/debugging-zine.pdf), Julian Evans
- [If you understand a bug, you can fix it](https://wizardzines.com/comics/understand-can-fix/)
- [The Thirty Minute Rule](https://daniel.feldroy.com/posts/thirty-minute-rule): if anyone gets stuck on something for more than 30 minutes, they should ask for help
- [How to create a Minimal, Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example), Stack Overflow
- [Some ways to get better at debugging](https://jvns.ca/blog/2022/08/30/a-way-to-categorize-debugging-skills/), Julia Evans
- Learn the codebase
- Learn the system (e.g., HTTP stack, database transactions)
- Learn your tools (e.g., `strace`, `tcpdump`)
- Learn strategies (e.g., writing code to reproduce, adding logging, taking a break)
- Get experience: according to a study, "experts simply formed more correct hypotheses and were more efficient at finding the fault."
- [What exactly is the 'Saff Squeeze' method of finding a bug?](https://stackoverflow.com/questions/23865274/what-exactly-is-the-saff-squeeze-method-of-finding-a-bug)
- A systematic technique for deleting both test code and non-test code from a failing test until the test and code are small enough to understand.
- [tcpdump is amazing](https://jvns.ca/blog/2016/03/16/tcpdump-is-amazing/), Julia Evans
- [What we talk about when we talk about ‘root cause’](https://github.com/readme/guides/root-cause)
- [David A. Wheeler's Review of "Debugging" by David J. Agans](https://dwheeler.com/essays/debugging-agans.html)
- [Troubleshooting: The Skill That Never Goes Obsolete](https://www.autodidacts.io/troubleshooting/)
- Includes links to interesting debugging stories
- [Falsehoods software teams believe about user feedback](https://thoughtbot.com/blog/falsehoods-software-teams-believe-about-user-feedback)