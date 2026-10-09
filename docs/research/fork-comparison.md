# Priority fork comparison

The signal continuation separately reviewed Zaid-Talib/AnyPS5 `claude/guest-signal-masks` at `28bea19c49379a30332e5ba207ef4a0ceffe3a4f`: six unique commits beyond its merge base. All six were integrated individually after native signal/exception tests, with conflict resolution retaining prior fixes. PR2106's pthread_sigmask wrapper was then applied against the new per-thread implementation. See the patch catalog for exact source/published mappings and unresolved signal limitations. The priority-fork snapshot below remains historical.

Baseline `d70b89989473ba1f6ae13e44e079e67f1f8a44b0`. Seven requested repositories fetched with all advertised branches: 101 refs. Ahead/behind is commit ancestry, not a functionality ranking. `git cherry` records patch-id equivalence; file lists use merge-base diffs. Duplicate merge commits and semantic equivalents require further human review.

| Branch | Tip | Ahead | Behind | Changed files | Decision |
|---|---|---:|---:|---:|---|
| [audit-AidanXVII/main](https://github.com/AidanXVII/AnyPS5/tree/main) | 3cf8ef370ec4abdacb7ba2b04dd43f5a3974a0fc | 2 | 825 | 1 | Unverified; keep isolated |
| [audit-GorramFrakker/main](https://github.com/GorramFrakker/AnyPS5/tree/main) | 1be6f9f1c58ba6e823e1855c178b831141b80095 | 0 | 105 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/astrobot-windows](https://github.com/SP4C3B4R-8/AnyPS5/tree/astrobot-windows) | ee72eb98c532ef118fcd9c543ac53941251fc44e | 401 | 1432 | 231 | Unverified; keep isolated |
| [audit-SP4C3B4R-8/feat/gds-guest-memory](https://github.com/SP4C3B4R-8/AnyPS5/tree/feat/gds-guest-memory) | faa1cc59e1397a98c9aca2446ce5d70d44102545 | 0 | 754 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/feat/jpegdec-exports](https://github.com/SP4C3B4R-8/AnyPS5/tree/feat/jpegdec-exports) | b50ddc014d69157c19aed2c8d2b89ba715441968 | 1 | 2099 | 1 | Unverified; keep isolated |
| [audit-SP4C3B4R-8/feat/missing-exports](https://github.com/SP4C3B4R-8/AnyPS5/tree/feat/missing-exports) | d56ce1953162472471c5508c261980d4e9d067b3 | 0 | 2097 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/feat/pad-tilt-correction](https://github.com/SP4C3B4R-8/AnyPS5/tree/feat/pad-tilt-correction) | c4be3f78f661305dbc5a35b8faed97201e14f98d | 0 | 2098 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/feat/windows-mapping-hints](https://github.com/SP4C3B4R-8/AnyPS5/tree/feat/windows-mapping-hints) | 4099ffb7d3b9b7e39bf88601ddbbf9290c553b2f | 0 | 2097 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/fix/absent-depth-stencil-plane](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/absent-depth-stencil-plane) | 48ebf3195e18105daf892d181d39b7b81fb33b60 | 0 | 1759 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/fix/aliased-depth-surface-texture](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/aliased-depth-surface-texture) | ab5e3a1c1bd7cef6f062af301633032bc762ceea | 9 | 134 | 16 | Unverified; keep isolated |
| [audit-SP4C3B4R-8/fix/fiber-windows-stack](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/fiber-windows-stack) | 78cb1598ce5c24e8e4319afa698b164de0ca1867 | 0 | 851 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/fix/mingw-test-runtime](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/mingw-test-runtime) | 8641b6026528cf43bf3e8431136396ca813853c9 | 0 | 2098 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/fix/replaced-device-host-imports](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/replaced-device-host-imports) | 53aac1137a431de4706fdf4c89530642785888cc | 0 | 2098 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/fix/scissor-window-offset](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/scissor-window-offset) | 579db050812ad97d23445663a631d3c4888623e4 | 0 | 1947 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/fix/vulkan-prefer-discrete-gpu](https://github.com/SP4C3B4R-8/AnyPS5/tree/fix/vulkan-prefer-discrete-gpu) | ef172bb5d1bafedf0bca3a801bbb679706a7171a | 0 | 2098 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/main](https://github.com/SP4C3B4R-8/AnyPS5/tree/main) | 709d7fe0fd1f801128793bf777c42bb94b6e885b | 0 | 2099 | 0 | Already in baseline |
| [audit-SP4C3B4R-8/perf/per-draw-gpu-timing](https://github.com/SP4C3B4R-8/AnyPS5/tree/perf/per-draw-gpu-timing) | d1cfcfe5de1a7babe2793356f2110130c33de6b1 | 395 | 1432 | 231 | Unverified; keep isolated |
| [audit-Z3R0339/feat/sce-module-load](https://github.com/Z3R0339/AnyPS5/tree/feat/sce-module-load) | 179841caff2945c6d6c4f2f77d054e47269fb27a | 0 | 2634 | 0 | Already in baseline |
| [audit-Z3R0339/fix/pad-input-header](https://github.com/Z3R0339/AnyPS5/tree/fix/pad-input-header) | 9dd86e99bf6e0baa4ec8e26c22881d14ccd83d36 | 0 | 2578 | 0 | Already in baseline |
| [audit-Z3R0339/main](https://github.com/Z3R0339/AnyPS5/tree/main) | ce6ac25b7e537e2d903e293dfd3e41b124055977 | 0 | 2571 | 0 | Already in baseline |
| [audit-ludnix/main](https://github.com/ludnix/AnyPS5/tree/main) | 5f96e1e0405ca1e34409a8142a43b90038c7f5e8 | 0 | 961 | 0 | Already in baseline |
| [audit-mjsikorsky/main](https://github.com/mjsikorsky/AnyPS5/tree/main) | 0c952fe574676b18a16bbc0af9e63ef5c4d9260d | 0 | 895 | 0 | Already in baseline |
| [audit-oneandonlydean/astrobot](https://github.com/oneandonlydean/AnyPS5/tree/astrobot) | 88d7bb6211c3299ee2777e061c232c4ed351eb32 | 393 | 1432 | 231 | Unverified; keep isolated |
| [audit-oneandonlydean/ci/build-merge-ref](https://github.com/oneandonlydean/AnyPS5/tree/ci/build-merge-ref) | 5994806a8b5bcb3abdcccc82d664d17ee7f2aa82 | 0 | 7 | 0 | Already in baseline |
| [audit-oneandonlydean/ci/lavapipe-avx-caps](https://github.com/oneandonlydean/AnyPS5/tree/ci/lavapipe-avx-caps) | 1e945e761502aa51d9941f38610c57156830ac17 | 0 | 1947 | 0 | Already in baseline |
| [audit-oneandonlydean/feat/agc-3d-thick-mip-tails](https://github.com/oneandonlydean/AnyPS5/tree/feat/agc-3d-thick-mip-tails) | 16f19c51ad0e0f90925550285e25f70019e544e0 | 0 | 1477 | 0 | Already in baseline |
| [audit-oneandonlydean/feat/audiopropagation-source-render](https://github.com/oneandonlydean/AnyPS5/tree/feat/audiopropagation-source-render) | be3f06bfe8122990fd984300ca8061f5e238b0a8 | 0 | 1944 | 0 | Already in baseline |
| [audit-oneandonlydean/feat/avplayer-ffmpeg](https://github.com/oneandonlydean/AnyPS5/tree/feat/avplayer-ffmpeg) | b62d02c2af0d23b17d93aa4991a08d3c3817af9d | 0 | 2044 | 0 | Already in baseline |
| [audit-oneandonlydean/feat/font-system-font-sets](https://github.com/oneandonlydean/AnyPS5/tree/feat/font-system-font-sets) | 9d4e6d2f28ad31750fcdecc63ce278d8d626f6cf | 0 | 1319 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/agc-compacted-color-exports](https://github.com/oneandonlydean/AnyPS5/tree/fix/agc-compacted-color-exports) | 1c4aadb3e33b4775b213c9eaadc03ab02d931dea | 0 | 1550 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/agc-gpu-timestamps](https://github.com/oneandonlydean/AnyPS5/tree/fix/agc-gpu-timestamps) | 97e9a3e65d94e2b57eb0ed2efae134551e8f74e4 | 337 | 1961 | 254 | Unverified; keep isolated |
| [audit-oneandonlydean/fix/agc-views-past-max-mip](https://github.com/oneandonlydean/AnyPS5/tree/fix/agc-views-past-max-mip) | b6298bf738028817e28a18e19e6d4227d1b3d8fa | 0 | 1807 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/agc-writeback-block-padding](https://github.com/oneandonlydean/AnyPS5/tree/fix/agc-writeback-block-padding) | a3ec50aefa9b9a8fda6dbddb8490609809e4bdd9 | 0 | 1495 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/cmask-metablock-size](https://github.com/oneandonlydean/AnyPS5/tree/fix/cmask-metablock-size) | c17337b6d9e4ad71ee603aa0690f2fb07b72919c | 0 | 531 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/hw-oracle-amdgpu-skip](https://github.com/oneandonlydean/AnyPS5/tree/fix/hw-oracle-amdgpu-skip) | e0a8297a7bc5c9542d029807efd07f5832c065ad | 0 | 5 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/recompiler-lds-array-bound](https://github.com/oneandonlydean/AnyPS5/tree/fix/recompiler-lds-array-bound) | bdf39840cf58a6758186748b3a9052c89796aad4 | 0 | 1503 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/relinker-linux-host-libc-needed](https://github.com/oneandonlydean/AnyPS5/tree/fix/relinker-linux-host-libc-needed) | 7103f390cfc18af3617dd259c0ba66b9dc970c2c | 0 | 1495 | 0 | Already in baseline |
| [audit-oneandonlydean/fix/spirv-headers-test-includes](https://github.com/oneandonlydean/AnyPS5/tree/fix/spirv-headers-test-includes) | 37bc6f2e74a931ca208999c8f5d9627b7c96ecd0 | 0 | 47 | 0 | Already in baseline |
| [audit-oneandonlydean/integ/gate-batch](https://github.com/oneandonlydean/AnyPS5/tree/integ/gate-batch) | cab0eabf077b400dbc66079a2eb1a042f1e6ba15 | 371 | 1961 | 293 | Unverified; keep isolated |
| [audit-oneandonlydean/integ/sync-1005](https://github.com/oneandonlydean/AnyPS5/tree/integ/sync-1005) | e2372d7ec5da19e333c570a8cba5ff78cfd35f1d | 350 | 1758 | 232 | Unverified; keep isolated |
| [audit-oneandonlydean/main](https://github.com/oneandonlydean/AnyPS5/tree/main) | 88d7bb6211c3299ee2777e061c232c4ed351eb32 | 393 | 1432 | 231 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/agc-large-label-stores](https://github.com/oneandonlydean/AnyPS5/tree/perf/agc-large-label-stores) | 23d67b59a7df3ccc96e388e52bcbd6e7c55ac5cf | 0 | 1493 | 0 | Already in baseline |
| [audit-oneandonlydean/perf/agc-pin-workers-linux](https://github.com/oneandonlydean/AnyPS5/tree/perf/agc-pin-workers-linux) | 604826c138acc1884e406cda5c81184c46a4d32a | 0 | 1493 | 0 | Already in baseline |
| [audit-oneandonlydean/perf/agc-query-entry-points-once](https://github.com/oneandonlydean/AnyPS5/tree/perf/agc-query-entry-points-once) | 2b388e0b0e0069b9fd8a4fbfc75137fba111fb00 | 0 | 1493 | 0 | Already in baseline |
| [audit-oneandonlydean/perf/bda-draw-builds](https://github.com/oneandonlydean/AnyPS5/tree/perf/bda-draw-builds) | 38e07b6e176152d798d1ead74c76053faf0bc751 | 332 | 1961 | 243 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/indirect-draw-ahead](https://github.com/oneandonlydean/AnyPS5/tree/perf/indirect-draw-ahead) | f46f0424f1d7593a050a37d54a66a7bddcc73231 | 334 | 1961 | 244 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/occlusion-in-pass](https://github.com/oneandonlydean/AnyPS5/tree/perf/occlusion-in-pass) | aac83cf2853ac5f3ad59bd6885467e76c350e0c3 | 335 | 1961 | 247 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/recompiler-lds-constant-slots](https://github.com/oneandonlydean/AnyPS5/tree/perf/recompiler-lds-constant-slots) | 31af5a9d2232b9950ecd977c59f2ce29ca175b20 | 0 | 1502 | 0 | Already in baseline |
| [audit-oneandonlydean/perf/recompiler-masked-select-elim](https://github.com/oneandonlydean/AnyPS5/tree/perf/recompiler-masked-select-elim) | 60c655211d5575da28ccbea8a65126fdaeca307e | 0 | 1518 | 0 | Already in baseline |
| [audit-oneandonlydean/perf/rt-proof-memo-38e](https://github.com/oneandonlydean/AnyPS5/tree/perf/rt-proof-memo-38e) | 48d2d0555fff22b6765ad76f91d8376b15f4834f | 335 | 1961 | 243 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/rt-proof-memo-d2a](https://github.com/oneandonlydean/AnyPS5/tree/perf/rt-proof-memo-d2a) | 51b1ed79ce9a07c0655183bc361c82be0f6a56a5 | 325 | 1961 | 240 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/rt-proof-memo-slabs](https://github.com/oneandonlydean/AnyPS5/tree/perf/rt-proof-memo-slabs) | 382b5dff26100810a0c2d14d1be2a6db00fdd455 | 342 | 1961 | 255 | Unverified; keep isolated |
| [audit-oneandonlydean/perf/submit-outside-gpu-mutex](https://github.com/oneandonlydean/AnyPS5/tree/perf/submit-outside-gpu-mutex) | 52570591511b0216e1f1ec052f1cdac259f145fd | 337 | 1961 | 249 | Unverified; keep isolated |
| [audit-oneandonlydean/pr-assets](https://github.com/oneandonlydean/AnyPS5/tree/pr-assets) | 3869aaca7562c8c5ac818544078edc083a9a3552 | — | — | 0 | No shared merge base; not an integration candidate |
| [audit-oneandonlydean/revert/1156-bundled-libc](https://github.com/oneandonlydean/AnyPS5/tree/revert/1156-bundled-libc) | 2096c66a913c49c9545c05b32cece588c12b37f5 | 0 | 376 | 0 | Already in baseline |
| [audit-oneandonlydean/up/address-draw-key](https://github.com/oneandonlydean/AnyPS5/tree/up/address-draw-key) | 74ebeb4f96adfb5971f999d42c0e39903136fcfb | 1 | 649 | 4 | Unverified; keep isolated |
| [audit-oneandonlydean/up/bda-fault-scan](https://github.com/oneandonlydean/AnyPS5/tree/up/bda-fault-scan) | 64d9291cfeacd5754a004551ce045036dc4fa69b | 1 | 649 | 9 | Unverified; keep isolated |
| [audit-oneandonlydean/up/boot](https://github.com/oneandonlydean/AnyPS5/tree/up/boot) | f9233f90042dfeb2f54b427fbc042cd84db68eb5 | 22 | 576 | 35 | Unverified; keep isolated |
| [audit-oneandonlydean/up/collect-memo-newest-first](https://github.com/oneandonlydean/AnyPS5/tree/up/collect-memo-newest-first) | 52446d0b2d6313e7614ad32561cb55185a2514d7 | 1 | 649 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up/depth-alias-on-425](https://github.com/oneandonlydean/AnyPS5/tree/up/depth-alias-on-425) | ad08175eb1030ed737976c5946998123df0560df | 8 | 774 | 14 | Unverified; keep isolated |
| [audit-oneandonlydean/up/flip-throttle](https://github.com/oneandonlydean/AnyPS5/tree/up/flip-throttle) | c3d116b582c314e0e8aa612f747005d1071a9680 | 1 | 577 | 6 | Unverified; keep isolated |
| [audit-oneandonlydean/up/flip-throttle-v2](https://github.com/oneandonlydean/AnyPS5/tree/up/flip-throttle-v2) | 3830ccf7772a379cfb86d511909546de13ac7bb1 | 1 | 479 | 6 | Unverified; keep isolated |
| [audit-oneandonlydean/up/host-import-small-refusal](https://github.com/oneandonlydean/AnyPS5/tree/up/host-import-small-refusal) | d550da6d5b8bdd1470500f29137b509399089363 | 1 | 577 | 4 | Unverified; keep isolated |
| [audit-oneandonlydean/up/integration](https://github.com/oneandonlydean/AnyPS5/tree/up/integration) | e2832f82da668d17c34c72b7ef3f3a2f7f7ed168 | 32 | 574 | 51 | Unverified; keep isolated |
| [audit-oneandonlydean/up/pipeline-cache-bound](https://github.com/oneandonlydean/AnyPS5/tree/up/pipeline-cache-bound) | ce6ea856f20d7c49ff04630a16ff044668970084 | 1 | 649 | 1 | Unverified; keep isolated |
| [audit-oneandonlydean/up/raw-texture-snapshots](https://github.com/oneandonlydean/AnyPS5/tree/up/raw-texture-snapshots) | aba8392d5cd3380178e4f07d1909f5ebc4b6d8f9 | 1 | 401 | 1 | Unverified; keep isolated |
| [audit-oneandonlydean/up/srt-conditional-slots](https://github.com/oneandonlydean/AnyPS5/tree/up/srt-conditional-slots) | 27f13b1e2f21d17d5771d21efbf9f915c40a373c | 1 | 577 | 10 | Unverified; keep isolated |
| [audit-oneandonlydean/up/stack2-base](https://github.com/oneandonlydean/AnyPS5/tree/up/stack2-base) | 0e6b8fc6b22d761058d3ebf9da0fdc78676c3fb4 | 12 | 401 | 31 | Unverified; keep isolated |
| [audit-oneandonlydean/up/waitmemory-race](https://github.com/oneandonlydean/AnyPS5/tree/up/waitmemory-race) | b4029887b45ef390430610ae93578fa46ab8a393 | 0 | 648 | 0 | Already in baseline |
| [audit-oneandonlydean/up639/address-draw-key](https://github.com/oneandonlydean/AnyPS5/tree/up639/address-draw-key) | 74cfd75493665c2314b0dd5bf57627f41b8cd9e0 | 1 | 125 | 4 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/adjusted-regions](https://github.com/oneandonlydean/AnyPS5/tree/up639/adjusted-regions) | ac2d172e0b615aa775a13038666bb4393044de9d | 1 | 93 | 5 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/astro-boot](https://github.com/oneandonlydean/AnyPS5/tree/up639/astro-boot) | ca9b2aa8f78b6cb62ee3ebf5549b8e69162202d4 | 23 | 125 | 49 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/bda-fault-scan](https://github.com/oneandonlydean/AnyPS5/tree/up639/bda-fault-scan) | 063f3cb617d8dbd47bf7640f9524864bf8436b4d | 1 | 125 | 10 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/calls-at-dispatch](https://github.com/oneandonlydean/AnyPS5/tree/up639/calls-at-dispatch) | 10dd4607e8522f4cde23fc90464e2004b4330ec4 | 1 | 93 | 6 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/cmask-gpu-clear](https://github.com/oneandonlydean/AnyPS5/tree/up639/cmask-gpu-clear) | 31cd920fc5501c3b8d1e495ed672fd1943de01ea | 1 | 29 | 18 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/collect-memo-newest-first](https://github.com/oneandonlydean/AnyPS5/tree/up639/collect-memo-newest-first) | 7d1694dcfce7b7b2fbe267e050dd8d758908af37 | 1 | 125 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/depth-bounds-absent-planes](https://github.com/oneandonlydean/AnyPS5/tree/up639/depth-bounds-absent-planes) | 5fbe399899582acf451ff174a86e34125be979e9 | 1 | 93 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/depth-plane-guest-layers](https://github.com/oneandonlydean/AnyPS5/tree/up639/depth-plane-guest-layers) | 42c14e806ac028b0ec76fa2ee105f20733fe36b5 | 24 | 125 | 50 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/depth-plane-guest-layers-on-425](https://github.com/oneandonlydean/AnyPS5/tree/up639/depth-plane-guest-layers-on-425) | 5f0e7304189174bbfc033f37138b06ed15e4e77a | 9 | 225 | 17 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/depth-plane-unchanged-copy-on-425](https://github.com/oneandonlydean/AnyPS5/tree/up639/depth-plane-unchanged-copy-on-425) | 8085ddae5d8326194483da312e50ed9a3d96c702 | 10 | 225 | 17 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/descriptor-web-blocks](https://github.com/oneandonlydean/AnyPS5/tree/up639/descriptor-web-blocks) | 4e13ec18d455742489776e0467d0d69dad190bde | 4 | 130 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/flip-throttle](https://github.com/oneandonlydean/AnyPS5/tree/up639/flip-throttle) | b168e1ded8396d7410d9b68d08290daddab3fc96 | 1 | 125 | 6 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/front-halves](https://github.com/oneandonlydean/AnyPS5/tree/up639/front-halves) | 24cc2170a4b7b9bd52c3686f7e721cbb8b5d3fda | 1 | 93 | 3 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/half-wave-fp-reduce](https://github.com/oneandonlydean/AnyPS5/tree/up639/half-wave-fp-reduce) | 5435cb28e7ebe31849ea5794ca4b655e5d868527 | 1 | 93 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/half-wave-lane-bits](https://github.com/oneandonlydean/AnyPS5/tree/up639/half-wave-lane-bits) | 8a581853063caed40cdfc718716037bd3d3cd0a2 | 1 | 93 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/half-wave-vertex-exec](https://github.com/oneandonlydean/AnyPS5/tree/up639/half-wave-vertex-exec) | c8c90995a05b1fadbefe3cde9447bcb9128da70e | 1 | 93 | 2 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/header-copies](https://github.com/oneandonlydean/AnyPS5/tree/up639/header-copies) | bc1af9dc55e2cbea1c1e5b0416060f619930769f | 1 | 93 | 3 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/image-dimensions](https://github.com/oneandonlydean/AnyPS5/tree/up639/image-dimensions) | df904a0b67dd9d91d111262ac4d8eb61996e622b | 1 | 93 | 7 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/image-heaps](https://github.com/oneandonlydean/AnyPS5/tree/up639/image-heaps) | 1aad65e61c7ee719e3aa59bceb538ae3e72fcad2 | 1 | 93 | 5 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/null-pixel](https://github.com/oneandonlydean/AnyPS5/tree/up639/null-pixel) | 0e9912cdb37f99913d0105912bd78b8317990e85 | 3 | 93 | 5 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/occlusion-in-pass](https://github.com/oneandonlydean/AnyPS5/tree/up639/occlusion-in-pass) | 8dac4e61b0d1367578f5f9e0eb49b0d0bce266cb | 1 | 42 | 9 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/pass-hazards](https://github.com/oneandonlydean/AnyPS5/tree/up639/pass-hazards) | fe1125c8ca5e1132bb79f8ca0a4e28868470b36b | 3 | 125 | 19 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/pending-write-merge](https://github.com/oneandonlydean/AnyPS5/tree/up639/pending-write-merge) | b55375e0c213e35aa068117381a3c5db779a0c94 | 1 | 125 | 3 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/pipeline-cache-bound](https://github.com/oneandonlydean/AnyPS5/tree/up639/pipeline-cache-bound) | 954864ea809f034ed78e034807de18b5d7518972 | 1 | 93 | 1 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/raw-texture-snapshots](https://github.com/oneandonlydean/AnyPS5/tree/up639/raw-texture-snapshots) | d3774bbf733d53426f63d73c2c52963db5070f8c | 1 | 125 | 1 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/resummarize-blits](https://github.com/oneandonlydean/AnyPS5/tree/up639/resummarize-blits) | 24876afca9b533abab19041acc3ad63b537d16a8 | 1 | 93 | 3 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/snapshot-copy-uncollected](https://github.com/oneandonlydean/AnyPS5/tree/up639/snapshot-copy-uncollected) | ad34a79009133dac1b82ab62cd29280e2784def1 | 2 | 125 | 6 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/srt-conditional-slots](https://github.com/oneandonlydean/AnyPS5/tree/up639/srt-conditional-slots) | 83d3010fd6b9248abc52c2d22494a55653720ee1 | 1 | 125 | 10 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/stale-snapshot-reuse](https://github.com/oneandonlydean/AnyPS5/tree/up639/stale-snapshot-reuse) | f4ca36b8757eb99fafea0ef67267dbfbae7f33e1 | 1 | 125 | 4 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/target-key-proof](https://github.com/oneandonlydean/AnyPS5/tree/up639/target-key-proof) | df5a149146da12c8bf757adefd71688f099aa8fa | 1 | 125 | 5 | Unverified; keep isolated |
| [audit-oneandonlydean/up639/unary-special](https://github.com/oneandonlydean/AnyPS5/tree/up639/unary-special) | aa3cff04626c2fa392ebd5f0588efd9737255e12 | 2 | 125 | 7 | Unverified; keep isolated |

Astro Bot Linux and Windows branches each diverge from this baseline by hundreds of commits. Their title-specific reports are third-party evidence only. No commercial title was acquired or tested. Historical Z3R0339, GorramFrakker, ludnix and mjsikorsky main tips are already ancestors of baseline. AidanXVII has two unique commits; no superiority claim is justified.

Windows fiber stack, discrete GPU selection, scissor offset, mapping hints, and MinGW runtime fixes in the SP4C3B4R-8 branches are ancestors of baseline. The aliased-depth-surface branch remains a review candidate. Many oneandonlydean GPU, shader, and performance branches are also ancestors; newer up639 branches remain unverified.


## Ecosystem-wide structural audit

The sharded [full snapshot](fork-snapshot-index.json) covers all 2,451 advertised tips: 2,444 have ancestry/patch/file comparisons; seven are orphan histories (assets, media or handoff notes) with no shared upstream ancestor. The two original snapshot SHAs that moved during acquisition were recovered by exact SHA and compared. Three listed repositories could not be fetched. 995 tips are upstream ancestors. Detailed semantic review remains selective; these counts do not certify every fork. The snapshot includes per-tip changed test files, subsystems, license-file changes and an all-local-ref patch identity/author index for duplicate detection. Dates and commit subjects do not independently prove meaningful functionality.

The broad audit found a useful patch outside the seven priority forks: drk1rd's single-file half-float conversion fix. It was isolated, reviewed and experimentally verified on this machine before retention.
