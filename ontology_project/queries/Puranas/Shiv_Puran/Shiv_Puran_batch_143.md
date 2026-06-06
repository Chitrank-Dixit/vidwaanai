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

### Verse 1 (Shiv Puran 0.2841)
- **Original**: वान्त्यात्मक मस्तस॑स्थे झम्मो: पादा्चने रतम्‌
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2842)
- **Original**: हा] + संक्षिप्त छिव-चरणार्जन-परायण, हिलत्रक्रे ब्रीजॉमें भ्रथम और कलूाओंमें च्ञार कल्ठाओंसे युक्त है, मैंने पूर्वदिज्ञामें भक्तिभावसे झक्तिसहित जिसका पूजन किया है, वह पवित्र परब्रह्म झिव मेरी प्रार्थना सफल करे
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2843)
- **Original**: 30--42
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2844)
- **Original**: । अज्ञनादिप्रत्तीकाशमघोरे मोरबिग्रहम्‌ । देखत्थ दक्षिण यक्‍्त्र देवटेवस्दार्थकम्‌
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2845)
- **Original**: विद्यापर्ट समारूज वह्िमण्छलमध्यगम्‌। द्वितीयं शिवनीजेपु कल्थस्यट्रकर््रन्यित्ा[
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2846)
- **Original**: शाम्मोरदक्षिणदिग्भागे शफत्या स्द समर्भितम्‌। पवित्र परम॑ बह्य प्रार्थित में ग्रवच्छतु
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2847)
- **Original**: जो अक्कन आदिके समान द्याम, घोर झरीरवाल्म एवं अधघोर नामसे प्रसिद्ध है, महादेबजीके दक्षिण मुखका अभिमानी तथा जिवके दक्षिणभागमें शक्तिके साथ पूजित है, बह पवित्र परब्रह्म मुझे मेरी अभीष्ठ वस्तु अ्दान करे
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2848)
- **Original**: 33--35
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2849)
- **Original**: कुक्कूसक्षोदसंकाश वामाझु्य॑ वसवेषधूक्‌ । बकतरमुत्तरमी शस्थ प्रतिक्ायों. प्रतिष्ठितम्‌
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2850)
- **Original**: वारिमिण्दछमध्यस्थ॑ महादेवार्चन रतम्‌। तुरीय॑ शिवश्रंजेषु त्रयोदशकलान्वितम्‌
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2851)
- **Original**: देजस्वोत्तरदिग्शागे शाकत्या सद्द समर्चितम्‌
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2852)
- **Original**: पत्निन्ने पसमे ब़ह्य प्रार्खत ये प्रदक्ततु
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2853)
- **Original**: सुन्दर अभिमानी है, प्रतिष्ठाकस्ममें प्रतिप्लित जह्क्के मसण्डलपें ब्रिराजमान त़था क युक्त है और महादेवजीके उत्तरभागपें शक्तिके साथ पूजित हुआ है, वह पश्ित्र परग्रह्य पेरी प्रार्थना पूर्ण करे
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2854)
- **Original**: 36--38
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2855)
- **Original**: च्राह्नकुच्देन्दुबचले सद्यालये सौभ्यलक्षणग्‌। विवस्थ पश्चिय॑ अक्‍्त्रे खिवपादार्चने रतम्‌
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2856)
- **Original**: निवृतिपदनिए॑य॒फुथिव्या समवस्थितम्‌
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2857)
- **Original**: सशुततीय॑ शिववीजेषु कत्मपिआए्टमियुतम्‌
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2858)
- **Original**: देखस्प पत्मिसे भागे शवत्या सह समर्चितस्‌। गयित परम जाप आर्थेत में प्रसच्छतु
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2859)
- **Original**: जो शाक्व, कुन्द और चन््रमाके समान थबरू, सौम्य तथा सद्योजात नामसे विख्यात है, भगजत्रानू शिवके पक्षिम सुखका अभिमानी एवं शिवचरणोंकी अर्चनामें रत है, निवृत्तिकल्ममें प्रतिष्ठित तथा पृथ्वी- मण्डलमें स्थित है, शिलबोजोंमें तृतीय, आठ कलाओंसे युक्त और महादेखजीके पश्चिम- भागमें झक्तिके साथ पूजित हुआ है, वह पत्रित्र परब्रह्म मुझे मेरी श्रार्थित खस्तु दे
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2860)
- **Original**: शिवस्य त॒ शिवायाश्व हन्मूर्ती शिवभाविते। तथोराज्ञों पुरश्कृत्य ते मे काम प्रयच्छताम्‌
- **Translation**: 

---

