import os

# HTML内容
html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<!-- 这里是之前提供的HTML内容 -->
</html>"""

# CSS内容
css_content = """/* 这里是之前提供的CSS内容 */"""

# JavaScript内容
js_content = """// 这里是之前提供的JavaScript内容"""

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建文件
def create_file(filename, content):
    file_path = os.path.join(current_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已创建文件: {filename}")

# 创建所需的文件
create_file('company_credit.html', html_content)
create_file('styles.css', css_content)
create_file('script.js', js_content)

print("\n所有文件已创建完成，现在可以运行 Untitled-1.py 了")