"""
旅行日志格式化工具
将包含日期、时间和内容的文本文件规范化为统一格式
"""
import re
import os
import sys
from datetime import datetime
from pathlib import Path

# 配置常量
DEFAULT_INPUT_FILE = "峡江红叶.txt"
SEPARATOR = "!"
DATE_PATTERN = re.compile(r'^(0\d|1[0-2])(-[0-2]\d|3[0-1])')
TIME_PATTERN = re.compile(r'^([0-1]\d|2[0-4])(:[0-5]\d)')


def generate_output_filename(input_path):
    """生成输出文件名：原文件名 + 规范化 + 日期"""
    base_name = Path(input_path).stem
    today_str = datetime.now().strftime("%Y-%m-%d")
    return f"{base_name}规范化{today_str}.txt"


def process_travel_log(input_fn, output_fn=None):
    """
    处理旅行日志文件，将其格式化为规范格式

    参数:
        input_fn: 输入文件路径
        output_fn: 输出文件路径（可选，默认自动生成）

    返回:
        bool: 处理是否成功
    """
    if not os.path.exists(input_fn):
        print(f"错误：找不到输入文件 '{input_fn}'")
        return False

    if output_fn is None:
        output_fn = generate_output_filename(input_fn)

    try:
        with open(input_fn, 'r', encoding='utf-8') as infile, \
             open(output_fn, 'w', encoding='utf-8') as outfile:

            last_date = ""
            is_first_record = True

            for line_num, line in enumerate(infile, 1):
                clean_line = line.strip()

                # 跳过空行
                if not clean_line:
                    continue

                # 匹配日期行
                date_match = DATE_PATTERN.match(clean_line)
                if date_match:
                    last_date = date_match.group(0)
                    continue

                # 匹配时间行
                time_match = TIME_PATTERN.match(clean_line)
                if time_match:
                    if not last_date:
                        print(f"警告：第 {line_num} 行发现时间但未找到对应日期")
                        continue

                    current_time = time_match.group(0)

                    # 非首条记录前先换行
                    if not is_first_record:
                        outfile.write("\n")

                    # 写入格式化的日期时间行
                    outfile.write(f"{last_date}{SEPARATOR}{current_time}{SEPARATOR}")
                    is_first_record = False

                # 其他内容行
                else:
                    if not is_first_record:
                        outfile.write(f"{clean_line}{SEPARATOR}")

            # 文件末尾添加换行
            if not is_first_record:
                outfile.write("\n")

        print(f"✓ 处理成功！输出文件: {output_fn}")
        return True

    except PermissionError:
        print(f"错误：没有权限访问文件 '{input_fn}' 或 '{output_fn}'")
        return False
    except Exception as e:
        print(f"错误：处理文件时发生异常 - {e}")
        return False


def main():
    """主函数：支持命令行参数或使用默认文件"""
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        input_file = DEFAULT_INPUT_FILE
        output_file = None

    success = process_travel_log(input_file, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()