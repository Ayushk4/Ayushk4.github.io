---
layout: project
title: "llama-int4-quant: 4-bit LLaMA Inference on a Laptop CPU"
date: 2023-03-09
permalink: /projects/llama-int4-quant/
summary: "LLaMA with 4-bit weights generating text on a MacBook CPU in C/C++, shown publicly on March 10, 2023 (UTC), two weeks after LLaMA was announced."
authors: ["Ayush Kaushal"]
venue: "Nolano"
links:
  - {label: Code, url: "https://github.com/NolanoOrg/llama-int4-quant"}
byline_in_body: true  # the post's first lines carry author, venue and links, so the header shows only title and date
---

**Ayush Kaushal** · Nolano · March 2023
[Code (archived)](https://github.com/NolanoOrg/llama-int4-quant) · [Demo videos](#demo) · [Follow-up write-up](https://nolanoorg.substack.com/p/int-4-llama-is-not-enough-int-3-and)

Meta announced LLaMA on February 24, 2023. On March 9, LLaMA-7B was generating text on a MacBook CPU from 4-bit weights, using a C/C++ implementation I wrote on top of Georgi Gerganov's [ggml](https://github.com/ggerganov/ggml) library. Nolano posted videos of it running that evening. The repository called itself a proof of concept, not for production use, and that is what it was: a demonstration that a 7B-parameter LLaMA model could run on a laptop, without a GPU and without PyTorch at inference time.

## What it did

- **Model:** LLaMA-7B (32 layers, hidden size 4096, 32 heads, vocabulary of 32,000), the configuration documented in the repository. Nolano's launch post on March 11 reported 4-bit inference of LLaMA models as large as 13B on personal hardware at more than 12 tokens per second.
- **Weights:** round-to-nearest 4-bit quantization in ggml's Q4_0 format. Each block of 32 weights stores 4-bit codes plus one 32-bit scale, which is 5 bits per weight, about 3.2× smaller than FP16.
- **Hardware:** the CPU of a MacBook or iMac, using ggml's SIMD kernels. No GPU.
- **Pipeline:**
  1. Convert the PyTorch checkpoint to ggml format.
  2. Quantize it to 4 bits.
  3. Run the C/C++ inference binary. Prompts are tokenized by a short Python script and piped into the binary.

## Demo {#demo}

Nolano posted five videos of the implementation running on X between 03:06 and 03:21 UTC on March 10, 2023, the evening of March 9 in US Central time.

<video controls preload="metadata" playsinline poster="/assets/projects/llama-int4-quant/demo-1634027966651834370.jpg" style="max-width:100%">
  <source src="/assets/projects/llama-int4-quant/demo-1634027966651834370.mp4" type="video/mp4">
</video>

*Posted by @NolanoOrg on X at 03:06 UTC, March 10, 2023 ([original](https://x.com/NolanoOrg/status/1634027966651834370)).*

| Posted (UTC, March 10, 2023) | Video |
|---|---|
| 03:06 | [x.com/NolanoOrg/status/1634027966651834370](https://x.com/NolanoOrg/status/1634027966651834370) |
| 03:09 | [x.com/NolanoOrg/status/1634028566013698048](https://x.com/NolanoOrg/status/1634028566013698048) |
| 03:13 | [x.com/NolanoOrg/status/1634029694642257921](https://x.com/NolanoOrg/status/1634029694642257921) |
| 03:19 | [x.com/NolanoOrg/status/1634031068574621702](https://x.com/NolanoOrg/status/1634031068574621702) |
| 03:21 | [x.com/NolanoOrg/status/1634031719652237315](https://x.com/NolanoOrg/status/1634031719652237315) |

## What I built, and what it built on

ggml already had what LLaMA needed for low-bit inference: a tensor library with CPU kernels and, on its experimental `gq` branch, 4-bit quantization formats with SIMD routines (developed between February 21 and 27, 2023). That branch had been used for 4-bit GPT-2, GPT-J and Whisper. It had no support for LLaMA's architecture.

I added that support:

- **Operators in ggml:** the SiLU activation and RMSNorm (March 4), then LLaMA's variant of rotary position embeddings and RMSNorm's epsilon of 10⁻⁶ (March 9). The March 9 changes landed in the same commit that first produced correct text.
- **The LLaMA model in ggml:** the forward pass, weight loading and the generation loop.
- **Tooling:** conversion from the PyTorch checkpoint, a 4-bit quantizer for LLaMA's weights, and an export of the 32,000-token vocabulary.

## Timeline

All times are UTC, from the public git histories.

| Date (2023) | Event |
|---|---|
| Feb 24 | Meta announces LLaMA. |
| Feb 21 to 27 | 4-bit quantization developed on ggml's `gq` branch. |
| Mar 4 | SiLU and RMSNorm added to ggml; a first LLaMA forward pass runs. |
| Mar 6 | The `gq` branch merged in; a 4-bit quantizer written for LLaMA weights. |
| **Mar 9, 07:32** | **"LLaMa finally works": correct text from 4-bit LLaMA-7B on a MacBook CPU.** |
| **Mar 10, 03:06 to 03:21** | **Nolano posts five demo videos on X.** |
| Mar 10, 18:40 | llama.cpp is first released. |
| Mar 11, 02:23 | The repository gets its README, vocabulary file and MIT license. |
| Mar 11, 03:31 | Nolano's launch post links the code. |
| Mar 13 | Nolano publishes a follow-up study of 3-bit and 4-bit quantization. |
| Mar 16 | Nolano's next project switches to llama.cpp. |

By early March, others had run LLaMA locally in PyTorch: in 32-bit on CPU, and in 8-bit and 4-bit on GPUs. What this project added was 4-bit inference on a laptop CPU in C/C++.

## What came next

**Lower bit widths.** On March 13 we published [Int-4 LLaMa is not enough: Int-3 and beyond](https://nolanoorg.substack.com/p/int-4-llama-is-not-enough-int-3-and). It applied GPTQ to LLaMA-7B and 13B at 3 and 4 bits, in both of ggml's 4-bit storage formats (with and without a stored zero offset) and with several block sizes.

**Moving to llama.cpp.** By mid-March, llama.cpp ran LLaMA at nearly the same speed and output quality on a MacBook, and also supported Linux and Windows. Our next project, InstructLLaMa.cpp (March 16), was built on it, and llama-int4-quant was archived so that development would consolidate in one place.

**Fewer bits since then.** I kept working on fewer bits per weight, but by training models that are low-bit from the start rather than compressing them afterwards. That work became [Spectra](/projects/spectra/), a suite of ternary language models, and [TriTera](/projects/spectra-1-1/), which added 1.6-bit and 2-bit packings for ternary weights. Those packings were merged into llama.cpp in September 2024 as the TQ1_0 and TQ2_0 formats.
