# Backend Code Scanner

Java代码坏味道检测工具，三层架构8个规则。

## 规则列表

| 规则 | 类别 | 说明 |
|------|------|------|
| EMPTY_LOOP | 结构层 | 空循环体检测 |
| DEEP_NESTING | 结构层 | 嵌套深度>3告警 |
| GOD_CLASS | 结构层 | 屎山指数GCI评分 |
| WORTHLESS_LOOP | 数据流层 | 循环不变量检测 |
| PORT_ALIGN | 配置层 | 端口暴露检测 |
| BANDWIDTH_ALIGN | 配置层 | 带宽风险检测 |
| TIMEOUT_ALIGN | 配置层 | 超时配置检测 |
| POOL_ALIGN | 配置层 | 连接池配置检测 |

## 快速开始

```bash
java -jar backend-code-scanner-0.1.01-jar-with-dependencies.jar 你的文件.java
