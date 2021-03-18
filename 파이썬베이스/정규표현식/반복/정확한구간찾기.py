import re


text = "body {background-color: #fefbd8;}h1 {background-color: #0000ff;}div {background-color: #d0f4e6;}span {background-color: #f08970;}"

# 방법 1
print(re.findall(r"#[A-Fa-f0-9]{6}", text))
