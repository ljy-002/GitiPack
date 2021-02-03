# GitiPack

## 如何使用：
命令`GitiPack.tig()`，需要在运行此包的时候提前运行。

命令`GitiPack.webg()`，需要在使用时运行。

函数`GitiPack.ctime()`返回时间戳

函数`GitiPack.mtime()`返回可读的字符串

函数`GitiPack.stime()`获取格式化时间字符串

函数`GitiPack.jc(值)`计算“值”的阶乘值，并写入“.tig”文件

函数`GitiPack.pertion(列表,开始索引,结束索引)`对“列表”进行全排序，并写入“.tig”文件

函数`GitiPack.w(内容)`将“内容”写入“.tig”文件

## 版本
### v1.3.2
创建函数`tig`和`webg`

### v1.4.5
修复了函数`tig`和`webg`不能调用的问题

### v1.5.8
修复了“Tig.ini”的版本错误问题

修复了更新v1.4.5后导入包时发生的错误

增添“__pycache__”配置文件，让程序运行的更快

更新`ctime()`、`mtime()`、`stime()`、`w()`函数

加入`jc()`、`pertion()`算法

### v1.6.0
修复了更改v1.5.8的主要文件后无法调用包的错误

添加了更多Tig的配置信息


