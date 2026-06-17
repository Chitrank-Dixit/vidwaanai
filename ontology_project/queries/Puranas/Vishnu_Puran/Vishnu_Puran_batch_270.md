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

### Verse 1 (Vishnu Puran 0.5381)
- **Original**: 37 काप्योदकप्रदान॑ ते मयैतत्कधित नृप
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5382)
- **Original**: यद्दत््वा प्रीणयत्येतन्मनुष्यस्सकलं जगत्‌। जगदाप्यायनोद्धूत॑ पुण्यमाप्नोति चानध
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5383)
- **Original**: 38 आज्रम्य च ततो द्यात्सूयाय सलिलाझलिप्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5384)
- **Original**: 39 नमो विवस्वते ब्रह्मभास्वते विष्णुतेजसे । जगत्सवित्रे शुच्चये सवित्रे कर्मसाक्षिणे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5385)
- **Original**: 40 ततो .गूहार्चन॑ कुर्यादभीष्टसुरपूजनप्‌ । जलाभिषेकै: पुष्पैश्न धूपाहौश्न निवेदनम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5386)
- **Original**: 41 अपूर्वमप्निहोत्रं च कुर्यात्माग्ब्रह्मणे नृप
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5387)
- **Original**: 42 प्रजापति सुमुद्दिश्य दद्यादाहतिमादरात्‌ । गुल्े भ्य: काइयपायाथ ततो 5नुमतये क्रमात्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5388)
- **Original**: 43 तच्छेष॑ मणिके पृथ्वीपर्जन्येभ्य: क्षिपेत्तत: । द्वारे धातुर्विधातुश्न मध्ये च ब्रह्मणे क्षिपेत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5389)
- **Original**: 44 गृहस्य॒पुरुषव्याप्र दिग्देवानपि में श्रृूणु
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5390)
- **Original**: 45 इन्द्राय. धर्मराजाय. वरुणाय तथेन्दवे । प्राच्यादिषु खुधो द््यादधुतशेषात्यक बलिम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5391)
- **Original**: 46 प्रागुत्ते च दिग्भागे धन्वन्तरिबर्लिं बुधः । निर्वपेहैश्नदेव॑ च कर्म कुर्यादत: परम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5392)
- **Original**: 47 वायव्यां यायवे दिक्षु समस्तासु यथादिशम्‌ । हूँ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5393)
- **Original**: जो मेंर बन्धु अथवा अबचन्धु हैं, तथा जो अन्य जन्मोमें मेरे बच्चु थे एवं और भी जो-जो मुझसे जरूकी इच्छा रखनेवाले हैं वे सत्र मेंरे दिये हुए जलसे परितृपत हों
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5394)
- **Original**: क्षुधा और दृष्णासे व्याकुछ जीव कहीं भी तयों न हो मेरा दिया हुआ यह तिल्लेदक उनको तृप्ति प्रदान करे'
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5395)
- **Original**: हे नृप ! इस प्रकार सैंने तुमसे यह क्ममम्य- तर्पणका निरूपण किया, जिसके करनेसे मनुष्य सकल संसारकों तृप्त कर देता है और हे अनघ ! इससे उसे जगतूकी तृप्निसे होनेवाल्य पुण्य प्राप्त होता हैं ।। 38
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5396)
- **Original**: इस प्रकार उपरोक्त जीवोंको श्रद्धापूर्वक काम्यजल- दान करनेके अनन्तर आचमन करे और फिर सूर्यदेबको जल्खज्ञलि दे ! 39
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5397)
- **Original**: [उस समय इस प्रकार कहे--
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5398)
- **Original**: ] “भगवान्‌ जिवस्वान॒कों नमस्कार है जो वेट-वेच्य और बिष्णुके तेजस्स्वरूप हैं तथा जगत्‌को उत्पन्न करनेजाले, अति पवित्र एव कर्मोंके साक्षी हैं.
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5399)
- **Original**: तदनन्तर जल्ाभिषेक और पुष्प तथा धूपादि निवेदन करता हुआ गृर्देव और इश्टदेबका पूजन करे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5400)
- **Original**: हे नृप ! फिर अपूर्व अग्निहोत्र करे, उसमें पहले ब्रद्माको और तदनत्तर क्रमश: प्रजापति, गुद्दा, काइयप और अनुमतिको आदरपूर्वक आहुतियाँ दें
- **Translation**: 

---

