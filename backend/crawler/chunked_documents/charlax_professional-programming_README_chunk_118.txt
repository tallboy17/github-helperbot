Repository: charlax/professional-programming
Language: Python
Stars: 47703
Forks: 3794
-----
- [A Map of Sync](https://stack.convex.dev/a-map-of-sync) categorizes state sync into 9 dimensions.
- Data model:
- Size: How large is the data set that a single client can access?
- Update rate: How often do clients send updates?
- Structure: Is the data rich with structure or flat and unstructured?
- Systems requirements:
- Input latency: How long can updates be delayed while maintaining a good user experience?
- Offline: How many interactions does the app need to support offline?
- Concurrent clients: How many concurrent clients will look at the same data?
- Programming model:
- Centralization: How centralized is the programming model and infrastructure?  Flexibility: How flexible are sync policies, especially around conflict resolution?
- Consistency: What types of invariants can the application assert about its data model, and how strong can these invariants be?