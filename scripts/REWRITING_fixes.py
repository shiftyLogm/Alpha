import os

# Check existing file
def verifyFile(m_path) -> bool:
    return os.path.isfile(m_path)

# Increase a number to tile video:
def increaseTitle(m_path, file_n) -> str:
    