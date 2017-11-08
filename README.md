# Hadoop Streaming & Python3
## 1.词频统计 WordCount
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
		   -D mapreduce.job.name="WordCount" \
		   -D mapreduce.job.maps=2 \
	           -D mapreduce.job.reduces=1 \
		   -D mapreduce.job.priority=NORMAL \
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
	           -D mapreduce.job.name="FoF_Job1" \
		   -D mapreduce.job.maps=2 \
	           -D mapreduce.job.reduces=1 \
		   -D mapreduce.job.priority=HIGH \
	           -files '/home/enmoedu/Desktop/FOF/mapper.py,/home/enmoedu/Desktop/FOF/reducer.py' \
	           -input /user/enmoedu/input/* \
	           -output /user/enmoedu/output/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py'

### 结果：
<img src="/2.FoF/result1.png"  alt="无法显示该图片" />

### Job2：
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.name="FoF_Job2" \
		   -D mapreduce.job.maps=2 \
	           -D mapreduce.job.reduces=1 \
		   -D mapreduce.job.priority=HIGH \
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
- 入链等于投票
	>PageRank让链接来投票，到一个页面的超链接相当于对该页投一票
- 入链数量
	>如果一个页面节点接收到的其他网页指向的入链数量越多，那么这个页面越重要
- 入链质量
	>指向页面A的入链质量不同，质量高的页面会通过链接向其他页面传递更多的权重，所以越是质量高的页面指向页面A，则页面A越重要
- 初始值
	>每个页面设置相同的PR值
	
	>Google的PageRank算法给每个页面的PR初始值为1
- 迭代递归计算（收敛）
	>Google不断的重复计算每个页面的PageRank，那么经过不断的重复计算，这些页面的PR值会趋向于稳定，也就是收敛的状态
	
	>在具体企业应用中怎么样确定收敛标准？
	
	>1.每个页面的PR值和上一次计算的PR值相等
	
	>2.设定一个差值指标（0.0001），当所有页面和上一次计算的PR差值平均小于该标准时则收敛
	
	>3.设定一个百分比（99%），当99%的页面和上一次计算的PR相等
- 修正PageRank计算公式
	>由于存在一些出链为0，也就是那些不链接任何其他页面的网页，也称为孤立网页，使得很多网页能被访问到，因此需要对PageRank公式进行修正，即在简单公式的基础上增加了阻尼系数（Damping Factor）q，q一般取值q=0.85

### PageRank计算公式：
<img src="/3.PageRank/PageRankExpression.png"  alt="无法显示该图片" />

### 网络页面链接图：
<img src="/3.PageRank/PageLink.png"  alt="无法显示该图片" />

### Python3实现PageRank算法：
	i = 0
	num = 0
	target_value = 0.001
	damping = 0.85
	a_arr = [1.0]
	b_arr = [1.0]
	c_arr = [1.0]
	d_arr = [1.0]
	
	
	def page_rank(a_arr, b_arr, c_arr, d_arr):
	    a_arr.append((1 - damping) / 4 + damping * c_arr[i] / 2)
	    b_arr.append((1 - damping) / 4 + damping * (a_arr[i] / 2 + c_arr[i] / 2 + d_arr[i] / 2))
	    c_arr.append((1 - damping) / 4 + damping * (b_arr[i] + d_arr[i] / 2))
	    d_arr.append((1 - damping) / 4 + damping * a_arr[i] / 2)
	    return a_arr, b_arr, c_arr, d_arr
	
	
	while True:
	    i = num
	    page_rank(a_arr, b_arr, c_arr, d_arr)
	    num += 1
	    value = (abs(a_arr[i] - a_arr[i - 1]) + abs(b_arr[i] - b_arr[i - 1]) + abs(c_arr[i] - c_arr[i - 1]) + abs(
	        a_arr[i] - a_arr[i - 1])) / 4
	    if value <= target_value:
	        print('迭代次数：' + str(num))
	        print('A\tB\tC\tD:')
	        print(a_arr[i], b_arr[i], c_arr[i], d_arr[i])
	        break
### 运行结果：
![](https://i.imgur.com/IDMUeZP.png)

### MapReduce模型：
<img src="/3.PageRank/MapReduce.png"  alt="无法显示该图片" />

### Hadoop Streaming：
	hadoop jar /opt/cloudera/parcels/CDH-5.9.0-1.cdh5.9.0.p0.23/lib/hadoop-mapreduce/hadoop-streaming.jar \
	           -D mapreduce.job.name="PageRank" \
		   -D mapreduce.job.maps=2 \
	           -D mapreduce.job.reduces=1 \
		   -D mapreduce.job.priority=VERY_HIGH \
	           -files '/home/enmoedu/Desktop/PageRank/mapper.py,/home/enmoedu/Desktop/PageRank/reducer.py' \
	           -input /user/enmoedu/input/PageRank.txt \
	           -output /user/enmoedu/output/ \
	           -mapper 'python mapper.py' \
	           -reducer 'python reducer.py'
