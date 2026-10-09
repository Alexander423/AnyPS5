# Engineering roadmap

1. Fork and origin are established; develop is published. Keep main a clean upstream line. Preserve verified tree identity when using connector publication.
2. Structural audit of all advertised tips is complete except seven unrelated histories and three inaccessible repositories; detailed semantics and PR/issue/discussion evidence remain incomplete. Prioritize isolated general fixes over Astro Bot branch merges.
3. Full native build and 528-test checkpoint are complete. Investigate the remaining pixel-interlock failure; install project-local Vulkan validation tooling for further diagnosis. Preserve failing assertions.
4. Import audits refreshed after POSIX filesystem/browser availability: absent counts 2/13/28/53. ScreenTester5 still needs sigaction and cancellation; browser launch now resolves but explicitly returns unavailable. Continue with accurate signal/cancellation behavior, then the other titles. PR1916 remains deferred pending complete handler delivery/mask/flag semantics. Preserve per-thread masks, pending delivery and context tests; investigate remaining asynchronous host-lock/TLS hazards. Only hw.ncpu and hw.realmem sysctl queries are supported.
5. Prepare a verified isolated runtime environment before executing external homebrew. Record startup, rendering, input, audio, filesystem, shutdown, crashes and resource lifetimes independently. No runtime stage is earned by relinking.
6. Add focused general ABI/shader regressions for demonstrated failures. Retain attribution and GPLv2-only compatibility. Keep GPLv3 test sources outside the implementation tree.
7. Establish controlled performance baselines only after correctness. No GTA-specific changes or commercial-game claims.

Upstream synchronization is manual: fetch upstream, compare exact hashes and patch equivalence, integrate on an isolated branch, run relevant tests, then advance develop. Do not automatically replace tested functionality, merge into main or open upstream PRs. No recurring automation has been installed.

Latest upstream inspection: c6e3aa767ba9a83db67496d6da7a18486c51d0f6 on 2026-10-10, 95 first-parent commits beyond our original baseline. Only PR1613 and PR2065 plus their follow-ups were selected this turn; the rest require review. In particular, upstream Windows YMM preservation (15c1962e8) is a next candidate to reconcile with our signal integration. main remains unchanged.
