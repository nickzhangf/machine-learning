# coding:utf-8
import re

# 解析消息头，提取发言者昵称
def extractMsgHeader(line):
    normalLine = line.strip()
    # 如果包含时间格式，确定该行是消息头（包含昵称信息）
    pattern = re.compile(r'\d+-\d+-\d+')
    result = re.match(pattern, normalLine)
    if not result:
        return ''
    splitLine = normalLine.split(' ')[-1].strip()
    # 【学弱】有这种称号的，去除
    speaker = splitLine.split('】')[-1].strip()
    return speaker
