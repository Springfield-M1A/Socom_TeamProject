import sys
import os

def create_pyvenv_cfg():
    venv_dir = sys.prefix
    pyvenv_cfg_path = os.path.join(venv_dir, 'pyvenv.cfg')

    if not os.path.exists(pyvenv_cfg_path):
        with open(pyvenv_cfg_path, 'w') as f:
            f.write('[install]\n')
            f.write('prefix = {}\n'.format(venv_dir))

    print('pyvenv.cfg 생성이 완료되었습니다.')

if __name__ == '__main__':
    create_pyvenv_cfg()
