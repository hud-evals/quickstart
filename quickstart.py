#!/usr/bin/env python3
"""
Complete Agent Lifecycle Example

This example demonstrates the full agent lifecycle:
- Task definition with setup and evaluation tools
- Agent initialization
- Setup phase
- Agent execution loop
- Tool call handling
- Evaluation phase
- Cleanup

The entire flow is wrapped in hud.trace() to provide RUN_ID context.
"""

import asyncio
import hud
from datasets import load_dataset
from hud.datasets import Task
from hud.clients import MCPClient
from hud.agents.claude import ClaudeAgent
from hud.agents.base import find_reward, find_content
from pprint import pprint

import logging
# logging.basicConfig(level=logging.INFO)

async def main():

    # Pull down the SheetBench-50 dataset from our public huggingface dataset.
    # https://huggingface.co/datasets/hud-evals/SheetBench-50
    print("📊 Loading dataset…")
    dataset = load_dataset("hud-evals/SheetBench-50", split="train")

    # Get the first task from the dataset
    sample_task = dataset[0]  # type: ignore[index]

    # Wrap everything in trace to provide RUN_ID for the task
    with hud.trace("SheetBench-50 Quickstart Task"):

        # Construct a Task object from the sample task
        task = Task(**sample_task)

        # Create MCP client with resolved config
        print(f"🔍 MCP client config:")
        pprint(task.mcp_config)
        client = MCPClient(mcp_config=task.mcp_config)

        # Create agent
        print("\n🔧 Creating agent...")
        agent = ClaudeAgent(
            mcp_client=client,
            model="claude-3-7-sonnet-20250219",
            allowed_tools=["anthropic_computer"],
            initial_screenshot=True,
        )

        try:
            # Phase 1: Initialize agent with task context
            print("🔧 Initializing agent...")
            await agent.initialize(task)

            # Phase 2: Run setup tool
            print("📋 Running setup...")
            setup_result = await agent.call_tools(task.setup_tool)
            setup_content = setup_result[0].content
            print("✅ Setup complete")

            # Phase 3: Add context and first messages
            print(f"\n🤖 Running task: {task.prompt}")
            messages = await agent.get_system_messages()

            # Add context
            context = await agent.format_message(
                [
                    *setup_content,
                    task.prompt,
                ]
            )

            messages.extend(context)
            print(f"\nMessages: {messages}")

            # Phase 4: Run agent loop
            done = False
            steps = 0
            max_steps = 10

            # Use messages as the state for the agent
            while not done and steps < max_steps:
                # Get model response
                response = await agent.get_response(messages)
                print(f"\n   Step {steps + 1}:")

                if response.content:
                    print(f"   💭 Agent: {response.content[:100]}...")

                if response.tool_calls:
                    # Execute tool calls
                    tool_results = await agent.call_tools(response.tool_calls)

                    # Format results back into messages
                    messages.extend(
                        await agent.format_tool_results(response.tool_calls, tool_results)
                    )
                else:
                    # No more tool calls, we're done
                    done = True

                steps += 1

            # Phase 4: Run evaluation
            print("\n📊 Running evaluation...")
            eval_result = await agent.call_tools(task.evaluate_tool)

            if eval_result[0].isError:
                print(f"❌ Evaluation failed: {eval_result[0].content}")
            else:
                reward = find_reward(eval_result[0])
                eval_content = find_content(eval_result[0])
                print(f"✅ Evaluation complete - Reward: {reward}")
                print(f"✅ Evaluation complete - Content: {eval_content}")

            # Summary
            print("\n📈 Summary:")
            print(f"   Total steps: {steps}")
            print(f"   Task completed: {done}")

        finally:
            # Phase 5: Cleanup
            print("\n🧹 Cleaning up...")
            await client.shutdown()

    
    # Print beautiful next steps guide with colors and hyperlinks
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
    print(f"          {BOLD}{YELLOW}Our SDK helps ML researchers and AI developers:{RESET}")
    print(f"  • Run agentic evaluations    • Develop RL environments    • Train agents\n")
    
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
    
    # Special opportunities
    print(f"{BOLD}{GREEN}💝 Special Opportunities{RESET}\n")
    
    print(f"  {BOLD}Students & Researchers:{RESET} {link('Apply for research grants and credits', 'https://docs.google.com/forms/d/e/1FAIpQLSf-Vq23Zw5DD05vNgNySAcLNI2U6db0SBZAvcwqCmlDjq10cw/viewform')}")
    print(f"  {BOLD}Labs & Enterprises:{RESET} {link('founders@hud.so', 'mailto:founders@hud.so')} or {link('Book a demo', 'https://cal.com/team/hud/demo')}\n")
    
    print(f"{BOLD}{GREEN}{'═' * 80}{RESET}")
    print(f"{BOLD}{WHITE}{center('Happy building! 🚀')}{RESET}")
    print(f"{BOLD}{GREEN}{'═' * 80}{RESET}\n")


if __name__ == "__main__":
    print("🚀 Agent Lifecycle Example")
    print("=" * 50)
    asyncio.run(main())
