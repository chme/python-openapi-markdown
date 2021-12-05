import json

from jinja2 import Environment, PackageLoader
from prance import ResolvingParser


def filter_jsonify(value, indent=2):
    json_value = json.loads(value) if isinstance(value, str) else value
    return json.dumps(json_value, indent=indent)


def render(
    url=None,
    spec_string=None,
    backend="openapi-spec-validator",
    theme="mkdocs-material",
):
    parser = ResolvingParser(
        url=url,
        spec_string=spec_string,
        backend=backend,
        strict=False,
    )
    env = Environment(
        loader=PackageLoader("openapi_markdown", f"templates/{theme}"),
        autoescape=False,
        trim_blocks=True,
    )
    env.filters["jsonify"] = filter_jsonify

    template = env.get_template("api.md.j2")
    md = template.render(spec=parser.specification)
    return md
