# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.7381)
- **Original**: भगवज्नस्माकमन्न बिरोधे कतरः पक्षों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7382)
- **Original**: हम दोनोंकि पारस्परिक कलहमें कौन-सा पक्ष जीतेगा 7" जेता भविष्यतीति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7383)
- **Original**: अथाह भगवान्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7384)
- **Original**: तब भगवान्‌ ब्रह्माजी योले---”'जिस पक्षकी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7385)
- **Original**: येषामर्थे रजिरात्तायुधो योत्स्यति तत्पक्षो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7386)
- **Original**: ओरसे राजा रजि झास्त्र धारणकर युद्ध करेगा उसी पक्षकी जेतेति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7387)
- **Original**: खिजय होगी'”
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7388)
- **Original**: आ09 ] अथ दैत्यैस्पेत्प रजिरात्मसाहाय्वदाना- याभ्यर्थितः प्राह
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7389)
- **Original**: थोस्स्ेफह॑भवतामर्थे यहाहममरजयाझबतामिन्द्रे भविष्या- मीत्याकण्यैंतसैरभिहितम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7390)
- **Original**: न वयमन्यथा वदिष्यामोउन्यथा करिष्यामो5स्माकमिन्द्र: प्रह्माद- स्तदर्थमेवायमुद्यम यश अपफाम रहुजस गदर देवैरप्य- साववनिपतिरेवमेवोक्तस्तेगनापि च् देवैरिन्रस्त्वे भविष्यसीति समन्वीप्सितम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7391)
- **Original**: रजिनापि देवसैन्यसहायेनानेकैर्महास््र- स्तदशेषमहासुरबल निषूदितम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7392)
- **Original**: _ अथ जितारिपक्षक्ष देवेद्यों रजिचरणयुगलमात्मन: शिरसा निपीड्याह
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7393)
- **Original**: भयत्राणादतन्नदाना- उवानस्मत्पिता5शेषस्त्रेकानामुत्तमोत्तमो भवान्‌ यस्पाईं पुत्रखिलोकेन्द्र:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7394)
- **Original**: स॒चापि राजा प्रहस्याह
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7395)
- **Original**: एव- मस्त्वेबमस्त्वनतिक्रमणीया हि वैरिपक्षादप्यनेक- विश्चचाटुवाक्यगर्भा प्रणतिरित्युक्त्वा जगाम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7396)
- **Original**: शतक्रतुरपीद्धत्व॑ चकार
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7397)
- **Original**: स्वयति तु रजौ नारदर्षिचोदिता रजिपुतन्नाइशतक्रतुमात्म- पितृपुत्र॑समाचाराद्राज्य॑ याचितबन्तः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7398)
- **Original**: अप्रदानेन भ्॒ विजित्येन्द्रमतियलिन: स्वयमिन्द्रत्व चक्कु:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7399)
- **Original**: ततश्न बहुतिथे काले ह्ातीते बृहस्पतिमेकान्ते दृष्ठा अपहतजत्रैल्लेक्ययज्ञभाग: शतक्रतुरुवाच
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7400)
- **Original**: बदरीफलमात्रमप्यहसि ममाप्यायनाय पुरोडाशखण्ड दातुमित्युक्तो यृहस्पतिरुवाच
- **Translation**: 

---

