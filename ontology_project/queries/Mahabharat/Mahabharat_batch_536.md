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

### Verse 1 (Mahabharat 0.5351)
- **Original**: आप इस समय महारथी झल्यपर चढ़ाई कीजिये। समझकर उनपर दया कसनेकी आवश्यकता नहीं है, क्षत्रिय-धर्मको सामने रखकर उम्हें मार ही डालिये। संप्राममें आप अपना तपोबलल और क्षात्रबलल दिखाइये।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5351)
- **Original**: आप इस समय महारथी झल्यपर चढ़ाई कीजिये। समझकर उनपर दया कसनेकी आवश्यकता नहीं है, क्षत्रिय-धर्मको सामने रखकर उम्हें मार ही डालिये। संप्राममें आप अपना तपोबलल और क्षात्रबलल दिखाइये।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5352)
- **Original**: महारधी झल्यकों अवश्य मार डालिये। यह कहकर भगवान्‌ श्रीकृष्ण पाण्डबोंसे सम्मानित हो
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5352)
- **Original**: महारधी झल्यकों अवश्य मार डालिये। यह कहकर भगवान्‌ श्रीकृष्ण पाण्डबोंसे सम्मानित हो
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5353)
- **Original**: बिश्रामके लिये अपने शिविरमें चले गये। उनके जानेके बाद
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5353)
- **Original**: बिश्रामके लिये अपने शिविरमें चले गये। उनके जानेके बाद
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5354)
- **Original**: राजा युधिष्ठिरे सब भाइयों, पाञ्चाक्लों और सोमकोंको
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5354)
- **Original**: राजा युधिष्ठिरे सब भाइयों, पाञ्चाक्लों और सोमकोंको
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5355)
- **Original**: भी बिदा किया। फिर सबने अपने-अपने शिविरमें सोकर झल्यको बहुत अच्छी तरह जानता हूँ। वे अत्यन्त पराक्रमी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5355)
- **Original**: भी बिदा किया। फिर सबने अपने-अपने शिविरमें सोकर झल्यको बहुत अच्छी तरह जानता हूँ। वे अत्यन्त पराक्रमी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5356)
- **Original**: शात बिततायी। > ,णन्‍न्‍ारजुरे य__« शल्यके सेनापतित्वमें युद्धछं आरम्भ और नकुलद्वारा कर्णके शेष तीनों पुत्रोंका वध सजय कहते हैं--महाराज! यह रात बीत जानेपर
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5356)
- **Original**: शात बिततायी। > ,णन्‍न्‍ारजुरे य__« शल्यके सेनापतित्वमें युद्धछं आरम्भ और नकुलद्वारा कर्णके शेष तीनों पुत्रोंका वध सजय कहते हैं--महाराज! यह रात बीत जानेपर
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5357)
- **Original**: दी। इसी तरह पाण्डल भी सेनाका व्यूह बनाकर युद्धकी दुर्मोधनने आपके सब सैनिकॉंको आज्ञा दी--'अब सब
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5357)
- **Original**: दी। इसी तरह पाण्डल भी सेनाका व्यूह बनाकर युद्धकी दुर्मोधनने आपके सब सैनिकॉंको आज्ञा दी--'अब सब
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5358)
- **Original**: महारथी तैयार हो जायें।' राजाकी आज्ञा पाकर सारी सेना कब्ज आदिसे सुसज्जित हो गयीं। बाजे बजने लगे।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5358)
- **Original**: महारथी तैयार हो जायें।' राजाकी आज्ञा पाकर सारी सेना कब्ज आदिसे सुसज्जित हो गयीं। बाजे बजने लगे।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5359)
- **Original**: योदधाओंका सिंहनाद होने छगा। उस समय मरनेसे बचे हुए
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5359)
- **Original**: योदधाओंका सिंहनाद होने छगा। उस समय मरनेसे बचे हुए
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5360)
- **Original**: आपके सैनिक मौतकी परवा न करके रणभूमिकी ओर कूच करते दिखायी देने लगे। मद्रराज झल्यको सेनाका नायक बनाकर महारथ्ियोने सम्पूर्ण सेनाके कई विभाग किये और
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5360)
- **Original**: आपके सैनिक मौतकी परवा न करके रणभूमिकी ओर कूच करते दिखायी देने लगे। मद्रराज झल्यको सेनाका नायक बनाकर महारथ्ियोने सम्पूर्ण सेनाके कई विभाग किये और
- **Translation**: 

---

