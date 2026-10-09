# Regression suite

## System configuration continuation

Local code `7f9770322`, published tree-equivalent code `29ebb25b0b9343e2dca2ed7e23220d63f2482b6e`: full native build and patched-library build pass. Full CTest remains **525 passed, 1 failed, 2 skipped out of 528** (73.37 seconds); the pixel-interlock failure and two skips are unchanged. Evidence: sysctl-full.xml. The CPU-only patch passes its focused test (sysctl.xml). The added memory fallback regression fails before implementation (sysctl-realmem-before.xml) and passes after (sysctl-realmem-after.xml). Source conventions and test-registration checks pass before the required report updates.

Windows/Linux CI now includes guest_system_configuration: [37943953798](https://github.com/Alexander423/AnyPS5/actions/runs/37943953798) passed on both Windows and Linux, including the Linux shader checks, on 2026-10-09. Status is recorded in baseline.json. All four homebrew conversions and static import audits were repeated against clean source and freshly built libraries. No application was launched.

## Kernel API continuation

The full native build and patched libraries were rebuilt at local code `9111f729d` (published tree-equivalent code `a7dd9324c7623014a7f6a1f1bc2c51e0ed94f807`). Full CTest: **525 passed, 1 failed, 2 skipped out of 528**, in 77 seconds. Failure/skips are unchanged. New guest_signal_sets and existing guest_signals/guest_thread_self pass. Source conventions passed against develop before report updates; test-registration checking reports 447 executables, the two already recorded unrun executables, and no new omissions.

signal-mask-before.xml records the new GuestSignals cases against the old production implementation: failure. signal-mask-after.xml records the same cases after correction: pass. kernel-api-full.xml records the full run. kernel-apis.xml and thread-name.xml contain focused results. The initial attempt used an incorrect build target; it was corrected and rebuilt before capturing the before/after evidence.

Pixel interlock reproduces with APS5_SPIRV_OPT=none and separately APS5_BDA_BYTE_READS=1, both reporting the same wave64 BDA-fault pixel 0 write (1 instead of 0). The first three normal wave64 draws complete before DrawFault fails; later wave32 cases are not reached. These switches do not establish a root cause. Assertions and GPU implementation are unchanged. No Vulkan validation-layer run was performed. The Khronos validation-layer release inspected offers Android binaries; a suitable Windows tooling setup remains pending.

Expanded Windows/Linux CI includes thread names, signal masking and signal sets alongside the prior relinker/ABI and Linux shader tests: [37941840109](https://github.com/Alexander423/AnyPS5/actions/runs/37941840109). Both Windows and Linux passed; the run completed on 2026-10-09. Status is also recorded in baseline.json.

Baseline `d70b89989473ba1f6ae13e44e079e67f1f8a44b0`: native relinker built; 39/40 CTest tests passed, TLS function coverage exceeded 30 seconds. Commit `ff130a37` shards the same cases deterministically across 16 tests and preserves the 30-second cap. That suite passed 55/55; adding the report tests produced 56/56 passes. No cases were deliberately dropped. The unsharded script remains usable without optional shard arguments.

`guest_atoll` and `guest_thread_atexit` passed against native MinGW system libraries. The full native system-library build also passed with SPIRV-Tools enabled. Full runtime, shader, sanitizer and Vulkan-validation suites are separate and not implied by these results.

Commands (with project-local MinGW bin on PATH):

```text
cmake -S . -B build-relinker -G Ninja -DCMAKE_BUILD_TYPE=Release -DANYPS5_RELINKER_ONLY=ON -DBUILD_TESTING=ON
cmake --build build-relinker --parallel 4
ctest --test-dir build-relinker --output-on-failure --timeout 30 -j 4 --output-junit final.xml
cmake --build build --target guest_atoll_tests guest_thread_atexit_tests --parallel 4
ctest --test-dir build -R "^(guest_atoll|guest_thread_atexit)$" --output-on-failure
```

The homebrew reporter verifies the exact input hash, refuses existing output/registry files, runs only the relinker with a timeout and captures return codes, stdout, stderr and artifact hashes. It never launches guest outputs. A RELINKED result cannot become FUNCTIONAL automatically. Eight unit tests cover checksum mismatch, missing inputs/tool, stale output, missing output artifacts, conversion failure, timeout and stage integrity.

```text
python tools/homebrew_report.py docs/compatibility/homebrew-elf-manifest.json --root ../homebrew-elf --relinker build-relinker/core/relinker/relinker.exe --output ../homebrew-results/new-run
```

Use a fresh output directory. Source commit, tree state and relinker hash are included. It does not yet verify every bundled module hash or launch isolated runtime sessions. Import auditing uses the existing tools/import_audit.py against built patched PRX files; its implemented class is an export/stub classification, not proof of complete API semantics.

The develop-regression workflow runs relinker and focused library ABI tests on Windows and Linux and uploads JUnit evidence. The first published code run is [37937228680](https://github.com/Alexander423/AnyPS5/actions/runs/37937228680). Both Windows and Linux passed the relinker and library ABI checks in that run. It does not replace upstream's full shader/Vulkan tests.

Fork discovery uses tools/fork_inventory.py; branch enumeration and local merge-base/patch-id analysis use tools/fork_branch_audit.py. HTTP failures preserve partial results; long waits are not hidden. Both discovery and snapshot comparison support --resume. Rate-limit reset and Retry-After headers are recorded when available. Per-fork PR/discussion auditing remains incomplete.


## Full native GPU baseline and correction

All native targets and the `libs` target built with SPIRV-Tools enabled. Before the half-float fix: 522 passed, 3 failed, 2 skipped (527 total). The failing tests were pixel_interlock, sdwa_float_selectors and sdwa_ldexp_f16. The three were rebuilt and run serially at untouched upstream `d70b89989473ba1f6ae13e44e079e67f1f8a44b0`; all three reproduced. Development sources were restored, rebuilt, and both ABI tests passed again.

Community patch `58f596ee894d5d0d326a379032950ff4170c6964` fixes the two SDWA failures on the RX 6600 without changing expected outputs. The complete subsequent native run produced **524 passed, 1 failed, 2 skipped**. Pixel interlock remains a baseline blocker: `pixel 0 counted 1 of 0 overlapping read-modify-writes`. The skips are storage_cache_budget and guest_video_out_wqhd_detection_no_vulkan. These results do not mean the full suite is green.

JUnit evidence: baseline-gpu.xml, full-native.xml, rdna2-targeted.xml, rdna2-full.xml and restored-abi.xml. The CI workflow now also builds/runs the two SDWA cases plus NaN quieting under Linux lavapipe with SPIRV-Tools. Its newer run is [37938980558](https://github.com/Alexander423/AnyPS5/actions/runs/37938980558); Windows and Linux both passed, including all three Linux shader regression tests. The workflow completed successfully on 2026-10-09. Actual Vulkan validation layers were absent locally; SPIR-V validation and GPU-result tests are distinct from layer validation.

Committed JUnit files normalize trailing whitespace in diagnostic lines; raw originals remain in the local build directories. Snapshot JSON shards are indexed with content hashes.

The upstream conventions checker reports nine notes-file errors for the nine Markdown reports explicitly required by this fork request. The user instruction takes precedence over that upstream documentation policy. No checker rule was disabled; source checks passed before the reports were added.
