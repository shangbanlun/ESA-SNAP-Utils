# esa-snappy-utilities 库

***
## 概览
鉴于ESA-SNAP软件提供的snappy包仅对 snap engine 原生的Java代码做了简易的包装（只提供了对应Java类的Python接口，IDE也不会对此有任何提示），本库在此基础上对snappy作了进一步的包装，使得操作更加符合现代Python使用习惯，并增加了一定的注释。

***
## 基础使用

本库的基本功能为依靠 ESA-SNAP Engine 实现多个极化SAR影像的批量操作，这里用哨兵一号A卫星的双极化单视复数影像举例，从哥白尼[https://dataspace.copernicus.eu/]官方网站上下载，我们检索到了覆盖上海及其周边地区的两景影像，分别是：

* S1A_IW_SLC__1SDV_20240602T095511_20240602T095538_054143_069586_39F6.SAFE
* S1A_IW_SLC__1SDV_20240602T095536_20240602T095602_054143_069586_C640.SAFE

将两个影像下载下来后，对于SLC影像一般的预处理流程如下：

轨道文件替换 TOPSAR影像合并 辐射定标 TOPSAR影像Deburt 研究子区域裁剪 

极化矩阵计算 多视处理 相干斑滤波 极化分解 地形改正 

单个处理的如下：

```python
import esa
```

上面整个流程的完整脚本代码位于/example目录下，在与该脚本相同的目录下创建一个/dataset文件夹并将两个影像文件置于其中该脚本即可运行，生成的影像同样位于/dataset文件夹下。

***
## core模块
本模块中的 SnapProduct 类实现了对于 snappy.Product 类的封装，包括初始化、影像产品的基础信息读取等。

其次本模块中的 Operator 抽象类用于为各种具体的 ESA-SNAP 操作类提供模板，该抽象类中封装了 ESA-SNAP Engine 中  GPF.createProduct() 方法，用于具体操作类继承。但在实际使用当中基于 GPF.createProduct() 方法实现操作的策略会遇到很多问题，故将该策略弃用。

当前本库使用的用于实现影像操作的策略是基于流程图的，ESA-SNAP 桌面版中提供了一个名为 GraphBuilder 的工具，在该工具中可以将一整个影像处理的过程视作一个流程图。具体来说各个不同的影像操作被视为一个节点，而影像的读入与写出是两种特殊的节点，不同节点之间按照你想要执行的操作流程用单向边来连接，而Read节点必须作为起点，Write节点必须作为终点，一个典型的流程图如下：

通过点击节点就可以设置该节点对应操作的具体参数，编辑完成后可以直接点击Run执行该流程图。若需要批量使用该流程图也可以单击Save将该图保存为xml文件，这样下次使用时就可以直接单击Load加载该流程图，然后只需更改Read节点中输入文件路径参数和Write节点中输出文件路径参数，就可以对多个影像进行一样的处理。

ESA-SNAP 软件在安装了桌面版之外，还提供了一个CLI工具——**流程图处理工具**（*Graph Process Tool, GPT*）用于执行流程图的处理，该工具位于软件根目录中的 bin 文件夹下，其具体使用参考如下：

* 首先在桌面版中编辑并保存一个流程图的xml文件。

* 然后在 bin 文件夹路径下执行下列命令：

  ```shell
  $ ./gpt graph.xml
  ```

* 这样该流程图就执行完成了。

尽管使用GPT工具大大简化了多个影像的批量处理过程，但仍然需要每次手动更改Read、Write的相关参数，故我们将流程图的制作与执行全部封装在core.Sequential类中，利用Python脚本的灵活性将整个批量处理的过程全部脚本化。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

***
## 其它模块
本库中的其它模块都是按照 ESA-SNAP 桌面版中各操作菜单栏的组织方式建立的，例如辐射标定的操作，在桌面版中其路径为：Radar -> Radiometric -> Calibration，那么辐射标定这一操作对应的类就位于 Rader.Radiometric.Calibration，


***
## 
testing: slice assambly -> orb -> cal -> deburst -> mat -> ml -> tc
result: failed, get band noise.

testing: orb -> cal -> deburst -> merge -> mat -> ml -> tc

testing: orb -> cal -> deburst -> cropping -> merge -> mat -> ml -> tc


take the subset of the asm image with :
* left-top corner: lat 31.9049 lon 121.1212
* right-bot corner: lat 31.3880 lon 121.9957

which the WKT of this rectangle is 
```
POLYGON((121.1212 31.9049, 121.9957 31.9049, 121.9957 31.3880, 121.1212 31.3880, 121.1212 31.9049))
```