import os
import subprocess
from pathlib import Path

from pydantic import BaseModel
from typing import Any, Optional, List

TARGET_DIRS = {"src", "app", "apps", "service", "services", "backend", "api", "server"}
FILES = {"dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml", "readme.md", "readme.rst", "readme.txt"}
ESSENTIAL_EXTS = [".yml", ".yaml", ".json", ".properties", ".xml", ".toml", ".ini", ".env"]
CODE_EXTS = [".js", ".ts", ".py", ".rb", ".go", ".java", ".kt", ".scala"]
IGNORE_DIRS = {".git", "target", "build", "node_modules", "__pycache__"}

class GitCrawler(BaseModel):
    repo_url : Optional[Any] = None
    modules : Optional[List[str]] = None
    path : Optional[str] = None

    def clone_repo(self, base_dir="repos"):
        base_dir = Path(base_dir)
        base_dir.mkdir(exist_ok=True)

        name = self.repo_url.rstrip("/").split("/")[-1]
        repo_path = base_dir / name

        if repo_path.exists():
            return repo_path

        subprocess.run(
            ["git", "clone", "--depth", "1", self.repo_url, str(repo_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if not repo_path.exists():
            return None

        return repo_path

    def find_main_modules(self):
        repo_path = Path("repos") / self.repo_url.rstrip("/").split("/")[-1]
        if not repo_path: return []
        modules = []

        for item in os.scandir(repo_path):
            if item.is_dir() and item.name.lower() in TARGET_DIRS:
                modules.append(Path(item.path))

        self.modules = modules
        return None

    def crawl_module(self, module_path):
        collected = []

        for root, dirs, files in os.walk(module_path):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for f in files:
                f_lower = f.lower()
                if (f_lower in FILES or
                        any(f_lower.endswith(ext) for ext in ESSENTIAL_EXTS + CODE_EXTS)):
                    collected.append(Path(root) / f)

        return collected

    def crawl_repo_code(self):
        if not self.modules:
            self.find_main_modules()
        all_files = []

        for module in self.modules:
            all_files.extend(self.crawl_module(module))

        return all_files
