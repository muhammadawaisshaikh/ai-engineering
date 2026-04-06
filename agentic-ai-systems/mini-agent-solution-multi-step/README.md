# Mini Agent Solution

A small modular Python project that demonstrates a multi-step agent workflow:

1. Analyze task
2. Plan solution
3. Execute tool calls
4. Validate result

## Structure

- `agent/analyzer.py`: intent and entity extraction
- `agent/planner.py`: per-intent execution plans
- `agent/tools/`: mock weather and pricing tools
- `agent/executor.py`: plan execution with trace
- `agent/validator.py`: result validation
- `agent/orchestrator.py`: `run_agent` end-to-end flow
- `main.py`: sample tasks runner

## Run

```bash
python main.py
```
