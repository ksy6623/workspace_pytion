import json
def convert_editthiscookie_to_netscape(json_path, output_path="cookies.txt"):
    with open(json_path, 'r', encoding='utf-8') as f:
        cookies = json.load(f)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for cookie in cookies:
            domain = cookie.get("domain", "")
            include_subdomain = "TRUE" if domain.startswith(".") else "FALSE"
            path = cookie.get("path", "/")
            secure = "TRUE" if cookie.get("secure", False) else "FALSE"
            expiry = int(cookie.get("expirationDate", 9999999999))
            name = cookie.get("name", "")
            value = cookie.get("value", "")
            f.write(f"{domain}\t{include_subdomain}\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n")

    print(f"✅ 변환 완료: {output_path}")

# 예시 사용
convert_editthiscookie_to_netscape("cookie.txt", "cookies.txt")