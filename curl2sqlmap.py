import uncurl
from sys import argv

arguments = []
sqlmap_command = "sqlmap" # Should it be $(which sqlmap)?

curlstring = argv[1]

context = uncurl.parse_context(curlstring)

if context.data:
    arguments.append(f'--data="{context.data}"')

if context.headers:
    headerlist = []
    for key, value in context.headers.items():

        if "user-agent" in key.lower():
            if ("--random-agent") in sqlmap_command:
                continue

        headerlist.append(f"{key}:{value}")
    headers_string = "\\n".join(headerlist)
    arguments.append(f'--headers="{headers_string}"')

if context.cookies:
    cookielist = []
    for key, value in context.cookies.items():
        cookielist.append(f"{key}={value}")
    arguments.append(f"--cookie=\"{'; '.join(cookielist)}\"")

command = f"{sqlmap_command} -u \"{context.url}\" {' '.join(arguments)}"

print()
print(command)
