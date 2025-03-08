import os
import subprocess
import unittest

import os
import subprocess
import pytest

def test_docker_build():
    # 設定 docker build 的 context 路徑（假設位於專案的 docker_context 資料夾）
    docker_context_path = os.path.join(os.path.dirname(__file__), "..", "dl-container", "GPU")
    
    # 組成 docker build 指令，-t 參數用來指定 tag 名稱
    command = f"docker build -t my-test-image {docker_context_path}"
    
    # 執行指令，並捕捉輸出與錯誤訊息
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # 若 returncode 不為 0，表示指令執行失敗，測試失敗並印出錯誤訊息
    assert result.returncode == 0, f"Docker build 失敗: {result.stderr}"

