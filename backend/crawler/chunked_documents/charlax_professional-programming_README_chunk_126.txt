Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
- ⭐️ [Testing strategies in a microservices architecture](http://martinfowler.com/articles/microservice-testing/) (Martin Fowler) is an awesome resources explaining how to test a service properly.
- 🧰 [Testing Distributed Systems](https://asatarin.github.io/testing-distributed-systems/)  
Why test:  
- [Why bother writing tests at all?](https://dave.cheney.net/2019/05/14/why-bother-writing-tests-at-all), Dave Cheney. A good intro to the topic.
- Even if you don’t, someone will test your software
- The majority of testing should be performed by development teams
- Manual testing should not be the majority of your testing because manual testing is O(n)
- Tests are the critical component that ensure you can always ship your master branch
- Tests lock in behaviour
- Tests give you confidence to change someone else’s code  
How to test:  
- [A quick puzzle to test your problem solving](http://www.nytimes.com/interactive/2015/07/03/upshot/a-quick-puzzle-to-test-your-problem-solving.html?_r=0)... and a great way to learn about confirmation bias and why you're mostly writing positive test cases.
- [Testing is not for beginners](https://www.calhoun.io/testing-is-not-for-beginners/): why learning to test is hard. This shouldn't demotivate you though!
- [Arrange-act-assert: a pattern for writing good tests](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)
- [Test smarter, notharder](https://lukeplant.me.uk/blog/posts/test-smarter-not-harder/)  
Test pyramid:  
- [The test pyramid](http://martinfowler.com/bliki/TestPyramid.html), Martin Fowler
- [Eradicating non-determinism in tests](http://www.martinfowler.com/articles/nonDeterminism.html), Martin Fowler
- [The practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html), MartinFowler.com
- Be clear about the different types of tests that you want to write. Agree on the naming in your team and find consensus on the scope of each type of test.
- Every single test in your test suite is additional baggage and doesn't come for free.
- Test code is as important as production code.
- [Software testing anti-patterns](http://blog.codepipes.com/testing/software-testing-antipatterns.html), Kostis Kapelonis.
- [Write tests. Not too many. Mostly integration.](https://blog.kentcdodds.com/write-tests-not-too-many-mostly-integration-5e8c7fff591c) for a contrarian take about unit testing
- 🎞 [Unit test 2, Integration test: 0](https://www.youtube.com/watch?v=Oj8bfBlwHAg&ab_channel=PercyRicardoAnticonaMasabel)
- [Testing in the Twenties](https://www.tbray.org/ongoing/When/202x/2021/05/15/Testing-in-2021)
- [Google Testing Blog: Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)
- [Pyramid or Crab? Find a testing strategy that fits](https://web.dev/articles/ta-strategies), web.dev  
End-to-end tests:  
- [Just say no to more end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html), Google Testing Blog
- [End-to-end testing considered harmful](https://www.stevesmith.tech/blog/end-to-end-testing-considered-harmful/)