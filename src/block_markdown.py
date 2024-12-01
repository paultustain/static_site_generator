def markdown_to_blocks(markdown):
    inlines = markdown.split('\n\n')
    return [line.strip() for line in inlines if line.strip() != '']