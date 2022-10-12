# pptx-ea-font
Fix the problem that the setting of East Asian fonts in python-pptx is invalid or incorrect.
修正python-pptx中东亚字体设置无效、不正确的问题。

## Installation

```
pip install pptx-ea-font
```

## Example

```Python
from pptx import Presentation
import pptx_ea_font


prs = Presentation('演示文稿.pptx')
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            text_frame = shape.text_frame
            for paragraph in text_frame.paragraphs:
                for run in paragraph.runs:
                    pptx_ea_font.set_font(run, '微软雅黑')
prs.save('字体修改版.pptx')
```