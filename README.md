## 词频统计
## 朋友推荐
```
hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
           -D mapreduce.job.reduces=1 \
           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
           -input /user/enmoedu/input/* \
           -output /user/enmoedu/output/ \
           -mapper 'python mapper.py' \
           -reducer 'python reducer.py'
           
