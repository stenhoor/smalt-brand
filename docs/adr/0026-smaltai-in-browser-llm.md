# ADR 0026: smaltai's in-browser LLM: an inference engine on WebGPU

- **Status:** proposed. The owner's answers of 2026-11-09 are recorded below; the items under "Still to decide" are
  open.
- **Date:** 2026-11-09
- **Builds on:** [ADR 0025](0025-smaltai-agent-gateways-and-actions.md) (smaltai: gateways, actions and context); smalt-brand's
  [DECISIONS.md](../../DECISIONS.md) (outside code: ask first);
  [smaltworks.dev/environments](https://smaltworks.dev/environments) (supported browsers).

## Context

The third part of smaltai (owner, 2026-11-09) is a large language model running in the browser on WebGPU, fetching its
own weights. It is the largest piece of work in smaltai. If it works, the smalt apps become a portable data analytics
platform with AI support that needs no server and sends nothing out of the browser.

The owner also set how it relates to the rest. It is **a harness that runs a model in the browser**, and smaltai
treats it as one more gateway, like llama.cpp's server or the Anthropic API (ADR 0025, section 2). It is **not
required** for smalt: it is a convenience. **Performance is paramount.**

What the platform gives, and where it falls short:

- **WebGPU** fully works for about 87% of users ([Can I use](https://caniuse.com/webgpu), 6 November 2026), almost all of
  them on Chrome and Edge 113 or later. Firefox has it on Windows only, and Safari's support is partial. Elsewhere the
  harness isn't offered, and the user picks another gateway.
- **16-bit floats in shaders** (`shader-f16`) arrived in Chrome 120, on GPUs that support them. Not every GPU does.
- **Buffer limits:** by default a buffer is at most 256 MB and a storage binding at most 128 MB
  ([MDN](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedLimits)). A page may ask for more, up to what the
  GPU's adapter reports. A 2 GB model is split across many buffers either way.
- **Storage:** OPFS can hold multi-gigabyte files (browsers give each origin a share of the free disk), and smaltdb
  already uses it. The apps share one
  origin, so they share a downloaded model (ADR 0025, Context).
- **WGSL has no 64-bit floats** (smaltdb's vectorization review). LLM inference works in 16 and 32 bits, so this is no
  obstacle here.

## Decision

### 1. Our own engine, in TypeScript and WGSL

The engine is our own (owner, 2026-11-09). It doesn't wrap WebLLM, ONNX Runtime Web or Transformers.js, so it adds no
outside code, and we control the kernels, the memory and the fusion, which is where its speed comes from. It runs in a
dedicated worker and offers ADR 0025's gateway interface: a chat request with tools, streamed back.

It contains:

- **The weights loader** (section 4) and **the tokenizer**, in TypeScript on the CPU, reading the vocabulary and merges
  from the model file.
- **The GPU kernels**, in WGSL: matrix products on quantized weights (dequantized inside the kernel), attention with a
  key–value cache, RMS normalization, rotary position embedding, and the activations. They are fused where it saves
  passes over memory. Prompt processing (many tokens at once) and generation (one token at a time) get kernels of their
  own, because they are limited by different things.
- **Sampling:** temperature, top-k and top-p, and **constrained decoding**. When the model calls a tool, the sampler
  allows only tokens that keep the call valid against the tool's input schema, so a small model's tool calls are
  always well-formed.

### 2. Model size: about 3–4 billion parameters

The engine is built to run models of about 3–4 billion parameters well (owner, 2026-11-09). At 4-bit weights that is
about 2 GB to download and hold in GPU memory, enough for usable tool calling on most recent laptops' GPUs. Smaller
models run faster. Larger ones run where the GPU has the memory.

### 3. Weight formats: GGUF, then safetensors

Both formats (owner, 2026-11-09), GGUF first:

- **GGUF:** one file holding the weights, the tokenizer and the model's settings, in the quantized forms llama.cpp
  uses. The engine supports a small set of quantization types and runs them well, rather than all of them.
- **safetensors** later: Hugging Face's format, with the tokenizer and configuration in their own files beside it.

The engine supports named model architectures, starting with one or two (see "Still to decide"), and refuses a file
whose architecture or quantization it doesn't support, with an error that names it.

### 4. Weights come from a URL the user gives

The user points the harness at the weights (owner, 2026-11-09):

- **A URL:** Hugging Face, another host, or a server on the user's own machine or network. The host must allow the
  app's origin (CORS); a local server also meets Chrome's local network prompt (ADR 0025, section 2).
- **Downloaded once,** in ranges, so a broken download resumes. Each file is checked against its size and, where the
  host gives one, its hash.
- **Cached in OPFS** for the origin, so every app on it uses the same copy. The harness asks the browser to keep the
  storage (`navigator.storage.persist()`) and shows what is cached, with sizes, so the user can delete it.
- **The weights' licence is between the user and the model's publisher.** smalt hosts no weights and ships none. The
  harness shows the licence named in the model file, where there is one.

### 5. Performance

Performance is paramount (owner, 2026-11-09). The goal is to **meet or beat WebLLM** running the same model in the same
browser on the same GPU, and to report how close the engine comes to **llama.cpp running natively** on that GPU.

- **Measured:** time to the first token, prompt tokens per second, generated tokens per second, loading time from the
  cache, and peak GPU memory. Each is measured per release, for a fixed set of models and machines.
- **Where the speed comes from:** quantized weights read once per token, fused kernels, few round trips between the CPU
  and the GPU, `shader-f16` and other optional GPU features used where present, and the key–value cache kept on the GPU.
- **CI has no GPU,** so the benchmarks run by hand on named hardware, recorded with their results. CI checks that the
  kernels give the right numbers, on WebGPU's software adapter.
- **No number is published without its benchmark and method** beside it (the brand's rule).

### 6. Where it lives

A package of its own, separate from `@smaltworks/smaltai`, so the agent package stays small. smaltai loads it only
when the user picks the in-browser gateway. Its name is open: the owner called it "llama.ts, or whatever we want to call
it". It gets its own repository when the work starts; until then this record lives in smalt-brand (owner, 2026-11-09).

### 7. Order of work

1. **A first end-to-end run:** one architecture, one quantization type, a GGUF from a URL, cached in OPFS, generating
   text. This proves the loader, the tokenizer and the kernels together.
2. **Speed:** kernels tuned until generation meets the WebLLM goal on the reference machines.
3. **Tool calling:** chat templates, constrained decoding and the gateway interface, so smaltai can use it.
4. **safetensors** and more architectures.

## Consequences

- **An optional, offline AI for smalt.** With the in-browser gateway, the model, the data and the work all stay in the
  browser.
- **Only where WebGPU is.** Chrome and Edge users get it today. Others use another gateway, and the apps work the same
  without it.
- **A large engine of our own** to build and keep fast: kernels per GPU feature set, a tokenizer, two file formats, and
  each architecture added. This is the bulk of smaltai's work.
- **Downloads are big.** About 2 GB on first use, once per origin. The user sees the size before it starts.
- **Benchmarks need real hardware,** outside CI.

## Still to decide

1. **The name** of the engine (a brand decision).
2. **The first architecture or two,** for example the Llama and Qwen families, and the quantization types (for
   example Q4_K and Q8_0).
3. **A fallback without WebGPU:** none (the recommendation, since running on the CPU would be too slow to be useful), or
   a CPU path for small models.
4. **The WebLLM comparison:** running WebLLM for benchmarks is outside code in development, so it needs the owner's yes
   (the family rule). It is never part of a package.
