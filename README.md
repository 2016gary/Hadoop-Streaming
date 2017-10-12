## 1.词频统计 WordCount
```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.10.0.jar \
           -D stream.non.zero.exit.is.failure=false \
           -files '/home/cloudera/Desktop/mapper.py,/home/cloudera/Desktop/reducer.py' \
           -input /user/cloudera/word_count/*  \
           -output /user/cloudera/output/ \
           -mapper mapper.py \
           -reducer reducer.py 
```
## 2.朋友推荐 FoF
<label>关系图：</label>

<img src="/FoF/fof.png"  alt="无法显示该图片" />

<label>Job1：</label>
```
hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
           -D mapreduce.job.reduces=1 \
           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
           -input /user/enmoedu/input/* \
           -output /user/enmoedu/output/ \
           -mapper 'python mapper.py' \
           -reducer 'python reducer.py'
```

<label>结果：</label>

<img src="/FoF/result1.png"  alt="无法显示该图片" />

<label>Job2：</label>
```
hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
           -D mapreduce.job.reduces=1 \
           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
           -input /user/enmoedu/output/part-00000 \
           -output /user/enmoedu/output2/ \
           -mapper 'python mapper.py' \
           -reducer 'python reducer.py'
```

<label>最终结果：Sooo 如果给我推荐好友的话，请把韩孝周女神推荐给我 :-)</label>

<img src="/FoF/result2.png"  alt="无法显示该图片" />

## 3.PageRank
