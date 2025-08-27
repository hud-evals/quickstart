"""
Display next steps and resources after completing the quickstart.
"""


def print_next_steps():
    """Print a beautiful guide with next steps, resources, and opportunities."""
    
    # ANSI color codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    
    # Helper function to create clickable terminal links
    def link(text, url):
        return f"\033]8;;{url}\033\\{CYAN}{text}{RESET}\033]8;;\033\\"
    
    # Centered text helper
    def center(text, width=80):
        return text.center(width)
    
    print("\n")
    print(f"{BOLD}{GREEN}{'═' * 80}{RESET}")
    print(f"{BOLD}{WHITE}{center('🎉  CONGRATULATIONS!  🎉')}{RESET}")
    print(f"{BOLD}{WHITE}{center('You just successfully made your first run with hud!')}{RESET}")
    print(f"{BOLD}{GREEN}{'═' * 80}{RESET}\n")
    
    # What we do
    print(f"              {BOLD}{YELLOW}Our SDK helps ML researchers and AI developers:{RESET}")
    print(f"\n  • Run agentic evaluations    • Develop RL environments    • Train agents\n")
    
    # Main sections in compact format
    print(f"{BOLD}{CYAN}{'─' * 80}{RESET}")
    print(f"{BOLD}{WHITE}{center('🚀 WHAT\'S NEXT?')}{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 80}{RESET}\n")
    
    # Three paths side by side
    print(f"{BOLD}{MAGENTA}Choose Your Path:{RESET}\n")
    
    print(f"  {BOLD}🔬 EVALUATE AGENTS{RESET}           {BOLD}🏗️  BUILD ENVIRONMENTS{RESET}         {BOLD}🎯 TRAIN AGENTS{RESET}")
    print(f"  {DIM}Test on SheetBench &{RESET}         {DIM}Wrap software in MCP{RESET}          {DIM}Use RL and GRPO to{RESET}")
    print(f"  {DIM}OSWorld benchmarks{RESET}           {DIM}for agent evaluation{RESET}          {DIM}improve performance{RESET}")
    print(f"  {link('→ Docs', 'https://docs.hud.so/evaluate-agents')}                      {link('→ Docs', 'https://docs.hud.so/build-environments')}                        {link('→ Docs', 'https://docs.hud.so/train-agents')}\n")
    
    print(f"{CYAN}{'─' * 80}{RESET}\n")
    
    # Resources in two columns
    print(f"{BOLD}{WHITE}📚 Resources{RESET}                                   {BOLD}{WHITE}🛠️  Build Your Agent{RESET}")
    print(f"  {link('• Leaderboard', 'https://app.hud.so/leaderboards')}                                {link('• Agent Docs', 'https://docs.hud.so/evaluate-agents/create-agents')}")
    print(f"  {link('• Documentation', 'https://docs.hud.so/')}                              {link('• Claude Example', 'https://github.com/hud-evals/hud-python/blob/main/hud/agents/claude.py')}")
    print(f"  {link('• Prime Intellect RL', 'https://primeintellect.ai')}                         {link('• OpenAI Example', 'https://github.com/hud-evals/hud-python/blob/main/hud/agents/openai.py')}\n")
    
    print(f"{CYAN}{'─' * 80}{RESET}\n")
    
    # Partnerships and Opportunities
    print(f"{BOLD}{GREEN}💝 Partnerships and Opportunities{RESET}\n")
    
    print(f"  {BOLD}Students & Researchers:{RESET} {link('Apply for research grants and credits', 'https://docs.google.com/forms/d/e/1FAIpQLSf-Vq23Zw5DD05vNgNySAcLNI2U6db0SBZAvcwqCmlDjq10cw/viewform')}")
    print(f"  {BOLD}Labs & Enterprises:{RESET} {link('founders@hud.so', 'mailto:founders@hud.so')} or {link('Book a demo', 'https://cal.com/team/hud/demo')}\n")
    
    print(f"{BOLD}{GREEN}{'═' * 80}{RESET}")
    print(f"{BOLD}{WHITE}{center('Happy building! 🚀')}{RESET}")
    print(f"{BOLD}{GREEN}{'═' * 80}{RESET}\n")
