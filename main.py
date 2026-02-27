import re
import os
from datetime import datetime

strfilename = "峡江红叶.txt"

def modifyText(input_fn):
    symbol = "!"
    # 1. 获取当前日期 (YYYY-MM-DD)
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # 2. 生成新文件名: 原文件名 + 规范化 + 日期
    base_name = os.path.splitext(input_fn)[0]
    output_fn = f"{base_name}规范化{today_str}.txt"

    # 正则表达式
    pattern1 = r'^(0\d|1[0-2])(-[0-2]\d|3[0-1])'
    pattern2 = r'^([0-1]\d|2[0-4])(:[0-5]\d)'

    try:
        with open(input_fn, 'r', encoding='utf-8') as file, \
             open(output_fn, 'w', encoding='utf-8') as fo:
            
            last_date = ""
            is_first_record = True

            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                # 1. 匹配到日期：仅更新状态，不换行也不写入
                date_match = re.match(pattern1, clean_line)
                if date_match:
                    last_date = date_match.group(0)
                    continue
                
                # 2. 匹配到时间：触发换行，开启属于该日期时间的新记录
                time_match = re.match(pattern2, clean_line)
                if time_match:
                    current_time = time_match.group(0)
                    # 如果不是文件开头的第一条记录，先换行
                    if not is_first_record:
                        fo.write("\n")
                    # 写入行首：日期!时间!
                    fo.write(f"{last_date}{symbol}{current_time}{symbol}")
                    is_first_record = False
                
                # 3. 杂项内容：直接拼接在当前行后面，并加上分隔符
                else:
                    # 只有在已经确定了时间点（即一行已经开始）后才写入杂项
                    if not is_first_record:
                        fo.write(f"{clean_line}{symbol}")
            
            # 文件末尾补一个换行
            if not is_first_record:
                fo.write("\n")
                    
        print(f"成功！已生成: {output_fn}")
        
    except FileNotFoundError:
        print(f"找不到输入文件: {input_fn}")

def main():
    modifyText(strfilename)

if __name__ == "__main__":
    main()