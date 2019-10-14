from jieba import analyse

# 引入TextRank关键词抽取接口
textrank = analyse.textrank

# 原始文本
text = "岗位职责：1.需求分析，编写需求规格说明书2.系统设计，编写开发设计说明书。3.系统分析，对系统、产品进行功能、性能调优。4.项目管理，带领团队完成项目，带领团队成员在技术、职业素养上有所提高5.单元测试。岗位要求：1.遵守项目开发规范、编码规范、文档规范。2.掌握主流数据库（Oracle、MySql、SQL Server）的基础语法，能够编写SQL语句查询、修改、删除、新增数据，能够读懂并独立编写存储过程、触发器、函数；能够对数据库进行性能调优；3.技术掌握至少4种后端+3种后端开发技术框架（SpringMVC、Spring、MyBatis、Quartz、Shiro、Freemarker、Layer、JQuery、Ajax、EasyUI）4.掌握数据建模工具，并能利用工具完成数据建模工作，实现DB初始化。5.掌握至少2种中间件容器（Microsoft IIS、IBM WebSphere、BEA WebLogic、Apache、Tomcat、JBoss），且至少掌握1种中间件容器的性能调优、故障解决工作。6.掌握UML建模工具，熟练运用UML建模工具完成类图的设计。7.作为核心开发人员参与，配合质保、产品规划完成需求规格评审、发版，需求规格页数大于35页8.参与研发周期大于1个月的项目，至少2个；独立完成任务量大于10人/天的功能模块开发，至少5个。能力要求：掌握基础的SSM开发框架，能够根据需求规格完成编码工作。掌握基础的软件设计工具，能够独立完成需求设计。掌握Tomcat、JBoss、WebLogic等中间容器的优化.能够编写复杂的Oracle存储过程、触发器；能够对Oracle数据库进行调优."

print("\nkeywords by textrank:")
# 基于TextRank算法进行关键词抽取
keywords = textrank(text)
# 输出抽取出的关键词
for keyword in keywords:
    print(keyword + "/",)