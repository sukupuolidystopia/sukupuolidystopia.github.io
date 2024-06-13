import re
import markdown

def convert_markdown_links_to_html_citations(markdown_content):
    # Regular expression to find markdown links
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
    citations = []
    citation_template = '<a href="{url}" target="_blank" id="cite-{index}">[{index}]</a>'

    def link_replacer(match):
        text = match.group(1)
        url = match.group(2)
        citation_index = len(citations) + 1
        citation = f'<li id="cite-{citation_index}"><a href="{url}" target="_blank">{url}</a></li>'
        citations.append(citation)
        return f'{text}<sup>{citation_template.format(url=url, index=citation_index)}</sup>'

    # Replace links in the content
    processed_content = link_pattern.sub(link_replacer, markdown_content)

    # Convert markdown to HTML
    html_content = markdown.markdown(processed_content)

    # Generate the citation list HTML
    citations_html = '<h2>References</h2><ol>' + ''.join(citations) + '</ol>'

    # Append citations to the processed content
    final_content = html_content + '\n\n' + citations_html
    return final_content

# Read markdown content from a file
with open('README.md', 'r',  encoding="utf8") as file:
    markdown_content = file.read()

# Convert markdown links to HTML citations and convert markdown to HTML
html_content = convert_markdown_links_to_html_citations(markdown_content)

# Write the converted content to a new file
with open('output.html', 'w',  encoding="utf8") as file:
    file.write(html_content)

print("Conversion complete. Check the output.html file.")
