## Generic vs. Specific

If sections of your plugin or specific subfunctions can have high reuse potential, consider making them a separate library in your repo, and calling that library within your code. Not all useful code has to be a plugin. For example, logging code (such as MDF4) might be more appropriate as a reuse library that a PE developer uses like a palette, rather than a standalone plugin.

## Code duplication vs. Abstraction

Think of the customer, not the developer. In general, highly abstract PEs require the customer to jump through more hoops at configuration-time in order for the PE to do what it needs to do. Highly specific PEs are easier to understand for the user and can have descriptive names (NI 1487 GMSL 8-channel with Logging vs NI 1487 GMS 4-channel no Logging). This will not be hard to see on a configurator palette. 

## Monoliths vs. Distribution

If 2 plugins only work when they're together, make them one plugin.
If a plugin only works with another plugin when multiple parameters match in a specific way, consider one plugin