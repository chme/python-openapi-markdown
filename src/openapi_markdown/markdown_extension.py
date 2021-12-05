import re
import markdown
import textwrap

from .renderer import render


class OpenAPIPreprocessor(markdown.preprocessors.Preprocessor):
    # Regular expression inspired from fenced_code and plantUML Markdown
    FENCED_BLOCK_RE = re.compile(
        r"""
        (?P<indent>[ ]*)
        (?P<fence>(?:~{3}|`{3}))[ ]*            # Opening ``` or ~~~
        (\{?\.?(openapi|swagger))[ ]*           # Optional {, and lang
        # args
        \s*(format=(?P<quot>"|')(?P<format>\w+)(?P=quot))?
        \s*(classes=(?P<quot1>"|')(?P<classes>[\w\s]+)(?P=quot1))?
        \s*(alt=(?P<quot2>"|')(?P<alt>.*?)(?P=quot2))?
        \s*(title=(?P<quot3>"|')(?P<title>.*?)(?P=quot3))?
        \s*(width=(?P<quot4>"|')(?P<width>[\w\s"']+%?)(?P=quot4))?
        \s*(height=(?P<quot5>"|')(?P<height>[\w\s"']+%?)(?P=quot5))?
        \s*(source=(?P<quot6>"|')(?P<source>.*?)(?P=quot6))?
        [ ]*
        }?[ ]*\n                                # Optional closing }
        (?P<code>.*?)(?<=\n)
        (?P=indent)(?P=fence)[ ]*$
        """,
        re.MULTILINE | re.DOTALL | re.VERBOSE,
    )
    # (?P<indent>[ ]*)(?P<fence>(?:~{3}|`{3}))[ ]*(\{?\.?(plant)?uml)[ ]*\n(?P<code>.*?)(?<=\n)(?P=indent)(?P=fence)$
    FENCED_CODE_RE = re.compile(
        r"(?P<fence>(?:~{4,}|`{4,})).*?(?P=fence)",
        re.MULTILINE | re.DOTALL | re.VERBOSE,
    )

    def __init__(self, md):
        super(OpenAPIPreprocessor, self).__init__(md)

    def run(self, lines):
        text = "\n".join(lines)
        idx = 0

        # loop until all text is parsed
        while idx < len(text):
            text1, idx1 = self._replace_block(text[idx:])
            text = text[:idx] + text1
            idx += idx1

        return text.split("\n")

    def _replace_block(self, text):
        # skip fenced code enclosing API specification
        m = self.FENCED_CODE_RE.search(text)
        if m:
            # check if before the fenced code there is a API specification
            m1 = self.FENCED_BLOCK_RE.search(text[: m.start()])
            if m1 is None:
                # no spec, skip this block of text
                return text, m.end() + 1

        # Parse configuration params
        m = self.FENCED_BLOCK_RE.search(text)
        if not m:
            return text, len(text)

        # Extract API specification
        code = m.group("code")

        # Convert API specification to Markdown
        openapi_md = self._render_openapi(code)

        # Indent generated Markdown
        openapi_md = textwrap.indent(openapi_md, m.group("indent"))

        return text[: m.start()] + openapi_md + text[m.end() :], m.start() + len(
            m.group("indent")
        ) + len(openapi_md)

    def _render_openapi(self, code):
        openapi = render(spec_string=code)
        return openapi


class OpenAPIExtension(markdown.Extension):
    def __init__(self, **kwargs):
        self.config = {
            "priority": [
                "35",
                "Extension priority. Higher values means the extension is "
                "applied sooner than others. "
                "Defaults to 35",
            ]
        }
        super(OpenAPIExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals=None):
        blockprocessor = OpenAPIPreprocessor(md)
        blockprocessor.config = self.getConfigs()
        md.preprocessors.register(
            blockprocessor, "openapi", int(blockprocessor.config["priority"])
        )


def makeExtension(**kwargs):
    return OpenAPIExtension(**kwargs)
