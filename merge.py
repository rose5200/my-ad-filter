from datetime import datetime
import requests

all_rules = []
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 订阅头部（拦截软件内展示名称）
header = f"""
! Title: 融合规则手机版-Jason
! Homepage: https://github.com/rose5200/my-ad-filter
! Description: HalfLife移动端+EasyList+EasyPrivacy+Cookie弹窗防护+自定义恶意跳转拦截
! Last modified: {now}
"""
all_rules.append(header)

# 全部上游规则（修复HalfLife 404失效链接）
source_list = [
    ("HalfLife 移动端", "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt"),
    ("EasyList", "https://easylist-downloads.adblockplus.org/easylist.txt"),
    ("EasyPrivacy", "https://easylist-downloads.adblockplus.org/easyprivacy.txt"),
    ("I don't care cookies", "https://www.i-dont-care-about-cookies.eu/abp/")
]

# 循环拉取所有上游规则
for name, url in source_list:
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        all_rules.append(f"\n! ========== {name} ==========\n")
        all_rules.append(resp.text)
    except Exception as err:
        all_rules.append(f"\n! 【拉取失败】{name} | {url} | 错误：{str(err)}\n")

# 个人专属跳转拦截黑名单
personal_rules = """
! ========== 个人自定义拦截黑名单 ==========
||viiraipj.com/h/$document,redirect
||ayhal.com/sm-click$document,redirect
"""
all_rules.append(personal_rules)

# 生成最终聚合规则文件
with open("mobile_final.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_rules))
