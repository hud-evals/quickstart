# Welcome to hud!

We help AI engineers and ML researchers evaluate their models and build environments!

## What this quickstart does

This quickstart will allow you to:
1. Pull down an evaluation set
2. Initialize an eval environment on our hosted infra
3. Run an agent through a task on the environment
4. Evaluate the environment
5. Close the remote environment
6. View the trajectory and telemetry in our trace viewer (steps, tool-calls, score, and logs)

## Repository contents

- `pyproject.toml` - dependencies for the hud-python SDK
- `quickstart.py` - a simple walkthrough of the full agent loop
- `.env.example` - a template for your environment variables
- `README.md` - this file

## Getting started

1. **Sign up** at [app.hud.so](https://app.hud.so)
2. **Get your API key** from [app.hud.so/project/api-keys](https://app.hud.so/project/api-keys)
3. **Configure environment variables** - Copy `.env.example` to `.env` and add your:
   - HUD API key
   - OpenAI API key
   - Claude API key
4. **Run the quickstart**: `uv run quickstart.py` 