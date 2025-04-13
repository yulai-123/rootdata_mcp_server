import requests
from bs4 import BeautifulSoup
import re
import json

def parse_project_description(script_content) -> dict[str, str]:
    # 解析项目数据
    projects = dict()
    
    # 正则表达式提取更多详细信息
    pattern = r'"([^"]+)。"'
    matches = re.findall(pattern, script_content, re.DOTALL)
    
    for match in matches:
        description = match
        
        # 从描述中提取项目名称（通常描述的开头部分是项目名称）
        name_parts = description.split("是")
        if len(name_parts) > 1:
            project_name = name_parts[0]
        else:
            project_name = description.split(" ")[0]
        
        projects[project_name.lower()] = description

    return projects

def parse_projects(html_content) -> list[str]:
    """从 rootdata 返回的 HTML 中解析出项目名称和介绍"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    projects = []
    
    # 查找每个项目行
    rows = soup.find_all('tr', role='row')
    for row in rows:
        # 跳过表头行
        if row.find('th'):
            continue
        
        # 找项目名称单元格
        name_cell = row.find('td', {'aria-colindex': '3'})
        if not name_cell:
            continue
        
        # 查找项目名称
        name_wrapper = name_cell.find('div', class_='d-flex name')
        if not name_wrapper:
            continue
            
        name_link = name_wrapper.find('a', class_='list_name')
        if not name_link:
            continue
            
        project_name = name_link.text.strip()
        link = name_link['href']
        
        # 查找项目描述
        project_description = ""
        tooltip = name_wrapper.find('div', role='tooltip')
        if tooltip:
            tooltip_html = str(tooltip)
            match = re.search(r'<!-- -->(.+?)</div>', tooltip_html, re.DOTALL)
            if match:
                project_description = match.group(1).strip()
        
        projects.append({
            'name': project_name,
            'description': project_description,
            'link': 'https://www.rootdata.com' + link
        })
    
    return projects


def fetch_rootdata_projects():
    # 定义请求头
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://www.rootdata.com/zh/Api',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
    
    url = 'https://www.rootdata.com/zh'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"请求失败，状态码: {response.status_code}"
    
    projects = parse_projects(response.text)
    
    return projects

# 执行函数并美化输出
if __name__ == "__main__":
    projects = fetch_rootdata_projects()
    if isinstance(projects, list):
        print(f"成功获取到 {len(projects)} 个热门项目:\n")
        for i, project in enumerate(projects):
            print(f"{i+1}. {project['name']}")
            print(f"   描述: {project['description']}\n"),
            print(f"   链接: {project['link']}\n")

    else:
        print(projects)  # 打印错误信息