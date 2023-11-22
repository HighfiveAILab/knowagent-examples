import httpx

query = "感冒怎麼辦"
custom_topk = 10
temperature = 0.0
endpoint = "knowagent-ana.laplace-ai.com"
url = f"https://{endpoint}/chat_stream?query={query}&custom_topk={custom_topk}&temperature={temperature}"

print(url)
with httpx.stream("GET", url, timeout=30) as r:
    for chunk in r.iter_text():
        print(chunk)
