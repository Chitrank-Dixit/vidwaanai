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

### Verse 1 (Mahabharat 0.4421)
- **Original**: बृहस्पति और शुक्रके समान नीतिकुझल और बड़े ही दुःसह मोहजारू छा गया कि उन्होंने उनकी कुछ भी परवा नहीं की ।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4421)
- **Original**: बृहस्पति और शुक्रके समान नीतिकुझल और बड़े ही दुःसह मोहजारू छा गया कि उन्होंने उनकी कुछ भी परवा नहीं की ।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4422)
- **Original**: थे; तो भी झख्त्र उनकी रक्षा नहीं कर सके । इस समय , कर्णके कूच करनेपर सब राजाओंने जयघोष किया। तब कर्णने सजा झल्यको सम्बोधन कस्के कहा, 'इस समय मैं अख्-झख्र धारण किये रथमें बैठा हूँ, आब मुझे क्रोधमें भरे हुए वज़धर इन्रले भी भय नहीं है। इन भीष्यादि थोद्धाओंको युद्धमें सोते देखकर मेरा साहस बहुत बढ़ गया है। वास्तवमें अर्जुनका मुकाबल्म रणभूमिमें मेरे सिवा और कोई नहीं कर सकता
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4422)
- **Original**: थे; तो भी झख्त्र उनकी रक्षा नहीं कर सके । इस समय , कर्णके कूच करनेपर सब राजाओंने जयघोष किया। तब कर्णने सजा झल्यको सम्बोधन कस्के कहा, 'इस समय मैं अख्-झख्र धारण किये रथमें बैठा हूँ, आब मुझे क्रोधमें भरे हुए वज़धर इन्रले भी भय नहीं है। इन भीष्यादि थोद्धाओंको युद्धमें सोते देखकर मेरा साहस बहुत बढ़ गया है। वास्तवमें अर्जुनका मुकाबल्म रणभूमिमें मेरे सिवा और कोई नहीं कर सकता
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4423)
- **Original**: यह साक्षात्‌ उप्ररूप मृत्थुके ही समान है। आचार्य ग्रेणमें शद्ससंचालनकी कुझलता, बल, पैर्य दुर्योधनका पुरुषार्थ ढीला पड़ गया है; ऐसी स्थितिमें मैं अपना
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4423)
- **Original**: यह साक्षात्‌ उप्ररूप मृत्थुके ही समान है। आचार्य ग्रेणमें शद्ससंचालनकी कुझलता, बल, पैर्य दुर्योधनका पुरुषार्थ ढीला पड़ गया है; ऐसी स्थितिमें मैं अपना
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4424)
- **Original**: कर्त्तव्य अच्छी तरह समझता हूँ। अब आप झनरुओंकी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4424)
- **Original**: कर्त्तव्य अच्छी तरह समझता हूँ। अब आप झनरुओंकी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4425)
- **Original**: सेनाकी ओर रथ बढ़ाइये। जहाँ सत्पप्रतिज्ञ राजा युधिष्ठिर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4425)
- **Original**: सेनाकी ओर रथ बढ़ाइये। जहाँ सत्पप्रतिज्ञ राजा युधिष्ठिर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4426)
- **Original**: बीर और नकुल-सहदेव युद्धके मैदानमें डटे हुए हैं, वहाँ मेरे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4426)
- **Original**: बीर और नकुल-सहदेव युद्धके मैदानमें डटे हुए हैं, वहाँ मेरे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4427)
- **Original**: सि्रा और कौन योद्धा इन सब वीरोंसे टक्कर ले सकता हैं ?
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4427)
- **Original**: सि्रा और कौन योद्धा इन सब वीरोंसे टक्कर ले सकता हैं ?
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4428)
- **Original**: इसलिये मद्रराज ! आप झौघ्र ही रणभूमिमें पाज्ञाल, पाण्डल
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4428)
- **Original**: इसलिये मद्रराज ! आप झौघ्र ही रणभूमिमें पाज्ञाल, पाण्डल
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4429)
- **Original**: और सृक्ञय वीऐेंकी ओर रथ ले चलिये। मैं उनके साथ चार
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4429)
- **Original**: और सृक्ञय वीऐेंकी ओर रथ ले चलिये। मैं उनके साथ चार
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4430)
- **Original**: र2े संक्षिप्ष महाभारत [ कर्णपर्व हाथ करके या तो उन्हींको मार डारूँगा-या आचार्य ड्रेणके
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4430)
- **Original**: र2े संक्षिप्ष महाभारत [ कर्णपर्व हाथ करके या तो उन्हींको मार डारूँगा-या आचार्य ड्रेणके
- **Translation**: 

---

