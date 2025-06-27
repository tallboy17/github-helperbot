Repository: apachecn/ailearning
Language: Python
Stars: 41016
Forks: 11568
-----
文本分类是指标记句子或文档，例如电子邮件垃圾邮件分类和情感分析。  
下面是一些很好的初学者文本分类数据集。  
1. [路透社Newswire主题分类](http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html)（路透社-21578）。1987年路透社出现的一系列新闻文件，按类别编制索引。[另见RCV1，RCV2和TRC2](http://trec.nist.gov/data/reuters/reuters.html)。
2. [IMDB电影评论情感分类（斯坦福）](http://ai.stanford.edu/~amaas/data/sentiment)。来自网站imdb.com的一系列电影评论及其积极或消极的情绪。
3. [新闻组电影评论情感分类（康奈尔）](http://www.cs.cornell.edu/people/pabo/movie-review-data/)。来自网站imdb.com的一系列电影评论及其积极或消极的情绪。  
有关更多信息，请参阅帖子:
[单标签文本分类的数据集](http://ana.cachopo.org/datasets-for-single-label-text-categorization)。  
> 情感分析  
比赛地址: https://www.kaggle.com/c/word2vec-nlp-tutorial  
* 方案一(0.86): WordCount + 朴素 Bayes
* 方案二(0.94): LDA + 分类模型（knn/决策树/逻辑回归/svm/xgboost/随机森林）
* a) 决策树效果不是很好，这种连续特征不太适合的
* b) 通过参数调整 200 个topic，信息量保存效果较优（计算主题）
* 方案三(0.72): word2vec + CNN
* 说实话: 没有一个好的机器，是调不出来一个好的结果 (: 逃  
**通过AUC 来评估模型的效果**