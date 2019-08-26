## Neutral Metrics
Neutral metrics are those that don't require human judgement to interpret.

Examples:
* A gate of zero compiler warnings is neutral; reviewing warnings to check if they are acceptable is not
* Maximum cyclometric complexity is neutral; an opnionated 'maintenance indicator' % given by a tool is not - though reported by a tool, the opinions are human :)

Gating on neutral metrics gives the team a direction with specific targets.
Non-neutral metrics are good as overall motivators / as benchmarks.

Let's look at some examples of 'measuring metrics for action'
1. High fan-out
2. Low coverage
3. Duplication
4. Dead code
5. High complexity

How about combining metrics?
1. High coverage, but high field defects too //check if funcs are called, etc.
2. High complexity with high fan-out
