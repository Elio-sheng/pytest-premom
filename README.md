### 项目说明

> 项目是一个基于 Python 和 Pytest 的自动化测试框架，它使用了 Page Object 模式来封装 HTTP 接口，并使用 YAML 文件来管理测试数据
> 这个项目的设计使得你可以轻松地添加新的接口和测试用例，只需要在相应的位置添加新的页面类、关键字或 YAML 文件即可。同时，通过使用 Page Object 模式和关键字驱动的方法，你的测试用例更易于理解和维护。

### 项目结构

- api 目录：这个目录包含了页面类，每个页面类封装了一个或多个 HTTP 接口。这些接口被封装成方法，可以被其他模块直接调用。

- common 目录：这个目录包含了一些公共的工具函数或类，可能被项目中的多个模块使用。

- core 目录：这个目录包含了对 requests 库的封装，以及关键字返回结果类。这些类和函数提供了发送 HTTP 请求和处理响应的基础功能。

- config 目录：这个目录包含了项目的配置文件，可能包括 API 的基础 URL、数据库连接信息等。

- data 目录：这个目录包含了测试数据文件，这些文件以 YAML 格式存储，可以被 conftest.py 文件读取并用于生成测试用例。

- operation 目录：这个目录包含了关键字的封装，每个关键字可能包含一个或多个 API 接口的调用。

- pytest.ini 文件：这个文件包含了 Pytest 的配置信息，如测试报告的格式、测试用例的搜索路径等。

- requirements.txt 文件：这个文件列出了项目的依赖包，可以通过 pip install -r requirements.txt 命令来安装这些依赖。

- testcases 目录：这个目录包含了所有的测试用例，每个测试用例可能包含一个或多个关键字的调用。

### pytest.ini 解析

- pytest.ini
  > pytest 框架的配置文件

```
[pytest]   # 这是配置文件的节标题，表示这个节包含了 Pytest 的配置选项。
addopts = -vqs    # addopts = -vqs：这个选项定义了默认的命令行参数。在这个例子中，-v 表示详细模式，-q 表示安静模式，-s 表示不捕获输出。这意味着 Pytest 将会打印详细的测试结果，但不会打印额外的信息，如测试进度。
testpaths = testcases # 这个选项定义了 Pytest 搜索测试用例的路径。在这个例子中，Pytest 将会在 testcases 目录下搜索测试用例。
markers =
  single: single api test page
  somkey: multiple api test page
  negative: abnormal test case

# markers这个选项定义了自定义的测试标记。在这个例子中，定义了三个测试标记：single：表示单个 API 测试页面的测试用例,smoke：表示冒烟测试的测试用例,negative：表示异常测试用例。
# 你可以在测试用例上使用这些标记，然后在运行测试时使用 -m 选项来选择要运行的测试用例，例如 pytest -m single 将会运行所有标记为 single 的测试用例。
```

### 项目操作文档

#### 项目简介

本项目是一个基于 Python 和 Pytest 的自动化测试框架，它使用了 Page Object 模式来封装 HTTP 接口，并使用 YAML 文件来管理测试数据。

#### 环境准备

1. **安装 Python**：请确保你的系统中已经安装了 Python 3.6 或更高版本。

2. **安装依赖**：在项目根目录下运行以下命令来安装项目的依赖包：

   ```bash
   pip install -r requirements.txt
   ```

#### 运行测试

> --testenv 是必填参数用来区分测试的环境

1. 在项目根目录下运行以下命令来运行所有的测试用例：

   ```bash
   python run.py --testenv=mtest
   ```

2. 如果你只想运行某一类测试用例，你可以使用 `-m` 选项来选择要运行的测试用例。例如，以下命令将会运行所有标记为 `single` 的测试用例：

   ```bash
   python run.py -m single --testenv=mtest
   ```

#### 添加新的接口

1. 在 api 目录下创建一个新的 Python 文件，这个文件将代表一个新的页面。

2. 在这个文件中，创建一个新的类来代表这个页面。这个类应该包含这个页面的所有接口，每个接口都被封装成一个方法。

3. 在 operation 目录下，创建一个新的 Python 文件来封装这个页面的关键字。

#### 添加新的测试用例

1. 在 data 目录下的 YAML 文件中添加新的测试数据。

2. 在 testcases 目录下创建一个新的 Python 文件，这个文件将包含新的测试用例。

3. 在这个文件中，使用 pytest.mark.parametrize 装饰器来定义新的测试用例。这个装饰器将会读取你在 YAML 文件中定义的测试数据，并将它们作为参数传递给测试用例。

#### data.yaml 格式

```
    The YAML file structure should be like this:
        TestXXX:                        # Class
          test_soco_xxx:                # Function
            parameters: paramA, paramB  # Parameter list
            values:
              - [valA1, valA2]          # Test cases
              - [valA2, valB2]
```
