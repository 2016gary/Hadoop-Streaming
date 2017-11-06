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
<img src="/WordCount/result.png"  alt="无法显示该图片" />

---
## 2.好友推荐 FoF
### 关系图：
<img src="/FoF/fof.png"  alt="无法显示该图片" />

### Job1：
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.reduces=1 \
	           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
	           -input /user/enmoedu/input/* \
	           -output /user/enmoedu/output/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py'

### 结果：
<img src="/FoF/result1.png"  alt="无法显示该图片" />

### Job2：
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.reduces=1 \
	           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
	           -input /user/enmoedu/output/part-00000 \
	           -output /user/enmoedu/output2/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py'

### 最终结果：Sooo 如果给我推荐好友的话，请把韩孝周女神推荐给我 :-)
<img src="/FoF/result2.png"  alt="无法显示该图片" />

---
## 3.PageRank
