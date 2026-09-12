"""
Book Writer — CLI Runner
=========================
Ponto de entrada para rodar o pipeline de escrita.

Uso:
  $ cd ~/code/feproduto
  $ python -m book_writer.run --chapter 7
  $ python -m book_writer.run --chapter 7 --max-revisions 2
  $ python -m book_writer.run --chapter 4  # completar cap 4

Requer:
  pip install langgraph langchain-core langchain-openai
  DEEPSEEK_API_KEY no ambiente ou ~/.hermes/.env
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Garante que o projeto está no path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def main():
    parser = argparse.ArgumentParser(
        description="Book Writer — Pipeline multiagente para escrita de livro"
    )
    parser.add_argument(
        "--chapter", "-c",
        type=int,
        default=7,
        help="Número do capítulo a escrever (1-11). Default: 1 (AI Trap)",
    )
    parser.add_argument(
        "--max-revisions", "-r",
        type=int,
        default=3,
        help="Máximo de ciclos de revisão. Default: 3",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Lista os capítulos disponíveis e sai",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Modo silencioso (menos output)",
    )
    parser.add_argument(
        "--brief", "-b",
        type=str,
        default=None,
        help="Caminho de um brief JSON (livro genérico). Sem ele, usa o livro fixo.",
    )

    args = parser.parse_args()

    brief = None
    if args.brief:
        from book_writer.brief import load_brief
        brief = load_brief(args.brief)

    if args.list:
        if brief:
            print(f"\nCapítulos de '{brief.get('title')}':\n")
            for ch in brief.get("chapters", []):
                print(f"  Cap {ch['num']}: {ch['title']}")
        else:
            from book_writer.knowledge_base import BOOK_OUTLINE
            print("\nCapítulos disponíveis:\n")
            for part_num in sorted(BOOK_OUTLINE["parts"]):
                part = BOOK_OUTLINE["parts"][part_num]
                print(f"  PARTE {part_num}: {part['title']}")
                for ch_num in sorted(part["chapters"]):
                    print(f"    Cap {ch_num}: {part['chapters'][ch_num]}")
                print()
        return

    if brief:
        nums = [ch["num"] for ch in brief.get("chapters", [])]
        if args.chapter not in nums:
            print(f"Erro: Capítulo {args.chapter} não existe no brief. Use: {nums}")
            sys.exit(1)
    elif args.chapter < 1 or args.chapter > 8:
        print(f"Erro: Capítulo {args.chapter} inválido. Use 1-8.")
        sys.exit(1)

    from book_writer.engine import run_pipeline

    run_pipeline(
        chapter_num=args.chapter,
        max_revisions=args.max_revisions,
        verbose=not args.quiet,
        brief=brief,
    )


if __name__ == "__main__":
    main()
