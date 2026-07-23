from datetime import datetime
import requests

all_rules = []
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 订阅头部（AdGuard/uBlock显示的订阅名称）
header = f"""
! Title: 融合规则手机版-Jason
! Homepage: https://github.com/rose5200/my-ad-filter
! Description: HalfLife+EasyList+EasyPrivacy+Cookie防护+自定义跳转拦截
! Last modified: {now}
"""
all_rules.append(header)

# 你指定的全部上游规则源
source_list = [
    ("HalfLife 移动端", "https://cdn.jsdelivr.net/gh/o0HalfLife0o/list@master/ad.txt"),
    ("EasyList", "https://easylist-downloads.adblockplus.org/easylist.txt"),
    ("EasyPrivacy", "https://easylist-downloads.adblockplus.org/easyprivacy.txt"),
    ("I don't care cookies", "https://www.i-dont-care-about-cookies.eu/abp/")
]

# 批量拉取每条上游规则
for name, url in source_list:
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        all_rules.append(f"\n! ========== {name} ==========\n")
        all_rules.append(resp.text)
    except Exception as err:
        all_rules.append(f"\n! 【拉取失败】{name} | {url} | 错误：{str(err)}\n")

# 你自己专属恶意跳转拦截规则
personal_rules = """
! ========== 个人自定义拦截黑名单 ==========
||viiraipj.com/h/$document,redirect
||ayhal.com/sm-click$document,redirect
"""
all_rules.append(personal_rules)

# 输出最终聚合文件
with open("mobile_final.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_rules))
