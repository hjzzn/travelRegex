import re
import os
from datetime import datetime

strfilename="湘西秋韵.txt"

def modifyText(input_fn):
    symbol = "!"
    # 1. 获取当前日期 (例如: 2026-02-27)
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # 2. 生成新文件名: 原文件名 + 规范化 + 日期
    base_name = os.path.splitext(input_fn)[0]
    output_fn = f"{base_name}规范化{today_str}.txt"

    # 正则表达式
    pattern1 = r'^(0\d|1[0-2])(-[0-2]\d|3[0-1])'
    pattern2 = r'^([0-1]\d|2[0-4])(:[0-5]\d)'

    try:
        # 使用版本 B 的 with open 结构，更安全、更简洁
        with open(input_fn, 'r', encoding='utf-8') as file, \
             open(output_fn, 'w', encoding='utf-8') as fo:
            
            last_date = ""

            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                # 匹配日期
                date_match = re.match(pattern1, clean_line)
                if date_match:
                    last_date = date_match.group(0)
                    fo.write(f"{last_date}{symbol}\n")
                
                # 匹配时间 (补全日期)
                elif re.match(pattern2, clean_line):
                    fo.write(f"{last_date}{symbol}{clean_line}{symbol}\n")
                
                # 其他杂项
                else:
                    fo.write(f"{last_date}{symbol}{clean_line}\n")
                    
        print(f"成功！已生成: {output_fn}")
        
    except FileNotFoundError:
        print(f"找不到输入文件: {input_fn}")

def main():
    modifyText(strfilename)

if __name__ == "__main__":
    main()