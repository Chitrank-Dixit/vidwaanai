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

### Verse 1 (Vaivtpuran 13.18617)
- **Original**: सर्वसम्पद्विधात्री या देवीनां च॒ परात्पा । करोति सततं लक्ष्मी: केशैस्त्वत्पादमार्जनम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.18618)
- **Original**: प्रकृतिबीजरूपा सा सर्वेषां शक्तिरूपिणी । स्मार॑ स्मारं त्वत्पदाब्ज॑ बभूव तत्यरा बवरा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.18619)
- **Original**: पार्वती सर्वरूपा सा सर्वेषां बुद्धिरूपिणी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.18620)
- **Original**: त्वत्याइसेवया कान्त॑ ललाभ शिवषभीश्चरम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.18621)
- **Original**: विद्याश्चिष्ठात्री देवी या ज्ञानमाता सरस्वती
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.18622)
- **Original**: पूज्या बभूब सर्वेषां सम्पूज्य त्वत्पदाम्बुजम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.18623)
- **Original**: सावित्री वेदजननी पुनाति भुवनत्रयम्‌ । ख्रह्मणो ख्राह्मणानां चर मतिस्त्वत्पादसेबया
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.18624)
- **Original**: क्षमा जगद्‌ विभर्तु च रलगर्भा वसुन्धरा । प्रसूति: सर्वशस्थानां. त्वत्पादपद्मसेवया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.18625)
- **Original**: राधा समांशसम्भूता तब तुल्या च तेजसा । स्थित्वा वक्षसि ते पार्द सेवतेउन्यस्थ का कथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.18626)
- **Original**: यथा शर्वादयो देवा देव्यः पद्मादयो यथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.18627)
- **Original**: सनाथं कुरु मापीश ईश्वरस्थ समा कृषा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.18628)
- **Original**: न यास्थाम्ति गृहं नाथ न गृद्दामि धन तब । कृत्वा मां रक्ष पादाब्जसेवायां सेवक रतम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.18629)
- **Original**: इति स्तुत्वा साथ्रुनेत्र: पपात चरणे हरे: । रुरोद चर भृशं भक्त्या पुलकाख्ितविग्रहः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.18630)
- **Original**: गर्गस्थ बचर्न श्रुत्वा जहास भक्तवत्सलः। उवाच त॑ स्वयं कृष्णो मयि ते भक्तिरस्त्विति
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.18631)
- **Original**: इदं गर्गकृत॑ स्तोत्र त्रिसंध्य॑ यः पठेन्नर: । दृढां भक्ति हरेदास्यं स्मृति च लभते ध्रुबम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.18632)
- **Original**: जन्ममृत्युजरारोगशोकमोहादिसड्डूटात्‌ । तीर्णोीा. भवति श्रीकृष्णदाससेवनतत्पर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.18633)
- **Original**: कृष्णस्य सह काल॑ च कृष्णसार्ध चर मोदते। कदाचिन्न भवेत्‌ तस्य विच्छेदो हरिणा सह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.18634)
- **Original**: ज्ति शभ्रीब्रह्मवैवर्तें गर्यक्ृतं श्रीकृष्णस्तोत्र सम्पूर्णय्‌। (श्रीकृष्णजन्मखण्ड 13। 193--218) #24/++>> ्विशयेफस050+2++
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6631)
- **Original**: + गणपतिखण्ड + 327 घघघघ]4]42280200287)807 8] 8] 8 ो22 222 2 8 4 6 4
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6632)
- **Original**: &#&#&####%%%$%% 555 # ## जाय। भाई! कर्मानुसार जिनका जिन-जिन योनियोंमें
- **Translation**: 

---

