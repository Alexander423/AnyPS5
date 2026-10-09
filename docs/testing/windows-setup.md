# Native Windows setup

Observed host: Windows 11 Pro 10.0.26200, Ryzen 5 5600G (6 cores / 12 logical processors), approximately 16 GB RAM, Radeon RX 6600 driver 32.0.21045.5002. Initial C: free space was approximately 178 GB. Visual Studio 2026 is installed; upstream requires MinGW rather than MSVC.

Project-local compiler: `../toolchains/mingw64/bin`, WinLibs GCC 15.2.0, release `15.2.0posix-14.0.0-ucrt-r7`. Download SHA-256 `cb2fbad6162540cdf5e1facdce08d4dac359e8cf64f7f696a99274291763b815` matches GitHub release metadata. CMake and Ninja are bundled; Python is 3.13.3. PATH changes are process-local. Use the Git for Windows CA bundle through SSL_CERT_FILE for FFmpeg configuration. No global settings were changed.

Vulkan loader probe: RX 6600, Vulkan 1.4.315, subgroup size 64, device-local heap 8573157376 bytes. WMI AdapterRAM is truncated and is not used as evidence of VRAM capacity. No VK_LAYER_KHRONOS_validation was enumerated; SDK environment variable was absent. Vulkan device enumeration is not a rendering or shader correctness test.

Follow [upstream build instructions](../dev/BUILD.md). The relinker-only build needs no submodules. Full configuration initializes all pinned third-party submodules. Build the `libs` target explicitly before import auditing or runtime work; an ordinary build is insufficient.

Local Git: main retains the original upstream snapshot, upstream remote points to boykopovar/AnyPS5, develop contains verified local changes. The user created Alexander423/AnyPS5 during setup; origin points to that fork. Local Git has no noninteractive write credential, so publication uses the authenticated GitHub Git Database connector. Each remote tree is checked against the corresponding locally tested tree. Local and remote commit IDs differ because commit metadata is recreated; the original community author is preserved through the atoll source commit as a merge parent, attribution trailers and the patch catalog. main remains unchanged.
