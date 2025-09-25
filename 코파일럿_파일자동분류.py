import os
import shutil
from pathlib import Path

def create_folders(base_path):
    """지정된 경로에 필요한 폴더들을 생성합니다."""
    folders = ['images', 'data', 'docs', 'archive']
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(downloads_path):
    """파일들을 확장자에 따라 해당 폴더로 이동합니다."""
    # 파일 확장자별 대상 폴더 매핑
    extension_mapping = {
        'images': ['.jpg', '.jpeg'],
        'data': ['.csv', '.xlsx'],
        'docs': ['.txt', '.doc', '.pdf', '.pptx', '.ppt'],
        'archive': ['.zip', '.exe', '.msi']
    }

    # 다운로드 폴더의 모든 파일 검사
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)
        
        # 파일이 아니면 건너뜀
        if not os.path.isfile(file_path):
            continue

        # 파일 확장자 확인
        file_ext = os.path.splitext(filename)[1].lower()
        
        # 확장자에 따른 대상 폴더 찾기
        for folder, extensions in extension_mapping.items():
            if file_ext in extensions:
                target_folder = os.path.join(downloads_path, folder)
                target_path = os.path.join(target_folder, filename)
                
                try:
                    shutil.move(file_path, target_path)
                    print(f"이동됨: {filename} -> {folder}/")
                except Exception as e:
                    print(f"오류 발생: {filename} 이동 실패 - {str(e)}")
                break

def main():
    # 다운로드 폴더 경로 설정
    downloads_path = r"C:\Users\student\Downloads"
    
    # 필요한 폴더 생성
    create_folders(downloads_path)
    
    # 파일 이동 실행
    move_files(downloads_path)
    print("파일 정리가 완료되었습니다.")

if __name__ == "__main__":
    main()