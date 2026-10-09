# Engineering roadmap

1. Fork and origin are established; develop is published. Keep main a clean upstream line. Preserve verified tree identity when using connector publication.
2. Structural audit of all advertised tips is complete except seven unrelated histories and three inaccessible repositories; detailed semantics and PR/issue/discussion evidence remain incomplete. Prioritize isolated general fixes over Astro Bot branch merges.
3. Full native build and 528-test checkpoint are complete. Investigate the remaining pixel-interlock failure; install project-local Vulkan validation tooling for further diagnosis. Preserve failing assertions.
4. Import audits refreshed after per-thread signals and pthread_sigmask: absent counts 3/15/30/55. Continue with ScreenTester5's sigaction, cancellation and browser launch, then the other titles. PR1916 remains deferred pending complete handler delivery/mask/flag semantics. Preserve per-thread masks, pending delivery and context tests; investigate remaining asynchronous host-lock/TLS hazards. Only hw.ncpu and hw.realmem sysctl queries are supported.
5. Prepare a verified isolated runtime environment before executing external homebrew. Record startup, rendering, input, audio, filesystem, shutdown, crashes and resource lifetimes independently. No runtime stage is earned by relinking.
6. Add focused general ABI/shader regressions for demonstrated failures. Retain attribution and GPLv2-only compatibility. Keep GPLv3 test sources outside the implementation tree.
7. Establish controlled performance baselines only after correctness. No GTA-specific changes or commercial-game claims.

Upstream synchronization is manual: fetch upstream, compare exact hashes and patch equivalence, integrate on an isolated branch, run relevant tests, then advance develop. Do not automatically replace tested functionality, merge into main or open upstream PRs. No recurring automation has been installed.
