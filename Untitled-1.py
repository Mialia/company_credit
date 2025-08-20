from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

def check_files():
    required_files = ['company_credit.html', 'styles.css', 'script1.js']
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join(current_dir, file)):
            missing_files.append(file)
    
    if missing_files:
        print("错误：以下文件未找到：")
        for file in missing_files:
            print(f"- {file}")
        print(f"\n请确保所有文件都在此目录下：{current_dir}")
        return False
    return True

def start_server():
    try:
        # 切换到Python文件所在目录
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # 检查文件是否存在
        if not check_files():
            return
        
        # 设置服务器地址和端口
        server_address = ('', 8080)
        # 创建服务器
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print(f"\n服务器已启动在: http://localhost:8000/company_credit.html")
        print("当前目录:", os.getcwd())
        print("\n按 Ctrl+C 可以停止服务器")
        
        # 自动打开浏览器
        webbrowser.open('http://localhost:8080/company_credit.html')
        
        # 启动服务器
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == '__main__':
    start_server()
