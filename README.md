# lightLabel
一个自己使用的标注系统（后端）



## 0. 声明

本项目目前只计划开放当前版本源码，以后的代码应该会闭源

## 1. 简介

该标注系统主要用于简单的标注任务，数据的标注信息会实时同步到数据库中，目前已经基本实现了文本分类任务（样本类别数量不大）。

## 2. 功能特性

- 系统各功能层次耦合度较低，将标注任务抽象成资源类。
- 将数据库访问功能也封装了抽象类，并且提供了MongoDB的默认实现，理论上可以自由添加其他数据库的实现。
- 采用flask作为web服务框架，较严格采用restful设计风格，系统会为每个标注任务都提供相关restAPI接口。

## 3. 使用示例

### 示例代码

```python
from lightlabel import Engine, TextClassification

text_cls = TextClassification('ttt_demo', 'des_demo')
text_cls.add_classes(['唐朝人物', '虚拟人物', '三国人物'])
text_cls.update_from_csv(r'C:\Users\Alienware\Desktop\text_classification_demo.csv', headers=['word'])
engine = Engine()
engine.add_plan(text_cls)
engine.run()
```

### 运行结果

```text
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
{'ttt_demo'}
 * Serving Flask app "lightlabel.web.engine" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
127.0.0.1 - - [21/Feb/2020 18:24:52] "GET /ttt_demo/items HTTP/1.1" 200 -
127.0.0.1 - - [21/Feb/2020 18:25:31] "GET /ttt_demo/data HTTP/1.1" 200 -
127.0.0.1 - - [21/Feb/2020 18:30:57] "GET /project_lists HTTP/1.1" 200 -
127.0.0.1 - - [21/Feb/2020 18:30:58] "GET /favicon.ico HTTP/1.1" 200 -
```

### `text_classification_demo.csv`文件中内容

```text
李白
曹操
夏侯惇
张飞
周瑜
陆逊
司马懿
```

### 数据库中该文本分类任务的数据内容（数据略有不符，因为我标注了几例）

```json
/* 1 */
{
    "_id" : ObjectId("5e4d411fc827b0709d554149"),
    "check_status" : false,
    "labeled_data" : "唐朝人物",
    "labeled_status" : true,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "李白"
    },
    "updated_time" : null
}

/* 2 */
{
    "_id" : ObjectId("5e4d411fc827b0709d55414b"),
    "check_status" : false,
    "labeled_data" : "三国人物",
    "labeled_status" : true,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "曹操"
    },
    "updated_time" : null
}

/* 3 */
{
    "_id" : ObjectId("5e4d411fc827b0709d55414d"),
    "check_status" : false,
    "labeled_data" : "三国人物",
    "labeled_status" : true,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "夏侯惇"
    },
    "updated_time" : null
}

/* 4 */
{
    "_id" : ObjectId("5e4d411fc827b0709d55414f"),
    "check_status" : false,
    "labeled_data" : null,
    "labeled_status" : false,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "张飞"
    },
    "updated_time" : null
}

/* 5 */
{
    "_id" : ObjectId("5e4d411fc827b0709d554151"),
    "check_status" : false,
    "labeled_data" : null,
    "labeled_status" : false,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "周瑜"
    },
    "updated_time" : null
}

/* 6 */
{
    "_id" : ObjectId("5e4d411fc827b0709d554153"),
    "check_status" : false,
    "labeled_data" : null,
    "labeled_status" : false,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "陆逊"
    },
    "updated_time" : null
}

/* 7 */
{
    "_id" : ObjectId("5e4d411fc827b0709d554155"),
    "check_status" : false,
    "labeled_data" : null,
    "labeled_status" : false,
    "labeled_user" : null,
    "raw_data" : {
        "word" : "司马懿"
    },
    "updated_time" : null
}
```

### 数据库中该文本分类任务对应的任务信息

```json
/* 1 */
{
    "_id" : ObjectId("5e4d411fc827b0709d554143"),
    "description" : "des_demo",
    "label_status" : true,
    "task_type" : "TextClassification",
    "title" : "ttt_demo",
    "data" : {
        "classes" : [ 
            "唐朝人物", 
            "虚拟人物", 
            "三国人物"
        ]
    },
    "data_path" : [ 
        "C:\\Users\\Alienware\\Desktop\\text_classification_demo.csv"
    ]
}
```

### rest接口

- `http://localhost:5000/project_lists`：返回所有任务信息
- `http://localhost:5000/ttt_demo/items`：该任务所有标注条目
- `http://localhost:5000/ttt_demo/data`：该任务相关数据，如在该例中为所有标签类别组成的列表

具体如下截图：

![UTOOLS1582280855124.png](https://lightsmile-img.oss-cn-beijing.aliyuncs.com/UTOOLS1582280855124.png)

![UTOOLS1582280902325.png](https://lightsmile-img.oss-cn-beijing.aliyuncs.com/UTOOLS1582280902325.png)

![UTOOLS1582280929192.png](https://lightsmile-img.oss-cn-beijing.aliyuncs.com/UTOOLS1582280929192.png)

## 4. 参考

- [使用mongodb增删改查深层嵌套文档_数据库_qq_42427109的博客-CSDN博客](https://blog.csdn.net/qq_42427109/article/details/90635466)
- [pycharm: 恢复(reset) 误删文件_开发工具_JNing-CSDN博客](https://blog.csdn.net/JNingWei/article/details/79966183)
- [快速入门 — Flask-RESTful 0.3.1 documentation](http://www.pythondoc.com/Flask-RESTful/quickstart.html)
- [[译] 用 Flask 和 Vue.js 开发一个单页面应用 - 掘金](https://juejin.im/post/5c1f7289f265da612e28a214)


