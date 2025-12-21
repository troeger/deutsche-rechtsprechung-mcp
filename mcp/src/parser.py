import re
from typing import Dict, Any, Optional

def parse_case_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    data = {
        'title': '',
        'metadata': {},
        'sections': {},
        'full_text': content
    }

    # 1. Extract Title
    if lines and lines[0].startswith('# '):
        data['title'] = lines[0][2:].strip()

    # 2. Extract Metadata
    # We look for the block between the title and the first separator '---'
    meta_start = 1
    meta_end = -1
    
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            meta_end = i
            break
    
    if meta_end != -1:
        meta_block = lines[meta_start:meta_end]
        for line in meta_block:
            # Regex to find **Key:** Value patterns
            # This handles multiple keys on one line separated by |
            # Pattern: **Key:** Value  (followed by | or end of line)
            matches = re.finditer(r'\*\*(.*?):\*\*\s*(.*?)(?=\s*\|\s*\*\*|$)', line)
            for match in matches:
                key = match.group(1).strip()
                val = match.group(2).strip()
                if key and val:
                    data['metadata'][key] = val
            
            # Special case for Vorinstanz or multiline fields that might not match the strict regex on subsequent lines
            # But the example shows "vorgehend ..." on new lines. 
            # For simplicity, we stick to the explicit keys for now.
            # If we need to capture "Vorinstanz" continuations, we'd need stateful parsing.
            # Looking at the example: 
            # **Vorinstanz:** vorgehend LG Aachen...
            # vorgehend AG Aachen...
            # The second line doesn't have a key. 
            # We will ignore unstructured lines in metadata for now or append to previous key if we wanted to be fancy.
            # Let's simple-parse for now.

    # 3. Extract Sections
    # Content after the first '---'
    if meta_end != -1:
        body_content = '\n'.join(lines[meta_end+1:])
        
        # Split by H2 headers "## "
        # We can use a regex split to keep the headers
        parts = re.split(r'^## (.*?)$', body_content, flags=re.MULTILINE)
        
        # parts[0] is text before first H2 (often empty or the separator)
        # parts[1] is first header, parts[2] is first body
        # parts[3] is second header, parts[4] is second body...
        
        for i in range(1, len(parts), 2):
            header = parts[i].strip()
            text = parts[i+1].strip()
            # Remove trailing '---' if it exists at end of section/file
            text = text.replace('\n---', '').strip()
            data['sections'][header] = text

    return data

if __name__ == "__main__":
    # Test with a dummy file if run directly (or user can import)
    pass
