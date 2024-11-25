import os

# Check existing file
def verifyFile(m_path) -> bool:
    return os.path.isfile(m_path)

# Increase a number to title video:
def increaseTitle(m_path, v_name, format) -> str:
    
    i = 1
    while os.path.exists(m_path + f"/{v_name}({i})" + f".{format}"):
        i += 1

    return f"{v_name}({i})"
