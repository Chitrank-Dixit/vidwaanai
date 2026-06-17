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

### Verse 1 (Mahabharat 0.5471)
- **Original**: भीमसेन, सात्यकि और माद्रीननदन सहदेव झल्यपर दूट पड़े। सायकोंकी सहस्रों धाराएँ बरस रही थीं। पहले दुर्योधनने ही सेनापति शल्यने तुरंत ही उन सबका सामना किया। उन्होंने धृष्टमुप्रको पाँच बाण मारे, तब धृष्टशयुप्नने भी सत्तर बाण युधिष्ठिको तीन, भीमसेनको पाँच, सात्यकिको सौ और मारकर दुर्वोधनको वि्षेष पीड़ा पहुँचायी। यह देख उसके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5471)
- **Original**: भीमसेन, सात्यकि और माद्रीननदन सहदेव झल्यपर दूट पड़े। सायकोंकी सहस्रों धाराएँ बरस रही थीं। पहले दुर्योधनने ही सेनापति शल्यने तुरंत ही उन सबका सामना किया। उन्होंने धृष्टमुप्रको पाँच बाण मारे, तब धृष्टशयुप्नने भी सत्तर बाण युधिष्ठिको तीन, भीमसेनको पाँच, सात्यकिको सौ और मारकर दुर्वोधनको वि्षेष पीड़ा पहुँचायी। यह देख उसके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5472)
- **Original**: सहदेवको तीन बाणोंसे बींध डाला। भाइयोंने बहुत बड़ी सेताके साथ आकर धुृष्टययुम्नको चारों
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5472)
- **Original**: सहदेवको तीन बाणोंसे बींध डाला। भाइयोंने बहुत बड़ी सेताके साथ आकर धुृष्टययुम्नको चारों
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5473)
- **Original**: इसके बाद मद्राजने क्षुझ्र मारकर नकुलके धनुषकों ओरसे घेर लिया। घिर जानेपर भी बह अखा-संचालनमें
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5473)
- **Original**: इसके बाद मद्राजने क्षुझ्र मारकर नकुलके धनुषकों ओरसे घेर लिया। घिर जानेपर भी बह अखा-संचालनमें
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5474)
- **Original**: काट दिया। तब नकुलने तुरंत ही दूसरा धनुष लेकर अपने हाथोंकी फुर्ती दिखाता हुआ युद्धमें निर्भभ विचर
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5474)
- **Original**: काट दिया। तब नकुलने तुरंत ही दूसरा धनुष लेकर अपने हाथोंकी फुर्ती दिखाता हुआ युद्धमें निर्भभ विचर
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5475)
- **Original**: झल्यके रथकों बाणोंसे भर दिया। साथ हो, युधिष्ठिर रहा था।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5475)
- **Original**: झल्यके रथकों बाणोंसे भर दिया। साथ हो, युधिष्ठिर रहा था।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5476)
- **Original**: और सहदेवने भी उनकी छातीमें दस-दस बाण मारे। फिर दूसरी ओर झिखण्डी अपने साथ प्रभव्रकॉंकी सेना
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5476)
- **Original**: और सहदेवने भी उनकी छातीमें दस-दस बाण मारे। फिर दूसरी ओर झिखण्डी अपने साथ प्रभव्रकॉंकी सेना
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5477)
- **Original**: भीमसेनने साठ और सात्यकिने दस सायकोंसे उन्हें घायल लेकर कृपाचार्य और कृतवर्मासे युद्ध कर रहा था। वहाँ भी
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5477)
- **Original**: भीमसेनने साठ और सात्यकिने दस सायकोंसे उन्हें घायल लेकर कृपाचार्य और कृतवर्मासे युद्ध कर रहा था। वहाँ भी
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5478)
- **Original**: कर दिया। अब मद्रराजने क्रोधमें भरकर सात्यकिकों पहले ब्राणोंकी बाजी लगाकर भयंकर संप्राम हो रहा था। इधर,
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5478)
- **Original**: कर दिया। अब मद्रराजने क्रोधमें भरकर सात्यकिकों पहले ब्राणोंकी बाजी लगाकर भयंकर संप्राम हो रहा था। इधर,
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5479)
- **Original**: नौ और फिर सत्तर बाणोंसे बींघ डाला। इसके बाद उसके राजा झल्य बाणोंको झड़ी लगाकर सात्यकि तथा
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5479)
- **Original**: नौ और फिर सत्तर बाणोंसे बींघ डाला। इसके बाद उसके राजा झल्य बाणोंको झड़ी लगाकर सात्यकि तथा
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5480)
- **Original**: धनुषको काटकर रथके घोड़ोंको भी मौतके घाट उतार भीमसेनसहित समस्त पाण्डबोंको पीड़ित कर रहे थे। साथ
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5480)
- **Original**: धनुषको काटकर रथके घोड़ोंको भी मौतके घाट उतार भीमसेनसहित समस्त पाण्डबोंको पीड़ित कर रहे थे। साथ
- **Translation**: 

---

