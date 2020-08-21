# lever 开发日志

## 2020-07-31 23:40

针对“基于json的REPL-like任务树管理器”这个想法，有以下可以开发的要点：

1. 日志功能：记录每次用户命令，并对累计数据进行统计分析
2. 多任务树功能：每一个任务树对应一组database/log

#### 完成的工作

1. Lever类下对project的操作
2. dummy parser（用于测试io，序列化）

## 2020-08-03 15:49

#### 想法

1. 每个project应包含两个键值对：name,
   cycle。其中cycle的值为各个cycle实际存放内容的列表。
2. 能通过相似结构的命令对cycle进行操作
3. 需要一个真正的parser来处理输入的命令
4. 应该能根据指定的时间对cycle进行标记（进行中/已完成/搁置）
5. 应该有一定的高亮
6. 启动过程：写入内存，检查日期，提醒管理

#### 完成的工作

以上的1, 2, 3, 4, 6均有了一定程度的实现。

高亮和logging是接下来工作的重点。

## 2020-08-04 12:52

#### 想法

1. 为命令行程序添加高亮
2. 添加logging功能，记录被保存下来的重要行为和每周为单位的统计数据

#### 完成的工作

以上功能均有了一些实现

现在的lever已经具备了一定的实用性。

## 2020-08-16 16:30

#### 想法

从完成第一版lever到现在已经过去两个星期了，在使用lever的过程中，观察到平时做事情其实把规划写出来不是难事，比较难的是在“下定决心努力工作”之后的几次施法，几个懒觉之后在脑子里保持这个努力工作虚心学习的状态。这其实也是lever这个名字的初衷：像一个拉杆一样，作为进入工作状态的一个仪式来进行，同时具备管理project, cycles，能方便地进行查询的一个入口。这一点在这个版本的lever当中没有得到很好的体现。

所以现在打算对lever在做一次大的改版（lever 0.0.2），加上一个lever简报的功能，将每天的任务自动打印出来。

## 2020-08-21 01:38

#### 想法

今天初步接触了git和github，把重要的dotfile迁移到了github上。

在使用git的时候，偶然发现`git pull`和`lever pull`挺像的。但是git是一个丰富的VCS，lever现在只是一个功能简单的project control system (for human)。

而且现在的lever可能需要人工进行一定的设置才能在新的机器上运行（需要向配置文件里添加函数做为wrapper）。这说明现在的lever远远不够完善。

所以如果接下来有时间继续开发，lever应该具有：

1. multiple subcommands (core functions can be accessed outside REPL)
	* lever pull: (remains?) pulling current projects and cycles
	* lever stat: report on statistics
	* lever ls/add/rm/tog (maybe?)
	* lever push: (idea) as the last motion of a day, human report back to lever
2. automatic installation (like dotbot, `git clone` and `./install`)
