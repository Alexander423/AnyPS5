# Performance evidence

No application FPS, GPU frame time, shader-cache benefit, memory leak or performance improvement is claimed. No guest application has been executed. Relinker wall time in compatibility JSON is conversion duration under concurrent build load and is not a controlled benchmark.

Regression sharding addressed a test timeout; it is not an emulator speed claim. Establish cold/warm shader and pipeline-cache baselines only after correctness, using identical inputs, commits, driver, clocks, resolution and instrumentation. Record CPU/GPU frame distributions, memory peaks and validation status. Preserve the general Vulkan path when investigating RDNA2-specific changes.
