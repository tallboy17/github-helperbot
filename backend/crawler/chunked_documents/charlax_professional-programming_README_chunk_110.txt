Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
- [Why We Leverage Multi-tenancy in Uber's Microservice Architecture](https://eng.uber.com/multitenancy-microservice-architecture/)
- [Developing in Production](https://tersesystems.com/blog/2020/01/22/developing-in-production/)
- Complex systems have emergent behavior, producing epiphenomenon that only appears with sufficient scale.
- Wood's theorem: As the complexity of a system increases, the accuracy of any single agent’s own model of that system decreases rapidly.
- The more tools and code that you add to create elements in a system, the harder it is to replicate an environment encompassing those tools and code.
- At the core of testing in production is the idea of splitting deployments (of artifacts) from releases (of features).
- [Testing in Production: the hard parts](https://medium.com/@copyconstruct/testing-in-production-the-hard-parts-3f06cefaf592), Cindy Sridharan
- The whole point of [actual] distributed systems engineering is you assume you’re going to fail at some point in time and you design the system in such a way that the damage, at each point is minimized, that recovery is quick, and that the risk is acceptably balanced with cost.
- How can you cut the blast radius for a similar event in half?
- Differentiate between deployment (0 risk) and release
- Build a deploy-observe-release pipeline
- Make incremental rollouts the norm (canaries, %-based rollouts, etc.)
- Test configuration changes just like you test code
- Default to roll back, avoid fixing forward (slow!)
- Eliminate gray failures - prefer crashing to degrading in certain cases
- Prefer loosely coupled services at the expense of latency or correctness
- Use poison tasters (isolate handling of client input)
- Implement per-request-class backpressure
- Have proper visibility from a client/end-user standpoint (client-side metrics)
- [Testing in Production, the safe way](https://medium.com/@copyconstruct/testing-in-production-the-safe-way-18ca102d0ef1)
- [Multi-Tenancy in a Microservice Architecture](https://www.usenix.org/system/files/login/articles/login_winter19_10_gud.pdf)