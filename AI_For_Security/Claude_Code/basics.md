https://code.claude.com/docs/en/best-practices

### What is is?
Claude Code is an agentic coding environment. Unlike a chatbot that answers questions and waits, Claude Code can read your files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely.

This changes how you work. Instead of writing code yourself and asking Claude to review it, you describe what you want and Claude figures out how to build it. Claude explores, plans, and implements.

But this autonomy still comes with a learning curve. Claude works within certain constraints you need to understand.

### How it works?

https://code.claude.com/docs/en/how-claude-code-works

Claude Code is an agentic assistant that runs in your terminal. While it excels at coding, it can help with anything you can do from the command line: writing docs, running builds, searching files, researching topics, and more.

`The Agentic loop`: When you give Claude a task, it works through three phases: 
1. gather context
2. take action
3. verify results

The agentic loop is powered by two components: `models` that reason and `tools` that act.

Claude Code uses Claude models to understand your code and reason about tasks

Tools are what make Claude Code agentic. Without tools, Claude can only respond with text. With tools, Claude can act: read your code, edit files, run commands, search the web, and interact with external services

The built-in tools generally fall into five categories, each representing a different kind of agency.
```
Category	                    What Claude can do

File operations	                Read files, edit code, create new files, rename and reorganize
Search	                        Find files by pattern, search content with regex, explore codebases
Execution	                    Run shell commands, start servers, run tests, use git
Web	                            Search the web, fetch documentation, look up error messages
Code intelligence	            See type errors and warnings after edits, jump to definitions, find references (requires code intelligence plugins)
```
Each tool use gives Claude new information that informs the next step. This is the agentic loop in action.

### Extending the base capabilities

https://code.claude.com/docs/en/features-overview

The built-in tools are the foundation, however you can extend what Claude knows with `skills`, `CLAUDE.md` adds persistent context Claude sees every session, connect to external services with `MCP`, automate workflows with `hooks`, and offload tasks to `subagents`.

`Skills` are the most flexible extension. A skill is a markdown file containing knowledge, workflows, or instructions. You can invoke skills with a command like /deploy, or Claude can load them automatically when relevant. Skills can run in your current conversation or in an isolated context via subagents.


### Best Pactices

https://code.claude.com/docs/en/best-practices

Most best practices are based on one constraint: `Claude’s context window fills up fast, and performance degrades as it fills.`

Claude’s context window holds your entire conversation, including every message, every file Claude reads, and every command output. However, this can fill up fast. A single debugging session or codebase exploration might generate and consume tens of thousands of tokens.

`This matters since LLM performance degrades as context fills`. When the context window is getting full, Claude may start “forgetting” earlier instructions or making more mistakes. The context window is the most important resource to manage

- Track context usage continuously with a `custom status line`, and see `Reduce token usage` for strategies on reducing token usage