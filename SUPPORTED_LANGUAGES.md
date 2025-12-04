# Supported Languages in Vidwaan AI

Vidwaan AI currently supports the following languages and dialects for processing, analysis, and RAG operations.

## Core Languages
| Language | Code | Processor |
|----------|------|-----------|
| **English** | `en` | Default (N/A) |
| **Hindi** | `hi` | `HindiProcessor` |
| **Sanskrit** | `sa` | (Implicit support via Devanagari) |

## Regional Languages
| Language | Code | Processor |
|----------|------|-----------|
| **Bengali** | `bn` | `BengaliProcessor` |
| **Gujarati** | `gu` | `GujaratiProcessor` |
| **Kannada** | `kn` | `KannadaProcessor` |
| **Malayalam** | `ml` | `MalayalamProcessor` |
| **Marathi** | `mr` | `MarathiProcessor` |
| **Tamil** | `ta` | `TamilProcessor` |
| **Telugu** | `te` | `TeluguProcessor` |

## Dialects & Other Languages
| Language | Code | Processor | Features |
|----------|------|-----------|----------|
| **Bhojpuri** | `bho` | `BhojpuriProcessor` | Tokenizer, Normalizer, Morphology, Stress, Dialect Classification (Northern/Southern/Western) |
| **Maithili** | `mai` | `MaithiliProcessor` | Tokenizer, Normalizer, Morphology, Dialect Classification (Sotipura/Angika/Bajjika) |
| **Rajasthani** | `raj` | `RajasthaniProcessor` | Tokenizer, Normalizer |
| **Haryanvi** | `bgc` | `HaryanviProcessor` | Basic Support |
| **Chhattisgarhi** | `hne` | `ChhattisgarhiProcessor` | Basic Support |
| **Dogri** | `doi` | `DogriProcessor` | Basic Support |
| **Konkani** | `kok` | `KonkaniProcessor` | Basic Support |

## Language Detection
Language detection is handled by `LanguageDetector` using `langdetect` with custom mapping for dialects.
