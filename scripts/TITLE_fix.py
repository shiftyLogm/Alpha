from re import sub

def fix_title_video(t_v: str) -> str:
     return sub(r'[^a-zA-Z0-9\s]', '', t_v)