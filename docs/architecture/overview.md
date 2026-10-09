# Architecture baseline

Per-thread signal masks now live on PthreadPrivate as four 32-bit words, with inherited masks and pending delivery. Linux bridges mapped guest signals to host masks and supports raised-exception context delivery; Windows maintains guest pending state and avoids an internal emulated-TLS lookup on delivery. Handler mask changes are scoped to the interrupted context. This does not implement sigaction flags or remove all asynchronous host-lock/TLS hazards. The attributed integration and limitations are in the community patch catalog.

Source: [upstream architecture](../dev/ARCHITECTURE.md), revision `d70b89989473ba1f6ae13e44e079e67f1f8a44b0`.

AnyPS5 converts guest x86-64 ELF programs and bundled modules into host ELF or PE files. The output executes natively and resolves guest imports against replacement system libraries. It is not a CPU interpreter or a sandbox. The relinker performs executable-format, relocation, import, TLS and instruction transformations. `core/libs/prx` supplies system behavior; bundled application modules must remain application-owned.

The AGC implementation translates guest graphics work to Vulkan. The shader recompiler decodes guest instructions, constructs intermediate representation and emits SPIR-V. Optional SPIRV-Tools validation checks module validity; it cannot establish pixel correctness. General memory, resource lifetime, synchronization and ABI behavior take precedence over per-title bypasses.

Local changes: TLS regression sharding, the attributed atoll export and ABI regression, a verified general half-float SPIR-V conversion correction, and discovery/compatibility tooling. No commercial-title or performance modifications were made. Existing GPLv2-only licensing and copyright notices are retained. GPLv3 homebrew source and binaries are kept outside this repository.
