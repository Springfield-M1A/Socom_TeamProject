import platform
import subprocess

# 시스템 운영 체제 확인
os_name = platform.system()

# 필요한 패키지 리스트 정의
if os_name == "Windows":
    packages = ["beautifulsoup4", "pandas", "pywin32", "sqlite3", "flask"]
elif os_name == "Darwin":  # Mac
    packages = ["beautifulsoup4", "pandas", "sqlite3", "flask"]
elif os_name == "Linux":
    packages = ["beautifulsoup4", "pandas", "libpq-dev", "sqlite3", "flask"]

# 패키지 설치
for package in packages:
    subprocess.run(["pip", "install", package])

import sqlite3
