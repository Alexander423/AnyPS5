# Homebrew compatibility matrix

No external homebrew executable has been launched. All runtime dimensions remain NOT_TESTED. These reports describe conversion and static import compatibility only.

| Application | Release | Stage | Implemented exports | Throwing stubs | Absent imports |
|---|---|---|---:|---:|---:|
| [PPSA69420](https://github.com/Marice/ScreenTester5) | 01.000.000 | RELINKED | 206 | 0 | 2 |
| [PPSA99005](https://github.com/blackbearreloaded/ps5-opengl) | v1.0.1 | RELINKED | 242 | 0 | 13 |
| [PPSA99039](https://github.com/sainsaji/EVO-PLAYER-PS5) | v0.12.0 | RELINKED | 313 | 1 | 28 |
| [PPSA99001](https://github.com/blackbearreloaded/ProsperoRadio) | 01.000.010 | RELINKED | 400 | 2 | 53 |

Exact release URLs, archive hashes, extracted ELF hashes, relinker hash, output hashes, registry hashes, bundled module hashes and built-library hashes are recorded in [homebrew-report.json](homebrew-report.json). Detailed per-title import JSON is adjacent. The export classifier does not establish full semantics. Bundled modules are not recursively audited by the current upstream import tool.

Packaged eboot.bin files initially failed with `The input is a SELF container, not an ELF`. The projects distribute plaintext homebrew containers. ScreenTester5 source at `72913163d6a73518fb4133d95221ca64afa6aac8` provides the GPLv3 extractor in tooling/native/self_container.cpp; a separately built wrapper used it to reconstruct ELF input and bundled modules. No keys, firmware or commercial assets were used. The official CLI equivalent is `ps5-native-tool self --extract --file <fself> --out <elf>`. Original downloads remain unchanged outside this repository.

The earlier signal checkpoint `a4d82b379d042d97fc506bf2922566f0b0d12490` adds pthread_sigmask after integrating per-thread masks, reducing absent counts from 4/16/30/56 to **3/15/30/55**. At that checkpoint ScreenTester5 lacked sigaction, pthread_setcanceltype and sceSystemServiceLaunchWebBrowser. Export resolution alone does not prove application behavior.

The POSIX/browser checkpoint `f0288f10f30a8517b360d9aa276b54fb423a34a6` reduces absent counts to **2/13/28/53**. ScreenTester5 still lacks sigaction and pthread_setcanceltype. Its 206 exports classified implemented include **one always-unavailable export**, sceSystemServiceLaunchWebBrowser, which returns 0x8002002D and opens nothing. The machine-readable report records this under known_unavailable_exports. Neither the count nor successful relinking establishes browser or application functionality.

## Shared absent imports

| Library | Name | NID | Titles |
|---|---|---|---:|
| libkernel.prx | sigaction | KiJEPEWRyUY | 3 |
| libSceVideoOut.prx | sceVideoOutGetResolutionStatus | 6kPnj51T62Y | 3 |

Next priorities are sigaction, cancellation and VideoOut resolution status. Review existing PRs before implementation. ProsperoRadio also needs Opus modules. A new implementation should follow guest ABI/error semantics and must not silently claim success.

The earlier sysctl checkpoint `29ebb25b0b9343e2dca2ed7e23220d63f2482b6e` reduces absent counts from 6/17/31/58 to 4/16/30/56. Only hw.ncpu and hw.realmem are supported; other sysctl queries still throw. Implemented-export counts therefore must not be read as complete API coverage. At that checkpoint ScreenTester5 still lacked sceSystemServiceLaunchWebBrowser, pthread_setcanceltype, pthread_sigmask and sigaction. Static query evidence is in [screentester-sysctl-evidence.json](screentester-sysctl-evidence.json).

## Runtime evidence still required

The earlier kernel checkpoint `a7dd9324c7623014a7f6a1f1bc2c51e0ed94f807` added pthread_set_name_np and five signal-set operations, with the prerequisite signal-mask indexing correction. Absent imports then changed from 9/20/33/63 to 6/17/31/58. The latest refreshed report records clean source state, tree identity and rebuilt-library hashes. All four conversions succeeded again.

Startup, visuals, keyboard/controller input, audio, filesystem behavior, shutdown, leaks, deadlocks, CPU/GPU timing and resource use have not been tested. Launch only in an appropriate isolated environment after verifying test inputs. AnyPS5 itself provides no isolation. Do not promote RELINKED to FUNCTIONAL on the strength of import resolution.
