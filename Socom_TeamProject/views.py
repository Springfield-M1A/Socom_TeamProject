from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def stock(request):
    return render(request, 'stock.html')

def prediction(request):
    return render(request, 'prediction.html')

def beginner(request):
    return render(request, 'beginner.html')

class Requirement:
    def __init__(self, name, installed):
        self.name = name
        self.installed = installed

def requirements(request):
    # requirements.txt 파일의 경로
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')

    # requirements.txt 파일을 읽어서 요구 사항 리스트 생성
    requirements = []
    with open(requirements_file, 'r') as file:
        for line in file:
            requirement_name = line.strip()
            installed = is_package_installed(requirement_name)  # 패키지 설치 여부 확인
            requirement = Requirement(name=requirement_name, installed=installed)
            requirements.append(requirement)

    # POST 요청인 경우, 요구 사항을 설치
    if request.method == 'POST':
        for requirement in requirements:
            if not requirement.installed:
                install_package(requirement.name)

        # 설치 후 요구 사항을 다시 확인
        for requirement in requirements:
            requirement.installed = is_package_installed(requirement.name)

    context = {
        'requirements': requirements
    }
    return render(request, 'requirements.html', context)


def is_package_installed(package_name):
    # 패키지 설치 여부 확인
    return True


def install_package(package_name):
    # 패키지 설치
    print(f"{package_name} has been installed.")

def copyrights(request):
    return render(request, 'copyrights.html')