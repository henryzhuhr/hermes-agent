#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
EN_ROOT = REPO_ROOT / "website" / "docs"
ZH_ROOT = REPO_ROOT / "website" / "docs.zh"
SPECIAL_ZH_ONLY = {"TRANSLATION_STATUS.md"}

PHASE1_FILES = {
    "index.md",
    "getting-started/_category_.json",
    "getting-started/installation.md",
    "getting-started/quickstart.md",
    "getting-started/termux.md",
    "getting-started/nix-setup.md",
    "getting-started/learning-path.md",
    "getting-started/updating.md",
    "user-guide/_category_.json",
    "user-guide/cli.md",
    "user-guide/configuration.md",
    "user-guide/sessions.md",
    "user-guide/profiles.md",
    "user-guide/git-worktrees.md",
    "user-guide/docker.md",
    "user-guide/security.md",
    "user-guide/checkpoints-and-rollback.md",
    "user-guide/features/_category_.json",
    "user-guide/features/overview.md",
    "user-guide/features/tools.md",
    "user-guide/features/skills.md",
    "user-guide/features/memory.md",
    "user-guide/features/context-files.md",
    "user-guide/features/mcp.md",
    "user-guide/features/acp.md",
    "user-guide/features/delegation.md",
    "user-guide/features/code-execution.md",
    "user-guide/features/voice-mode.md",
    "user-guide/features/personality.md",
    "user-guide/features/provider-routing.md",
    "user-guide/features/fallback-providers.md",
    "user-guide/messaging/_category_.json",
    "user-guide/messaging/index.md",
    "user-guide/messaging/telegram.md",
    "user-guide/messaging/discord.md",
    "user-guide/messaging/slack.md",
    "user-guide/messaging/whatsapp.md",
    "integrations/index.md",
    "integrations/providers.md",
    "reference/_category_.json",
    "reference/cli-commands.md",
    "reference/slash-commands.md",
    "reference/profile-commands.md",
    "reference/environment-variables.md",
    "reference/tools-reference.md",
    "reference/toolsets-reference.md",
    "reference/mcp-config-reference.md",
    "reference/faq.md",
}

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((/docs(?:\.zh)?/[^)\s\"']*)\)")
HTML_HREF_RE = re.compile(r"""href=["'](/docs(?:\.zh)?/[^"' ]*)["']""")


def route_to_relpath(route: str, prefix: str) -> Path:
    route = route.split("#", 1)[0].split("?", 1)[0]
    if route == prefix or route == prefix + "/":
        return Path("index.md")

    suffix = route[len(prefix) :].strip("/")
    if not suffix:
        return Path("index.md")
    if suffix.endswith(".md") or suffix.endswith(".json"):
        return Path(suffix)
    return Path(f"{suffix}.md")


def route_exists(root: Path, route: str, prefix: str) -> bool:
    rel = route_to_relpath(route, prefix)
    direct = root / rel
    if direct.exists():
        return True

    stem = rel.with_suffix("")
    section_dir = root / stem
    if (section_dir / "_category_.json").exists():
        return True
    if (section_dir / "index.md").exists():
        return True
    return False


def collect_links(text: str) -> set[str]:
    links = set()
    links.update(MARKDOWN_LINK_RE.findall(text))
    links.update(HTML_HREF_RE.findall(text))
    return links


def main() -> int:
    errors: list[str] = []

    zh_files = sorted(p for p in ZH_ROOT.rglob("*") if p.is_file())
    for rel in sorted(PHASE1_FILES):
        if not (ZH_ROOT / rel).exists():
            errors.append(f"Missing Phase 1 file: {rel}")

    checked = 0
    for path in zh_files:
        rel = path.relative_to(ZH_ROOT).as_posix()
        if rel in SPECIAL_ZH_ONLY:
            continue

        checked += 1
        en_path = EN_ROOT / rel
        if not en_path.exists():
            errors.append(f"Missing English source for zh file: {rel}")

        if path.suffix != ".md":
            continue

        text = path.read_text(encoding="utf-8")
        for route in sorted(collect_links(text)):
            if route.startswith("/docs.zh/") or route == "/docs.zh":
                if not route_exists(ZH_ROOT, route, "/docs.zh"):
                    errors.append(f"Broken /docs.zh link in {rel}: {route}")
            elif route.startswith("/docs/") or route == "/docs":
                if not route_exists(EN_ROOT, route, "/docs"):
                    errors.append(f"Broken /docs link in {rel}: {route}")

    if errors:
        print("docs.zh validation failed:\n")
        for item in errors:
            print(f"- {item}")
        return 1

    print(
        f"docs.zh validation passed: {checked} translated source files checked, "
        f"{len(PHASE1_FILES)} Phase 1 targets present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
