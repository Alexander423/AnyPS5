# Architecture baseline

Source: [upstream architecture](../dev/ARCHITECTURE.md), revision `d70b89989473ba1f6ae13e44e079e67f1f8a44b0`.

AnyPS5 converts guest x86-64 ELF programs and bundled modules into host ELF or PE files. The output executes natively and resolves guest imports against replacement system libraries. It is not a CPU interpreter or a sandbox. The relinker performs executable-format, relocation, import, TLS and instruction transformations. `core/libs/prx` supplies system behavior; bundled application modules must remain application-owned.

The AGC implementation translates guest graphics work to Vulkan. The shader recompiler decodes guest instructions, constructs intermediate representation and emits SPIR-V. Optional SPIRV-Tools validation checks module validity; it cannot establish pixel correctness. General memory, resource lifetime, synchronization and ABI behavior take precedence over per-title bypasses.

Local changes: TLS regression sharding, the attributed atoll export and ABI regression, a verified general half-float SPIR-V conversion correction, and discovery/compatibility tooling. No commercial-title or performance modifications were made. Existing GPLv2-only licensing and copyright notices are retained. GPLv3 homebrew source and binaries are kept outside this repository.
