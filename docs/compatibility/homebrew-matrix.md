# Homebrew compatibility matrix

No external homebrew executable has been launched. All runtime dimensions remain NOT_TESTED. These reports describe conversion and static import compatibility only.

| Application | Release | Stage | Implemented exports | Throwing stubs | Absent imports |
|---|---|---|---:|---:|---:|
| [PPSA69420](https://github.com/Marice/ScreenTester5) | 01.000.000 | RELINKED | 204 | 0 | 4 |
| [PPSA99005](https://github.com/blackbearreloaded/ps5-opengl) | v1.0.1 | RELINKED | 239 | 0 | 16 |
| [PPSA99039](https://github.com/sainsaji/EVO-PLAYER-PS5) | v0.12.0 | RELINKED | 311 | 1 | 30 |
| [PPSA99001](https://github.com/blackbearreloaded/ProsperoRadio) | 01.000.010 | RELINKED | 397 | 2 | 56 |

Exact release URLs, archive hashes, extracted ELF hashes, relinker hash, output hashes, registry hashes, bundled module hashes and built-library hashes are recorded in [homebrew-report.json](homebrew-report.json). Detailed per-title import JSON is adjacent. The export classifier does not establish full semantics. Bundled modules are not recursively audited by the current upstream import tool.

Packaged eboot.bin files initially failed with `The input is a SELF container, not an ELF`. The projects distribute plaintext homebrew containers. ScreenTester5 source at `72913163d6a73518fb4133d95221ca64afa6aac8` provides the GPLv3 extractor in tooling/native/self_container.cpp; a separately built wrapper used it to reconstruct ELF input and bundled modules. No keys, firmware or commercial assets were used. The official CLI equivalent is `ps5-native-tool self --extract --file <fself> --out <elf>`. Original downloads remain unchanged outside this repository.

## Shared absent imports

| Library | Name | NID | Titles |
|---|---|---|---:|
| libkernel.prx | pthread_sigmask | JZKw5+Wrnaw | 3 |
| libkernel.prx | sigaction | KiJEPEWRyUY | 3 |
| libScePosixForWebKit.prx | isatty | InoC17C0v7k | 3 |
| libScePosixForWebKit.prx | mkstemp | uEtgPWgPxOk | 3 |
| libSceVideoOut.prx | sceVideoOutGetResolutionStatus | 6kPnj51T62Y | 3 |

First implementation priorities are signal handling, isatty/mkstemp and VideoOut resolution status. Review existing PRs before implementation. ProsperoRadio also needs Opus modules. A new implementation should follow guest ABI/error semantics and must not silently claim success.

The sysctl checkpoint `29ebb25b0b9343e2dca2ed7e23220d63f2482b6e` reduces absent counts from 6/17/31/58 to 4/16/30/56. Only hw.ncpu and hw.realmem are supported; other sysctl queries still throw. Implemented-export counts therefore must not be read as complete API coverage. ScreenTester5 still lacks sceSystemServiceLaunchWebBrowser, pthread_setcanceltype, pthread_sigmask and sigaction. Static query evidence is in [screentester-sysctl-evidence.json](screentester-sysctl-evidence.json).

## Runtime evidence still required

The earlier kernel checkpoint `a7dd9324c7623014a7f6a1f1bc2c51e0ed94f807` added pthread_set_name_np and five signal-set operations, with the prerequisite signal-mask indexing correction. Absent imports then changed from 9/20/33/63 to 6/17/31/58. The latest refreshed report records clean source state, tree identity and rebuilt-library hashes. All four conversions succeeded again.

Startup, visuals, keyboard/controller input, audio, filesystem behavior, shutdown, leaks, deadlocks, CPU/GPU timing and resource use have not been tested. Launch only in an appropriate isolated environment after verifying test inputs. AnyPS5 itself provides no isolation. Do not promote RELINKED to FUNCTIONAL on the strength of import resolution.
