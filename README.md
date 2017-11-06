# Hadoop Streaming & Python3
## 1.词频统计 WordCount
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.reduces=1 \
	           -files '/home/enmoedu/Desktop/mapper.py,/home/enmoedu/Desktop/reducer.py,/home/enmoedu/Desktop/combiner.py' \
	           -input /user/enmoedu/input/Shakespeare \
	           -output /user/enmoedu/output/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py' \
	           -combiner 'python combiner.py'


### 结果：
<img src="/1.WordCount/result.png"  alt="无法显示该图片" />

---
## 2.好友推荐 FoF
### 关系图：
<img src="/2.FoF/fof.png"  alt="无法显示该图片" />

### Job1：
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.reduces=1 \
	           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
	           -input /user/enmoedu/input/* \
	           -output /user/enmoedu/output/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py'

### 结果：
<img src="/2.FoF/result1.png"  alt="无法显示该图片" />

### Job2：
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.reduces=1 \
	           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
	           -input /user/enmoedu/output/part-00000 \
	           -output /user/enmoedu/output2/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py'

### 最终结果：Sooo 如果给我推荐好友的话，请把韩孝周女神推荐给我 :-)
<img src="/2.FoF/result2.png"  alt="无法显示该图片" />

---
## 3.PageRank
### PageRank算法原理：
1. 在初始阶段：网页通过链接关系构建起Web图，每个页面设置相同的PageRank值，通过若干轮的计算，会得到每个页面所获得的最终PageRank值。随着每一轮的计算进行，网页当前的PageRank值会不断得到更新。
2. 在一轮中更新页面PageRank得分的计算方法：在一轮更新页面PageRank得分的计算中，每个页面将其当前的PageRank值平均分配到本页面包含的出链上，这样每个链接即获得了相应的权值。而每个页面将所有指向本页面的入链所传入的权值求和，即可得到新的PageRank得分。当每个页面都获得了更新后的PageRank值，就完成了一轮PageRank计算。

### PageRank计算公式：
<img src="/3.PageRank/PageRankExpression.png"  alt="无法显示该图片" />

### 网络页面链接图：
<img src="/3.PageRank/PageLink.png"  alt="无法显示该图片" />
