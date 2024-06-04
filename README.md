# esa-snappy-utilities 库

***
## 概览
鉴于ESA-SNAP软件提供的snappy包仅对 snap engine 原生的Java代码做了简易的包装（只提供了对应Java类的Python接口，IDE也不会对此有任何提示），本库在此基础上对snappy作了进一步的包装，使得操作更加符合现代Python使用习惯，并增加了一定的注释。

***
## core模块
本模块中的SnapProduct类实现了对于snappy.Product类的封装，包括初始化、影像产品的基础信息读取等。

其次本模块中的Operator抽象类用于为各种具体的ESA-SNAP操作类提供模板，该抽象类中封装了ESA-SNAP Engine 中 GPF.createProduct() 方法，用于具体操作类继承。

***
## 其它模块
本库中的其它模块都是按照 ESA-SNAP 桌面版中各操作菜单栏的组织方式建立的，类似于辐射标定的操作，其路径为：
Radar -> Radiometric -> Calibration
那么辐射标定这一操作对应的类就位于 Rader.Radiometric.Calibration，