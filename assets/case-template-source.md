


# 一、概述

## 1.1 案例介绍

<span style="color:rgb(216,27,68)">*//案例介绍，需简短有力吸引眼球，正文删除这行*</span>

## 1.2 适用对象
<span style="color:rgb(216,27,68)">*//开发者可根据案例实际受众选择开发者类型，正文删除这行*</span>

-   企业开发者
-   个人开发者
-   高校学生

## 1.3 案例时间

如：本案例总时长预计45分钟。

## 1.4 案例流程
<span style="color:rgb(216,27,68)">*//案例流程的简单图示以及流程说明，正文删除这行*</span>

<img src="https://fileserver.developer.huaweicloud.com/FileServer/getFile/spaceguides/804/607/a5f/6cf46c0e47804607a5f980bd1c414a26.20250909031654.50697660942367254469403710359374:50560908031655:2421:6927E15D8D2364446E754309F07EE049D7345B87BB1827A6B4B0062F14E0BDB3.png?customIdMd=a7b03596c49046808a6fe0c93b60b137"  width=1200px />

<span style="color:rgb(216,27,68)">*//此处的说明是对实验流程图的解释说明，下面的序号要和图中形成对应关系，正文删除这行*</span>
说明：

1.  购买弹性云服务器，创建虚拟私有云及安全组；
2.  登录云主机，购买CodeArts并创建CodeArts项目，创建代码质量门禁检查流水线；
3.  CodeArts IDE本地拉取云上代码；
4.  CodeArts IDE集成CodeArts Pipeline插件实现本地调用华为云云上流水线任务；
5.  云上流水线查看运行结果；进行分支合并，创建部署流水线。


## 1.5 资源总览
<span style="color:rgb(216,27,68)">*//罗列案例中使用的资源，主要是涉及收费的服务，正文删除这行*</span>
本案例预计花费**4.75元**。体验完成后请及时释放资源，避免产生多余的费用。


| **资源名称**  |  **规格** |  **单价（元）** |
| ------------ | ------------ | ------------ |
|  开发者空间云开发环境 | ARM\| 4 vCPUs 8GB \| Ubuntu 24.04 Server 定制版  |  免费 |
|  [弹性云服务器ECS](https://www.huaweicloud.com/product/ecs.html) |  X86计算，通用计算增强型  \| c7.large.2 \| 2 vCPUs \| 4 GiB CentOS 7.6 64bit (40GB) | 0.6  |
| [弹性公网IP](https://www.huaweicloud.com/product/eip.html)  |  按流量计费 5Mbit/s  |  0.8元/GB |
| [华为云码道（CodeArts）代码智能体](https://codearts.huaweicloud.com/download.html?source=dmzntgwds&sourcead=dmzntgwalzx)  |  通用体验版 | 免费  |
|  [分布式消息服务Kafka实例](https://www.huaweicloud.com/product/dmskafka.html) | 按需计费，集群版 3.x， kafka.2u4g.cluster.small，数量：3  |  3.15 |


# 二、环境和资源准备

<span style="color:rgb(216,27,68)">*//案例的准备工作，比如案例中用到大模型服务需提前领取、环境中需要预安装工具、数据库、三方库等等，正文删除这行*</span>

<span style="color:rgb(216,27,68)">*//1.华为开发者空间需要设置超链接，使用链接：https://developer.huaweicloud.com/space/home，正文删除这行*</span>
<span style="color:rgb(216,27,68)">*//2.开发者空间基础的操作可以引用原子案例，比如领取华为云MaaS平台大模型Tokens福利（任选其一）可参考[原子案例列表](https://bbs.huaweicloud.com/forum/thread-0282200732583629096-1-1.html)，正文删除这行*</span>

## 2.1 *如：*领取华为云MaaS平台大模型Tokens福利（任选其一）

**方式一**： 登录华为开发者空间，参考案例[《华为开发者空间 - ModelArts Studio大模型通用代金券领取使用指导》](https://devstation.connect.huaweicloud.com/space/devportal/casecenter/2bbe5c54fec441899094e456c4f137fe/1)中的“二、 开通MaaS平台大模型”章节内容领取代金券，获取到模型的**API地址**、**模型名称**和**API Key**。

**方式二**： 登录华为开发者空间，参考案例[《华为云MaaS平台大模型Tokens领取使用指导》](https://devstation.connect.huaweicloud.com/space/devportal/casecenter/538a4b85f4d240b4bfbd45a1c6a93e70/1)中的“二、 领取MaaS平台大模型Tokens”章节内容，领取MaaS平台DeepSeek V3系列大模型Tokens代金券，购买ModelArts Studio DeepSeek Tokens套餐包，开通模型服务，最后获取到模型的**API地址**、**模型名称**和**API Key**。

<img src="https://fileserver.developer.huaweicloud.com/FileServer/getFile/spaceguides/2b4/6cf/960/675e761ca42b46cf96050bedc4d5868c.20260203041106.63108339874953276197713273941669:50570202041108:2421:5DA8814FFC4336B5308917863F22AE7EAD01EC5A4CB75264C7FCD7671C2F904C.png?customIdMd=04bf3b5abd1b430aa0833d6fac78cf95" width=1000px />

<img src="https://fileserver.developer.huaweicloud.com/FileServer/getFile/spaceguides/a34/e2e/a49/faea1eb284a34e2ea4964f3ffe46d1e2.20260109011311.16549782486770233841626434535831:50570108011313:2421:586B81F59F42612E845D3CEAF364531E5614636F380C2A0DA0BDF6075BA90034.png?" width=1000px />

## 2.2 XXXX

<span style="color:rgb(216,27,68)">*//其他准备工作，正文删除这行*</span>

# 三、构建XX应用

## 3.1 创建云开发环境
<span style="color:rgb(216,27,68)">//涉及页面上的菜单点击，通过菜单层级展示，减少截图同时保证指引清晰，例如：**开发平台 > 云开发环境 > 容器**，正文删除这行</span>
<span style="color:rgb(216,27,68)">//涉及截图要保证分辨率清晰，推荐width=1200px，让读者看清楚图中关键信息，正文删除这行</span>

登录[华为开发者空间](https://developer.huaweicloud.com/space/home)，点击菜单 **开发平台 > 云开发环境 > 容器**，创建云开发环境容器版

![2.png](https://fileserver.developer.huaweicloud.com/FileServer/getFile/spaceguides/ec4/e93/9a1/71cb528da6ec4e939a19d11ed6d78b74.20251211030012.37420093962362025337029522467981:50561210030013:2421:F6C90A2D4AFE06C3BCD8788CB0D5FA5909F3C34046C5BAECAA11EBFF0A6EB80C.png?customIdMd=c63962d3edac4371bdbf9063f1fe50db)

## 3.2 部署项目代码
<span style="color:rgb(216,27,68)">//涉及项目代码部分，可以通过树形图形式说明项目结构，正文删除这行</span>
1）项目结构说明：
英语学习助手功能介绍
AddCustom
```bash
├── build.sh // 编译入口脚本
├── cmake
│ ├── config.cmake
│ ├── util // 算子工程编译所需脚本及公共编译文件存放目录
├── CMakeLists.txt // 算子工程的CMakeLists.txt
├── CMakePresets.json // 编译配置项

```
2）下载源码
<span style="color:rgb(216,27,68)">//源代码可以放到GitCode上，通过git下载到开发环境上，正文删除这行</span>

通过git下载源码到本地，代码仓地址：https://gitcode.com/sinat_41661654/english_ai_tutor.git

3）关键代码讲解
<span style="color:rgb(216,27,68)">//涉及到项目中的核心代码及需要自定义配置的，需要单独讲解，正文删除这行</span>
<span style="color:rgb(216,27,68)">//代码可通过菜单中的"插入代码"插入代码片段，配置文件修改可以有相应的截图指导，正文删除这行</span>
<span style="color:rgb(216,27,68)">//如涉及三方库安装，如pip install xxx等，必须指定版本号，如pip install mindspore==2.3.0而非pip install mindspore，否则后期容易出现版本依赖冲突。</span>

- **进行核函数的定义，并在核函数中调用算子类的Init和Process函数**
``` extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
{
      // 获取Host侧传入的Tiling参数
      GET_TILING_DATA(tiling_data, tiling);
      // 初始化算子类
      KernelAdd op;
      // 算子类的初始化函数，完成内存初始化相关工作
      op.Init(x, y, z, tiling_data.totalLength, tiling_data.tileNum);
      // 完成算子实现的核心逻辑
      op.Process();
}
```
- **在Notebook终端中通过vi编辑器修改AddCustom目录下CMakePresets.json中ASCEND_CANN_PACKAGE_PATH为CANN软件的安装目录，修改为：/usr/local/Ascend/ascend-toolkit/latest**
``` {
    ……
    "configurePresets": [
        {
                ……
                "ASCEND_CANN_PACKAGE_PATH": {
                    "type": "PATH",
                    "value": "/usr/local/Ascend/ascend-toolkit/latest"
                },
                ……
        }
    ]
}
```
![001.png](https://fileserver.developer.huaweicloud.com/FileServer/getFile/spaceguides/ec4/e93/9a1/71cb528da6ec4e939a19d11ed6d78b74.20251211030633.55310527998809190723635565728208:50561210030634:2421:434C36AB20B4E7AAE4049046EE98D82CE04F7CFC855DFFA17059DEB72D016868.png?customIdMd=4cb016f057634aa6b5bdf6378845c357)
4）运行调试
<span style="color:rgb(216,27,68)">//运行代码，要有执行命令行说明，并展示最终的运行结果，并配截图说明，正文删除这行</span>

在自定义算子包所在路径(build_out目录)下，执行如下命令，安装自定义算子包。
``` language
./custom_opp_<os>_<architecture>.run --install-path=<path>
```
|  参数 | 值  |
| ------------ | ------------ |
|  os | 表示操作系统，本例为openEuler  |
|  architecture |  硬件架构，本例为aarch64 |
|-path|算子安装目录，本例制定/home/service|

![002.png](https://fileserver.developer.huaweicloud.com/FileServer/getFile/spaceguides/ec4/e93/9a1/71cb528da6ec4e939a19d11ed6d78b74.20251211031023.93765049165122215480174108636697:50561210031024:2421:BFA0CF7D1C7620CA1A7AAA87E21F8D0981C664E90CDD1007F84596EA9DB04D9F.png?customIdMd=03d9ac906d564672b09f59d54806ceec)

# 四、释放资源
<span style="color:rgb(216,27,68)">//如果涉及云资源或者付费资源，需要说明资源释放，正文删除这行</span>

## 4.1 删除ECS弹性云服务器

进入ECS列表，点击全选按钮，点击“更多 -\> 删除”。

在对话框中选择“释放云服务器绑定的公网IP地址”和“删除云服务器挂载的数据盘”，点击“是”。

# 五、扩展资料说明
<span style="color:rgb(216,27,68)">//说明引用的资料或者扩展学习信息等，正文删除这行</span>

如果想了解更多手写体识别的内容可以访问：[https://yann.lecun.com/exdb/mnist/](https://yann.lecun.com/exdb/mnist/)

想了解更多关于PyTorch框架的可以访问：[https://pytorch.org/](https://pytorch.org/)

------------------------

# 附：MD使用规范：

1、标题
# 案例标题
# 一级目录标题
## 二级目录标题
### 三级目录标题
#### 四级目录标题
##### 五级目录标题

2、图片
通过菜单的中的"插入图片"插入即可

3、代码
行内代码：`spring-boot-bulking-kafka/src/main/resources/application.yaml`
代码块：
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>FunctionGraph动漫头像</title>
```
注意：代码相关的内容请使用代码格式，如网址链接、文件路径、类/方法名称等。

4、表格
|  两端对齐 | 对齐两端  |
| ------------ | ------------ |
|  1 | 2  |
|  3 |  4 |

5、超链接
[百度](https://www.baidu.com/)

6、文字颜色
<span style="color:rgb(216,27,68)">文字颜色调整</span>

7、其他
水平线： 
------------
段内换行
<br>
**加粗**
~~删除线~~
*斜体*
***加粗斜体***
> 引用 

