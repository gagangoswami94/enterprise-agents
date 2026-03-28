#!/usr/bin/env python3
"""
agents -- Enterprise AI Agent CLI

Lint, convert, and install AI agent specs across coding tools.

Usage:
  python agents.py lint [file]          Validate agent files
  python agents.py convert [--tool T]   Generate integration files
  python agents.py install [--tool T]   Copy agents to tool directories
  python agents.py list [--cat C]       List available agents
"""

import argparse
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path(__file__).parent.resolve()
INTEGRATIONS = REPO / "integrations"
TODAY = date.today().isoformat()

AGENT_DIRS = [
    "academic", "design", "engineering", "game-development", "marketing",
    "paid-media", "sales", "product", "project-management", "testing",
    "support", "spatial-computing", "specialized",
    "cloud", "cybersecurity", "data-science", "ecommerce", "fintech",
    "low-code", "content", "customer-success", "executive", "finance",
    "healthcare", "legal", "operations", "people-ops", "solopreneur", "strategy",
]

ALL_TOOLS = [
    "claude-code", "copilot", "antigravity", "gemini-cli",
    "opencode", "openclaw", "cursor", "aider", "windsurf", "qwen", "kimi",
]

OPENCODE_COLORS = {
    "cyan": "#00FFFF", "blue": "#3498DB", "green": "#2ECC71",
    "red": "#E74C3C", "purple": "#9B59B6", "orange": "#F39C12",
    "teal": "#008080", "indigo": "#6366F1", "pink": "#E84393",
    "gold": "#EAB308", "amber": "#F59E0B", "neon-green": "#10B981",
    "neon-cyan": "#06B6D4", "metallic-blue": "#3B82F6", "yellow": "#EAB308",
    "violet": "#8B5CF6", "rose": "#F43F5E", "lime": "#84CC16",
    "gray": "#6B7280", "fuchsia": "#D946EF",
}

REQUIRED_FIELDS = ["name", "description", "color"]
RECOMMENDED_SECTIONS = ["identity", "core mission", "critical rules"]

# ---------------------------------------------------------------------------
# Terminal colors (graceful fallback when stdout is not a tty)
# ---------------------------------------------------------------------------
USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR", "") == "" and os.environ.get("TERM", "") != "dumb"

def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text

def ok(msg: str)   -> None: print(_c("0;32", f"[OK]  {msg}"))
def warn(msg: str) -> None: print(_c("1;33", f"[!!]  {msg}"))
def err(msg: str)  -> None: print(_c("0;31", f"[ERR] {msg}"), file=sys.stderr)
def info(msg: str) -> None: print(_c("1",    f"\n{msg}"))

# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------
def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Return (fields_dict, body_str). Returns ({}, full_text) if no frontmatter."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text

    fields: dict = {}
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        m = re.match(r'^(\w[\w-]*):\s*(.*)$', lines[i])
        if m:
            key, val = m.group(1), m.group(2).strip().strip("'\"")
            fields[key] = val
        i += 1

    body = "".join(lines[i + 1:]) if i + 1 < len(lines) else ""
    return fields, body


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def resolve_color(color: str) -> str:
    c = color.strip().lower()
    mapped = OPENCODE_COLORS.get(c, c)
    if re.match(r'^#?[0-9a-fA-F]{6}$', mapped):
        hex6 = mapped.lstrip('#')
        return f"#{hex6.upper()}"
    return "#6B7280"


def iter_agents():
    """Yield (Path, fields, body) for every valid agent file."""
    for dirname in AGENT_DIRS:
        d = REPO / dirname
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*.md")):
            fields, body = parse_frontmatter(f)
            if not fields or not fields.get("name"):
                continue
            yield f, fields, body

# ---------------------------------------------------------------------------
# LINT
# ---------------------------------------------------------------------------
def cmd_lint(args) -> int:
    if args.file:
        targets = [Path(args.file).resolve()]
    else:
        targets = [f for f, _, _ in iter_agents()]

    errors = 0
    warnings = 0

    for path in targets:
        fields, body = parse_frontmatter(path)
        rel = path.relative_to(REPO)
        file_ok = True

        if not fields:
            err(f"{rel}: missing YAML frontmatter")
            errors += 1
            continue

        for field in REQUIRED_FIELDS:
            if not fields.get(field):
                err(f"{rel}: missing required field '{field}'")
                errors += 1
                file_ok = False

        body_lower = body.lower()
        for section in RECOMMENDED_SECTIONS:
            if section not in body_lower:
                warn(f"{rel}: recommended section '{section}' not found")
                warnings += 1

        if file_ok:
            ok(f"{rel}")

    print(f"\n{len(targets)} file(s) checked — {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0

# ---------------------------------------------------------------------------
# CONVERT helpers
# ---------------------------------------------------------------------------
def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def convert_antigravity(f: Path, fields: dict, body: str) -> None:
    slug = f"enterprise-{slugify(fields['name'])}"
    out = INTEGRATIONS / "antigravity" / slug / "SKILL.md"
    write(out, f"---\nname: {slug}\ndescription: {fields['description']}\nrisk: low\nsource: community\ndate_added: '{TODAY}'\n---\n{body}")


def convert_gemini_cli(f: Path, fields: dict, body: str) -> None:
    slug = slugify(fields['name'])
    out = INTEGRATIONS / "gemini-cli" / "skills" / slug / "SKILL.md"
    write(out, f"---\nname: {slug}\ndescription: {fields['description']}\n---\n{body}")


def convert_opencode(f: Path, fields: dict, body: str) -> None:
    slug = slugify(fields['name'])
    color = resolve_color(fields.get('color', 'gray'))
    out = INTEGRATIONS / "opencode" / "agents" / f"{slug}.md"
    write(out, f"---\nname: {fields['name']}\ndescription: {fields['description']}\nmode: subagent\ncolor: '{color}'\n---\n{body}")


def convert_cursor(f: Path, fields: dict, body: str) -> None:
    slug = slugify(fields['name'])
    out = INTEGRATIONS / "cursor" / "rules" / f"{slug}.mdc"
    write(out, f"---\ndescription: {fields['description']}\nglobs: \"\"\nalwaysApply: false\n---\n{body}")


def convert_openclaw(f: Path, fields: dict, body: str) -> None:
    slug = slugify(fields['name'])
    outdir = INTEGRATIONS / "openclaw" / slug

    soul_keywords = {"identity", "communication", "style", "critical rule", "rules you must follow"}
    soul_sections: list[str] = []
    agents_sections: list[str] = []
    current: list[str] = []
    current_target = "agents"

    for line in body.splitlines(keepends=True):
        if line.startswith("## "):
            if current:
                (soul_sections if current_target == "soul" else agents_sections).extend(current)
                current = []
            lower = line.lower()
            current_target = "soul" if any(kw in lower for kw in soul_keywords) else "agents"
        current.append(line)

    if current:
        (soul_sections if current_target == "soul" else agents_sections).extend(current)

    write(outdir / "SOUL.md", "".join(soul_sections))
    write(outdir / "AGENTS.md", "".join(agents_sections))

    emoji = fields.get("emoji", "")
    vibe = fields.get("vibe", "")
    if emoji and vibe:
        write(outdir / "IDENTITY.md", f"# {emoji} {fields['name']}\n{vibe}\n")
    else:
        write(outdir / "IDENTITY.md", f"# {fields['name']}\n{fields['description']}\n")


def convert_qwen(f: Path, fields: dict, body: str) -> None:
    slug = slugify(fields['name'])
    out = INTEGRATIONS / "qwen" / "agents" / f"{slug}.md"
    tools_line = f"\ntools: {fields['tools']}" if fields.get("tools") else ""
    write(out, f"---\nname: {slug}\ndescription: {fields['description']}{tools_line}\n---\n{body}")


def convert_kimi(f: Path, fields: dict, body: str) -> None:
    slug = slugify(fields['name'])
    outdir = INTEGRATIONS / "kimi" / slug
    write(outdir / "agent.yaml", f"version: 1\nagent:\n  name: {slug}\n  extend: default\n  system_prompt_path: ./system.md\n")
    write(outdir / "system.md", f"# {fields['name']}\n\n{fields['description']}\n\n{body}")


AIDER_HEADER = """\
# Enterprise Agents -- AI Agent Conventions
#
# To activate an agent, reference it by name in your Aider session, e.g.:
#   "Use the Backend Architect agent to review this service."
#
# Generated by agents.py convert -- do not edit manually.

"""

WINDSURF_HEADER = """\
# Enterprise Agents -- AI Agent Rules for Windsurf
#
# Full roster of specialized AI agents.
# Reference an agent by name in your Windsurf conversation to activate it.
#
# Generated by agents.py convert -- do not edit manually.

"""


def cmd_convert(args) -> int:
    tool = args.tool or "all"

    valid = set(ALL_TOOLS) | {"all"}
    valid.discard("claude-code")
    valid.discard("copilot")
    if tool not in valid:
        err(f"Unknown tool '{tool}'. Valid: {', '.join(sorted(valid))}")
        return 1

    converters = {
        "antigravity": convert_antigravity,
        "gemini-cli":  convert_gemini_cli,
        "opencode":    convert_opencode,
        "cursor":      convert_cursor,
        "openclaw":    convert_openclaw,
        "qwen":        convert_qwen,
        "kimi":        convert_kimi,
    }

    tools_to_run = list(converters.keys()) + ["aider", "windsurf"] if tool == "all" else [tool]
    count = 0

    aider_buf = AIDER_HEADER
    windsurf_buf = WINDSURF_HEADER

    for t in tools_to_run:
        info(f"Converting: {t}")
        n = 0
        for f, fields, body in iter_agents():
            if t in converters:
                converters[t](f, fields, body)
                n += 1
            elif t == "aider":
                aider_buf += f"\n---\n\n## {fields['name']}\n\n> {fields['description']}\n\n{body}"
                n += 1
            elif t == "windsurf":
                windsurf_buf += f"\n{'=' * 80}\n## {fields['name']}\n{fields['description']}\n{'=' * 80}\n\n{body}\n"
                n += 1
        ok(f"{t}: {n} agents")
        count += n

    # Write single-file outputs
    if tool in ("all", "aider"):
        out = INTEGRATIONS / "aider" / "CONVENTIONS.md"
        write(out, aider_buf)
        ok(f"aider: wrote {out.relative_to(REPO)}")

    if tool in ("all", "windsurf"):
        out = INTEGRATIONS / "windsurf" / ".windsurfrules"
        write(out, windsurf_buf)
        ok(f"windsurf: wrote {out.relative_to(REPO)}")

    # Gemini CLI manifest
    if tool in ("all", "gemini-cli"):
        manifest = INTEGRATIONS / "gemini-cli" / "gemini-extension.json"
        write(manifest, '{\n  "name": "enterprise-agents",\n  "version": "1.0.0"\n}\n')

    print(f"\nDone. {count} conversions across {len(tools_to_run)} tool(s).")
    return 0

# ---------------------------------------------------------------------------
# INSTALL helpers
# ---------------------------------------------------------------------------
def copy_dir(src: Path, dest: Path, pattern: str = "*.md", flat: bool = True) -> int:
    """Copy matching files from src into dest. Returns count."""
    dest.mkdir(parents=True, exist_ok=True)
    n = 0
    if flat:
        for f in src.glob(pattern):
            if f.is_file():
                shutil.copy2(f, dest / f.name)
                n += 1
    return n


def install_claude_code() -> None:
    dest = Path.home() / ".claude" / "agents"
    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for f, fields, body in iter_agents():
        shutil.copy2(f, dest / f.name)
        count += 1
    ok(f"Claude Code: {count} agents -> {dest}")


def install_copilot() -> None:
    dest_gh = Path.home() / ".github" / "agents"
    dest_cp = Path.home() / ".copilot" / "agents"
    count = 0
    for f, fields, body in iter_agents():
        dest_gh.mkdir(parents=True, exist_ok=True)
        dest_cp.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest_gh / f.name)
        shutil.copy2(f, dest_cp / f.name)
        count += 1
    ok(f"Copilot: {count} agents -> {dest_gh} + {dest_cp}")


def _require_integration(tool_dir: str) -> Path | None:
    p = INTEGRATIONS / tool_dir
    if not p.is_dir():
        err(f"integrations/{tool_dir} missing — run: python agents.py convert --tool {tool_dir}")
        return None
    return p


def install_antigravity() -> None:
    src = _require_integration("antigravity")
    if not src: return
    dest = Path.home() / ".gemini" / "antigravity" / "skills"
    count = 0
    for d in src.iterdir():
        if d.is_dir():
            t = dest / d.name
            t.mkdir(parents=True, exist_ok=True)
            shutil.copy2(d / "SKILL.md", t / "SKILL.md")
            count += 1
    ok(f"Antigravity: {count} skills -> {dest}")


def install_gemini_cli() -> None:
    src = _require_integration("gemini-cli")
    if not src: return
    dest = Path.home() / ".gemini" / "extensions" / "enterprise-agents"
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src / "gemini-extension.json", dest / "gemini-extension.json")
    skills_src = src / "skills"
    count = 0
    if skills_src.is_dir():
        for d in skills_src.iterdir():
            if d.is_dir():
                t = dest / "skills" / d.name
                t.mkdir(parents=True, exist_ok=True)
                shutil.copy2(d / "SKILL.md", t / "SKILL.md")
                count += 1
    ok(f"Gemini CLI: {count} skills -> {dest}")


def install_opencode() -> None:
    src = _require_integration("opencode")
    if not src: return
    dest = Path.cwd() / ".opencode" / "agents"
    n = copy_dir(src / "agents", dest)
    ok(f"OpenCode: {n} agents -> {dest}")
    warn("OpenCode: project-scoped — run from your project root")


def install_openclaw() -> None:
    src = _require_integration("openclaw")
    if not src: return
    dest = Path.home() / ".openclaw" / "enterprise-agents"
    count = 0
    for d in src.iterdir():
        if d.is_dir():
            t = dest / d.name
            t.mkdir(parents=True, exist_ok=True)
            for fname in ("SOUL.md", "AGENTS.md", "IDENTITY.md"):
                if (d / fname).exists():
                    shutil.copy2(d / fname, t / fname)
            count += 1
    ok(f"OpenClaw: {count} workspaces -> {dest}")


def install_cursor() -> None:
    src = _require_integration("cursor")
    if not src: return
    dest = Path.cwd() / ".cursor" / "rules"
    n = copy_dir(src / "rules", dest, pattern="*.mdc")
    ok(f"Cursor: {n} rules -> {dest}")
    warn("Cursor: project-scoped — run from your project root")


def install_aider() -> None:
    src = INTEGRATIONS / "aider" / "CONVENTIONS.md"
    if not src.exists():
        err("integrations/aider/CONVENTIONS.md missing — run: python agents.py convert --tool aider")
        return
    dest = Path.cwd() / "CONVENTIONS.md"
    if dest.exists():
        warn(f"Aider: {dest} already exists — remove it to reinstall")
        return
    shutil.copy2(src, dest)
    ok(f"Aider: installed -> {dest}")
    warn("Aider: project-scoped — run from your project root")


def install_windsurf() -> None:
    src = INTEGRATIONS / "windsurf" / ".windsurfrules"
    if not src.exists():
        err("integrations/windsurf/.windsurfrules missing — run: python agents.py convert --tool windsurf")
        return
    dest = Path.cwd() / ".windsurfrules"
    if dest.exists():
        warn(f"Windsurf: {dest} already exists — remove it to reinstall")
        return
    shutil.copy2(src, dest)
    ok(f"Windsurf: installed -> {dest}")
    warn("Windsurf: project-scoped — run from your project root")


def install_qwen() -> None:
    src = _require_integration("qwen")
    if not src: return
    dest = Path.cwd() / ".qwen" / "agents"
    n = copy_dir(src / "agents", dest)
    ok(f"Qwen Code: {n} agents -> {dest}")
    warn("Qwen Code: project-scoped — run from your project root")


def install_kimi() -> None:
    src = _require_integration("kimi")
    if not src: return
    dest = Path.home() / ".config" / "kimi" / "agents"
    count = 0
    for d in src.iterdir():
        if d.is_dir():
            t = dest / d.name
            t.mkdir(parents=True, exist_ok=True)
            for fname in ("agent.yaml", "system.md"):
                if (d / fname).exists():
                    shutil.copy2(d / fname, t / fname)
            count += 1
    ok(f"Kimi Code: {count} agents -> {dest}")


INSTALLERS = {
    "claude-code": install_claude_code,
    "copilot":     install_copilot,
    "antigravity": install_antigravity,
    "gemini-cli":  install_gemini_cli,
    "opencode":    install_opencode,
    "openclaw":    install_openclaw,
    "cursor":      install_cursor,
    "aider":       install_aider,
    "windsurf":    install_windsurf,
    "qwen":        install_qwen,
    "kimi":        install_kimi,
}

DETECTORS = {
    "claude-code": lambda: (Path.home() / ".claude").is_dir(),
    "copilot":     lambda: shutil.which("code") or (Path.home() / ".github").is_dir(),
    "antigravity": lambda: (Path.home() / ".gemini" / "antigravity").is_dir(),
    "gemini-cli":  lambda: shutil.which("gemini") or (Path.home() / ".gemini").is_dir(),
    "opencode":    lambda: shutil.which("opencode") or (Path.home() / ".config" / "opencode").is_dir(),
    "openclaw":    lambda: shutil.which("openclaw") or (Path.home() / ".openclaw").is_dir(),
    "cursor":      lambda: shutil.which("cursor") or (Path.home() / ".cursor").is_dir(),
    "aider":       lambda: bool(shutil.which("aider")),
    "windsurf":    lambda: shutil.which("windsurf") or (Path.home() / ".codeium").is_dir(),
    "qwen":        lambda: shutil.which("qwen") or (Path.home() / ".qwen").is_dir(),
    "kimi":        lambda: bool(shutil.which("kimi")),
}


def cmd_install(args) -> int:
    tool = args.tool

    if tool and tool not in INSTALLERS:
        err(f"Unknown tool '{tool}'. Valid: {', '.join(ALL_TOOLS)}")
        return 1

    if tool:
        INSTALLERS[tool]()
    else:
        info("Scanning for installed tools...")
        detected = [t for t, detect in DETECTORS.items() if detect()]
        if not detected:
            warn("No supported tools detected. Use --tool to install for a specific tool.")
            print(f"  Available: {', '.join(ALL_TOOLS)}")
            return 0
        for t in detected:
            INSTALLERS[t]()

    return 0

# ---------------------------------------------------------------------------
# LIST
# ---------------------------------------------------------------------------
def cmd_list(args) -> int:
    cat_filter = args.cat

    rows: list[tuple[str, str, str]] = []
    for f, fields, _ in iter_agents():
        cat = f.parent.name if f.parent != REPO else "root"
        if cat_filter and cat != cat_filter:
            continue
        rows.append((cat, fields.get("name", "?"), fields.get("description", "")))

    if not rows:
        warn("No agents found.")
        return 0

    rows.sort()
    col_cat  = max(len(r[0]) for r in rows)
    col_name = max(len(r[1]) for r in rows)

    print(f"\n{'Category':<{col_cat}}  {'Name':<{col_name}}  Description")
    print("-" * (col_cat + col_name + 40))
    for cat, name, desc in rows:
        print(f"{cat:<{col_cat}}  {name:<{col_name}}  {desc}")

    print(f"\n{len(rows)} agent(s)")
    return 0

# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(
        prog="agents",
        description="Enterprise Agents CLI — lint, convert, install AI agent specs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python agents.py lint
  python agents.py lint engineering/engineering-backend-architect.md
  python agents.py convert
  python agents.py convert --tool cursor
  python agents.py install
  python agents.py install --tool claude-code
  python agents.py list
  python agents.py list --cat engineering
""",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # lint
    p_lint = sub.add_parser("lint", help="Validate agent files")
    p_lint.add_argument("file", nargs="?", help="Specific file to lint (default: all)")
    p_lint.set_defaults(func=cmd_lint)

    # convert
    p_conv = sub.add_parser("convert", help="Generate tool-specific integration files")
    p_conv.add_argument("--tool", metavar="TOOL", help=f"Tool to convert for (default: all). One of: {', '.join(t for t in ALL_TOOLS if t not in ('claude-code','copilot'))}")
    p_conv.set_defaults(func=cmd_convert)

    # install
    p_inst = sub.add_parser("install", help="Copy agents to tool config directories")
    p_inst.add_argument("--tool", metavar="TOOL", help=f"Tool to install for (default: auto-detect). One of: {', '.join(ALL_TOOLS)}")
    p_inst.set_defaults(func=cmd_install)

    # list
    p_list = sub.add_parser("list", help="List available agents")
    p_list.add_argument("--cat", metavar="CATEGORY", help="Filter by category directory name")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
