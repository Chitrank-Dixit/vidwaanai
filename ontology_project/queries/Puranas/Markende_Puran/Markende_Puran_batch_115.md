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

### Verse 1 (Markende Puran 0.2281)
- **Original**: शहिं संघ्याक्े और कान जायुके तेजसे उत्पन्न हुए थे। अपायतातिमहता प्रतिशव्दो महानभूत्‌। इसी प्रकार आन्यान्य देवताओंके तेजसे भी उस, चुक्षुभु: सक्कला लोका: समुद्रा् चक्तम्पिरे
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2282)
- **Original**: कल्याणमयी देवीक। आबिर्भाव हुआ
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2283)
- **Original**: सतत: समस्तदेखानां तेजोराशिसमुद्धवाम्‌। तां विलोक्य मुर्द प्रापुरमरा महिषादिता;
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2284)
- **Original**: शूल॑ शूलाद्विविष्फृष्य ददो तस्थे पिनाकक्ृक । चकं च दत्तत्ान्‌ कृष्ण: समुत्पाद्य स्वचक्रत:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2285)
- **Original**: श्भुं च चरुण: शक्ति ददौ तस्यै हुलाशन:। मारुतो दक्तजाँआपं बाणपूर्णे तश्रेषुधी
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2286)
- **Original**: खज़मिन्द्र: कुलिशादमराधिप;
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2287)
- **Original**: दी तस्ये सहस्याक्षो घण्टापैरावत्ताद्‌ गजात्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2288)
- **Original**: 22 4 कालदण्डाझ्ममों दण्ड पाश॑ तजाम्बुपतिर्ददी। प्रजापतिशभ्षाक्षमालां ददौ ब्रह्मा क़मण्डलुमू
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2289)
- **Original**: सपमस्तरोगकृपेषु दिवाकरः:। कालश्न 8:08 विखनक त्ञ निर्मलम्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2290)
- **Original**: क्षीरोदशआमल॑ हारमजरे ता तथाम्बरे। चूडामणिं तथा दिव्बं कुण्डले कटकानि ज्
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2291)
- **Original**: अर्धचर्द्धट तथा पुभ॑ केयूगान्‌ सर्वयाहुपु। नूपुरी बिमली तट्ठ॒दे ग्रेवेबकमनुत्तमम्‌
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2292)
- **Original**: अड्युलीयकरब्रानि समस्तास्वद्डलीषु ज। विश्वकर्मा दृदी तस्येँ परशुं चातिनिर्षलम्‌
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2293)
- **Original**: अस्त्राण्यनेकरूपाणि तथाभेद्यं च दंशनम्‌। चत्नाल वसुथा चेलु:ः सकलाश्ष महोथरा:। जयेति देवा: मुदा त्ममूचु: सिंहवाहिनीम 434
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2294)
- **Original**: तुष्ठ॑चुर्मुनबश्चैनां भक्तिनप्रात्मपूर्तव:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2295)
- **Original**: तदनन्तर समस्त देवताओंके तेज:पुञ्लले प्रकट हुई देवीको देखकर महियासुरके सताये छुए देवता बहुत प्रसन्न हुए
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2296)
- **Original**: पिनाकथारी भगवान्‌ शड्ूरने अपने शूलसे एक शूल निकालकर उन्हें दिया; फिर भगवान्‌ विष्णुने भो अपने चक्रसे चक्र उत्पन्न करके भगवतीकों अर्पण किया
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2297)
- **Original**: बरुणने भी शह्डु भेंट किया, अग्निने उन्हें शक्ति दी और वायुने धनुष तथा बाणसे भरे हृए दो तरकस प्रदान किय्रे
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2298)
- **Original**: सहस नेत्रोंवाले देवराज इत्घने अपने बज्जसे ठज् उत्पन्न करके दिया और ऐशबत हाथीसे उतारकर एक घण्टा भी प्रदान किया
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2299)
- **Original**: यमगजने कालदण्डसे दण्ड, बरुणने पाश, प्रजापतिने स्फटिकाक्षकों माला तथा अह्ाजोने कम"0डलु भेंट क्रिब।
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2300)
- **Original**: सूर्यने देवीके समस्त रोम-कृपोंमें अपनी किरणोंदा तेज भर दिया। काले उन्हें चमकतों हुईं ढाल और तलवार दी
- **Translation**: 

---

