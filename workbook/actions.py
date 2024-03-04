import os

import requests

pbars = []
# ['0x11', '그리디', 'https://www.acmicpc.net/workbook/view/7320']
def parse_links():
  attrs = []
  with open('links.txt', encoding="UTF-8") as f:
    for line in f:
      attrs.append(line.strip().split(','))
  return attrs

def parse_category():
  category = []
  with open('problems.txt', encoding="UTF-8") as f:
    for line in f:
      category.append(line.strip().split(','))
  return category

def get_problem_info(workbook_url):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
  txt = requests.get(workbook_url, headers=headers).text
  pattern = '/problem/'
  ret = []
  while True:
    x = txt.find(pattern)
    if x == -1: break
    txt = txt[x+9:]
    prob_id, prob_name = '', ''
    i = 0
    while txt[i] in '0123456789':
      prob_id += txt[i]
      i += 1
    if not prob_id: continue
    i += 2
    while txt[i] != '<':
      prob_name += txt[i]
      i += 1
    ret.append((prob_id, prob_name))
  return ret

CATEGORY = ["연습 문제", "기본 문제✔", "기본 문제", "응용 문제✔", "응용 문제"]

# gen 0x00.md to 0x??.md, proper prob_id.py for each solution directory
def gen_ind_workbook(attrs, category):
  txt = ''
  chapter_idx = 0
  for attr in attrs:
    if len(attr) < 3: # No workbook
      pbars.append("")
      continue
    solution_num = 0
    solution_path = f'../{attr[0]}/solutions/'
    category_idx = 0
    problem_infos = get_problem_info(attr[2])
    prob_table = '| 문제 분류 | 문제 | 문제 제목 | 정답 코드 |\n| :--: | :--: | :--: | :--: |\n'
    for prob_id, prob_name in problem_infos:
      if prob_id in category[chapter_idx]:
        category_idx = category[chapter_idx].index(prob_id)
      file_path = solution_path + prob_id
      # os.remove(file_path+'.py')
      if not os.path.exists(file_path + '.py'):
        with open(file_path + '.py', 'w', encoding="UTF-8") as f:
          f.write(txt)
      try:
        codes = open(file_path + '.py', 'r', encoding="UTF-8").read()
      except: # EUC-KR -> UTF-8
        codes = open(file_path + '.py', 'r', encoding="EUC-KR").read()
        with open(file_path + '.py', 'w', encoding="UTF-8") as fw:
          fw.write(codes)
      if codes[:100] == txt[:100]:
        prob_table += f'| {CATEGORY[category_idx]} | {prob_id} | [{prob_name}](https://www.acmicpc.net/problem/{prob_id}) | - |\n'
      else:
        solution_num += 1
        code_attr = f'[정답 코드]({file_path.replace(" ", "%20")}.py)'
        MAX_DIFFERENT_SOLUTION = 9
        for i in range(1, MAX_DIFFERENT_SOLUTION+1):
          if os.path.exists(file_path+'_'+str(i)+'.py'):
            code_attr += f", [별해 {i}]({file_path+'_'+str(i)+'.py'})"
        prob_table += f'| {CATEGORY[category_idx]} | {prob_id} | [{prob_name}](https://www.acmicpc.net/problem/{prob_id}) | {code_attr} |\n'
    with open(attr[0]+'.md', 'w', encoding="UTF-8") as f:
      # progress bar
      f.write(f'# {attr[1]}\n\n')
      pbar = f'![100%](https://progress-bar.dev/{solution_num}/?scale={len(problem_infos)}&title=progress&width=500&color=babaca&suffix=/{len(problem_infos)})'
      pbars.append(pbar)
      f.write(pbar + '\n\n')
      f.write(f'[문제집 링크]({attr[2]})\n\n')
      f.write(prob_table)
    chapter_idx += 1

# ['0x11', '그리디', 'https://www.acmicpc.net/workbook/view/7320']
def gen_total_workbook(attrs):
  with open('../README.md', 'w', encoding="UTF-8") as f:
    f.write('''# 문제집
| 번호 | 주제 | 진행도 |
| :--: | :--: | :--: |\n''')
    for attr, pbar in zip(attrs, pbars):
      if len(attr) < 3: # No workbook
        f.write(f'| {attr[0]} | {attr[1]} | |\n')
      else:
        f.write(f'| {attr[0]} | [{attr[1]}](workbook/{attr[0].replace(" ", "%20")}.md) | {pbar} |\n')
    f.write('''## 출처
  - [바킹독 실전 알고리즘 강좌 블로그](https://blog.encrypted.gg/category/%EA%B0%95%EC%A2%8C/%EC%8B%A4%EC%A0%84%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
  - [바킹독 깃헙 리포지토리](https://github.com/encrypted-def/basic-algo-lecture)''')
attrs = parse_links()
category = parse_category()
gen_ind_workbook(attrs, category)
gen_total_workbook(attrs)