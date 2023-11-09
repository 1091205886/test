# Doxygen简易教程

## 安装
```
sudo apt install doxygen 
sudo apt install doxygen-gui//可选
```

## 创建配置文件Doxygen和编译

```
cd $your_workspace
doxygen -g 
```
会默认生成一个叫Doxygen文件，用于后续编译

```
doxygen ./Doxygen 
```
在工程目录下运行就能生成文档，主要都在/html文件夹中，其中index.html为文档主界面

## 修改配置文件
**项目名称**

```
PROJECT_NAME           = "Your Project"
```

**项目版本号**
```
PROJECT_NUMBER = “1.0.0”
```

**语言环境**
```
OUTPUT_LANGUAGE        = English
```

**创建细分子目录**
对于有大量的源文件非常有用
```
CREATE_SUBDIRS         = YES
```

**包含STL类**
```
BUILTIN_STL_SUPPORT    = YES
```

**文件系统中大小写区分**
```
CASE_SENSE_NAMES       = YES
```

**对于使用typedef定义的进行文档化**
```
TYPEDEF_HIDES_STRUCT = YES
```

**输入源文件目录**
```
INPUT                  = $yourworkspace/src \
                         $yourworkspace/include ....
```

**为所有对象文件生成说明**
即使没有注释的对象也将文档化
```
EXTRACT_ALL            = YES
```
想要生成UML格式的类成员图
```
HAVE_DOT               = YES
UML_LOOK               = YES
RECURSIVE              = YES
```
**静态成员**
```
EXTRACT_STATIC         = YES
```

**私有成员**
```
EXTRACT_PRIVATE        = YES
```

**所有对象文档可以被交叉引用**
```
SOURCE_BROWSER         = YES
```

**生成依赖关系(全局函数、类方法)**
这里强调的是调用了谁
```
CALL_GRAPH             = YES
```

这里强调的是谁被调用
```
CALLER_GRAPH           = YES
```

