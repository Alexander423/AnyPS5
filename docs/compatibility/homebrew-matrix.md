# Homebrew compatibility matrix

No external homebrew executable has been launched. All runtime dimensions remain NOT_TESTED. These reports describe conversion and static import compatibility only.

| Application | Release | Stage | Implemented exports | Throwing stubs | Absent imports |
|---|---|---|---:|---:|---:|
| [PPSA69420](https://github.com/Marice/ScreenTester5) | 01.000.000 | RELINKED | 199 | 0 | 9 |
| [PPSA99005](https://github.com/blackbearreloaded/ps5-opengl) | v1.0.1 | RELINKED | 235 | 0 | 20 |
| [PPSA99039](https://github.com/sainsaji/EVO-PLAYER-PS5) | v0.12.0 | RELINKED | 308 | 1 | 33 |
| [PPSA99001](https://github.com/blackbearreloaded/ProsperoRadio) | 01.000.010 | RELINKED | 390 | 2 | 63 |

Exact release URLs, archive hashes, extracted ELF hashes, relinker hash, output hashes, registry hashes, bundled module hashes and built-library hashes are recorded in [homebrew-report.json](homebrew-report.json). Detailed per-title import JSON is adjacent. The export classifier does not establish full semantics. Bundled modules are not recursively audited by the current upstream import tool.

Packaged eboot.bin files initially failed with `The input is a SELF container, not an ELF`. The projects distribute plaintext homebrew containers. ScreenTester5 source at `72913163d6a73518fb4133d95221ca64afa6aac8` provides the GPLv3 extractor in tooling/native/self_container.cpp; a separately built wrapper used it to reconstruct ELF input and bundled modules. No keys, firmware or commercial assets were used. The official CLI equivalent is `ps5-native-tool self --extract --file <fself> --out <elf>`. Original downloads remain unchanged outside this repository.

## Shared absent imports

| Library | Name | NID | Titles |
|---|---|---|---:|
| libkernel.prx | sysctl | DFmMT80xcNI | 4 |
| libkernel.prx | pthread_set_name_np | oxMp8uPqa+U | 4 |
| libkernel.prx | sigemptyset | +F7C-hdk7+E | 3 |
| libkernel.prx | pthread_sigmask | JZKw5+Wrnaw | 3 |
| libkernel.prx | sigaction | KiJEPEWRyUY | 3 |
| libScePosixForWebKit.prx | isatty | InoC17C0v7k | 3 |
| libScePosixForWebKit.prx | mkstemp | uEtgPWgPxOk | 3 |
| libSceVideoOut.prx | sceVideoOutGetResolutionStatus | 6kPnj51T62Y | 3 |

First implementation priorities are sysctl and pthread_set_name_np (all four), then signal handling, isatty/mkstemp and VideoOut resolution status. Review existing PRs before implementation. ProsperoRadio also needs Opus modules. A new implementation should follow guest ABI/error semantics and must not silently claim success.

## Runtime evidence still required

Startup, visuals, keyboard/controller input, audio, filesystem behavior, shutdown, leaks, deadlocks, CPU/GPU timing and resource use have not been tested. Launch only in an appropriate isolated environment after verifying test inputs. AnyPS5 itself provides no isolation. Do not promote RELINKED to FUNCTIONAL on the strength of import resolution.
