"""this to work with http requests"""
import requests


def tokenizer(target: str, prefix: str, suffix: str):
    """Write a function that takes a string target and returns all tokens that start
    with prefix and end with suffix, inclusive, and returns a list of items that match.
    """
    tokens = target.split()
    if prefix == "href":
        urls = []
        for token in tokens:
            if "href=" in token:
                start_index = token.find('href="') + len('href="')
                end_index = token.find('"', start_index)
                url = token[start_index:end_index]
                if url.strip():
                    urls.append(url)

        url_link = [url for url in urls if "http" in url]
        return url_link

    tokens_list = [
        token
        for token in tokens
        if token[0 : len(prefix)] == prefix and token[-(len(suffix)) :] == suffix
    ]
    return tokens_list


def get_url_list(urls="https://httpbin.org"):
    """Write a function that takes a url and returns a list of
    all urls that are only
    referenced as ahrefs in the response text.
    Make sure to use the tokenizer function you wrote in Part 1.
    """
    r = requests.get(urls, timeout=2)
    r.raise_for_status()
    data = r.text
    data = str(r.text)
    url_list = tokenizer(data, "href", '"')
    return url_list


def infix_to_postfix(infix_expression: str):
    """this func converts infix to postfix"""
    stack = []
    expression = []
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 4, ")": 4}

    for char in infix_expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                expression.append(stack.pop())
            if stack:
                stack.pop()
        elif char in priority:
            while stack and priority[char] <= priority[stack[-1]]:
                expression.append(stack.pop())
            stack.append(char)
        else:
            expression.append(char)

    while stack:
        expression.append(stack.pop())
    result = [i for i in expression if i not in ('(', ')')]
    return "".join(result)

if __name__ == "__main__":
    print(get_url_list())
    print(tokenizer("hey momo my name is mango", "m", "o"))
    print(infix_to_postfix(    '(a + b) ^ (c - d / q)'   ))
