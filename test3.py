# coding=gbk
str1 = """达伦台灯厂商接入华为平台智选品类项目

测试内容：
根据华为智选品类接入要求，进行测试，用例由华为提供，主要包含hilink认证基本用例、WiFi穿墙性能测试、产品KPI测试、长稳挂机测试、压力测试等

测试流程：
● 根据华为智选品类认证要求执行测试用例：
 1.使用 onmipeek  抓包工具对配网过程进行抓包
 2.搭建-70dbm  环境进行测试【WiFi穿墙性能测试】
 3.编写自动化脚本，进行【产品 kpi  测试】，大大降低测试人力
 4. 测试过程中使用SecureCRT串口工具保留模组日志，方便出现问题后更好追溯
● 按规范提交 BUG ，并协助开发人员复现定位问题
● 通过测试日报的形式汇报项目测试进展，同时测试过程中与华为认证测试人员沟通使得认证快速有效进展

经验总结：
此项目由于测试时间紧，为加快测试进度，减少沟通成本，故为驻场测试，通过此项目熟悉了照明类产品的功能特性，并且通过与达伦、华为很好的沟通使得项目进展顺利，另外在测试中使用不同工具，很大幅度提高了测试效率。"""

# str1.replace(" ", "、")
str2=str1.replace("	", "")
str3=str2.replace(" ", "")


print(str3)
