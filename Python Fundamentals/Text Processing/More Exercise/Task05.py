title = input()
content = input()

all_comments = []
comments = input()
while comments != "end of comments":
    all_comments.append(comments)
    comments = input()

print("<h1>")
print(f"    {title}")
print("</h1>")
print("<article>")
print(f"    {content}")
print("</article>")
for i in all_comments:
    print("<div>")
    print(f"    {i}")
    print("</div>")