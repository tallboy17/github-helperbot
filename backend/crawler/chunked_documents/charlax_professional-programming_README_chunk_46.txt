Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
Here's a list of good books:  
- 📖 [Design Patterns: Elements of Reusable Object-Oriented Software](http://www.amazon.com/dp/0201633612/): dubbed "the gang of four", this is almost a required reading for any developer. A lot of those are a bit overkill for Python (because everything is an object, and dynamic typing), but the main idea (composition is better than inheritance) definitely is a good philosophy.
- And their nefarious nemesis [Resign Patterns](http://nishitalab.org/user/paulo/files/resign-patterns.txt)
- 📖 [Patterns of Enterprise Application Architecture](http://www.amazon.com/dp/0321127420/?tag=stackoverfl08-20): learn about how database are used in real world applications. Mike Bayer's SQLAlchemy has been heavily influenced by this book.
- 📖 [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215), Eric Evans
- 📖 [Clean Architecture](https://www.goodreads.com/book/show/18043011-clean-architecture), Robert C. Martin. Uncle Bob proposes an architecture that leverages the Single Responsibility Principle to its fullest. A great way to start a new codebase. Also checkout the [clean architecture cheatsheet](cheatsheets/Clean-Architecture-V1.0.pdf) and [this article](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).
- 📖 [Game Programming Patterns](https://www.amazon.com/dp/0990582906/ref=cm_sw_em_r_mt_dp_U_9xygFb9M86CXY): a book about design, sequencing, behavioral patterns and much more by Robert Nystrom explained through the medium of game programming. The book is also free to read online [here](https://gameprogrammingpatterns.com/contents.html).  
One of the absolute references on architecture is Martin Fowler: checkout his [Software Architecture Guide](https://martinfowler.com/architecture/).  
Articles:  
- O'Reilly's [How to make mistakes in Python](https://www.oreilly.com/content/how-to-make-mistakes-in-python/)
- [Education of a Programmer](https://hackernoon.com/education-of-a-programmer-aaecf2d35312): a developer's thoughts after 35 years in the industry. There's a particularly good section about design & complexity (see "the end to end argument", "layering and componentization").
- [Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design), Wikipedia.
- [On the Spectrum of Abstraction](https://www.youtube.com/watch?v=mVVNJKv9esE) 🎞, Cheng Lou
- [The “Bug-O” Notation](https://overreacted.io/the-bug-o-notation/), Dan Abramov
- [Antipatterns](./antipatterns)
- [Inheritance vs. composition](http://learnpythonthehardway.org/book/ex44.html): a concrete example in Python. [Another slightly longer one here](http://python-textbok.readthedocs.io/en/latest/Object_Oriented_Programming.html). [One last one, in Python 3](http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-3-delegation-composition-and-inheritance/#.V7SZ4tB96Rs).
- [Composition Instead Of Inheritance](http://c2.com/cgi/wiki?CompositionInsteadOfInheritance)
- [Complexity and Strategy](https://hackernoon.com/complexity-and-strategy-325cd7f59a92): interesting perspective on complexity and flexibility with really good examples (e.g. Google Apps Suite vs. Microsoft Office).
- [The Architecture of Open Source Applications](https://aosabook.org/en/index.html)
- [The Robustness Principle Reconsidered](https://cacm.acm.org/magazines/2011/8/114933-the-robustness-principle-reconsidered/fulltext)
- Jon Postel: "Be conservative in what you do, be liberal in what you accept from others." (RFC 793)
- Two general problem areas are impacted by the Robustness Principle: orderly interoperability and security.
- [Basics of the Unix Philosophy](http://catb.org/esr/writings/taoup/html/ch01s06.html#id2877610), Eric S Raymond
- [Eight Habits of Expert Software Designers: An Illustrated Guide](https://thereader.mitpress.mit.edu/habits-of-expert-software-designers/)
- [No Silver Bullet - Essence and Accident in Software Engineering](https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf), Frederick P. Brooks, Jr. (1986)
- There are four properties of software systems which make building software hard: Complexity, Conformity, Changeability and Invisibility
- There are ways to address this:
- Exploiting the mass market to avoid constructing what can be bought. ("Buy vs. Build")
- Using rapid prototyping as part of a planned iteration in establishing software requirements.
- Growing software organically, adding more and more function to systems as they are run, used, and tested
- Identifying and developing the great conceptual designers of the rising generation.
- (also included in The Mythical Man-Month)
- [Out of the Tar Pit](https://curtclifton.net/papers/MoseleyMarks06a.pdf), Ben Moseley, Peter Marks (2006) introduces the distinction between essential and accidental complexity
- Complexity is the root cause of the vast majority of problems with software today. Unreliability, late delivery, lack of security — often even poor performance in large-scale systems can all be seen as deriving ultimately from unmanageable complexity.
- Quoting Djikstra: "testing is hopelessly inadequate....(it) can be used very effectively to show the presence of bugs but never to show their absence."
- Functional programming goes a long way towards avoiding the problems of state-derived complexity, thanks to immutability and clear separation of state and logic.
- [A Note on Essential Complexity](https://olano.dev/blog/a-note-on-essential-complexity/)
- The goal of the software engineer is to minimize accidental complexity and assist with essential complexity.
- [Software Design is Knowledge Building](https://olano.dev/blog/software-design-is-knowledge-building/)
- Programming should be regarded as an activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand. This suggestion is in contrast to what appears to be a more common notion, that programming should be regarded as a production of a program and certain other texts.
- The building of the program is the same as the building of the theory of it by the team of programmers.
- [Cognitive load is what matters](https://minds.md/zakirullin/cognitive#long)
- A well-crafted monolith with truly isolated modules is often much more flexible than a bunch of microservices.
- Three decades on, microkernel-based GNU Hurd is still in development, and monolithic Linux is everywhere
- "Reduce cognitive load by limiting the number of choices." (Rob Pike)
- The same rule applies to all sorts of numeric statuses (in the database or wherever) - prefer self-describing strings.
- With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody. ([Hyrum's Law](https://www.hyrumslaw.com/))
- DDD is about problem space, not about solution space.
- Familiarity is not the same as simplicity
- The more mental models there are to learn, the longer it takes for a new developer to deliver value.  
> You can use an eraser on the drafting table or a sledge hammer on the construction site. (Frank Lloyd Wright)  
Resources:  
- 🧰 [Design Principles](https://principles.design/)